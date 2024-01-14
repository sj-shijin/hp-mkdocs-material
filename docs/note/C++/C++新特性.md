# C++新特性

## 右值引用

### 区分左值，右值，左值引用，右值引用

- 左值：顾名思义，等号左边的值，有实际内存地址，可修改
- 右值：等号右边的值，1.纯右值（常数，表达式等）；2.将亡值（语句结束后会被抛弃的值）
- 左值引用：`T&`，非常熟悉，相当于别名，只能接受左值
- 右值引用：`T&&`，新特性，只能接受右值
- 常量左值引用：`const T&`，非常熟悉，可以接受左值或右值
- 常量右值引用：无使用价值

**gap:右值引用是一个左值。**

易错的左值：

1. 字符串字面量：`"hello world"`
2. 前置\+\+或\-\-：`++a`
3. 右值引用：`T&& a = T(1)`，此处a是左值

易错的右值：

1. 后置\+\+或\-\-：`a++`
2. lambda表达式：`[](){}`
3. 转为右值的表达式：`static_cast<T&&>(fvalve)`，即std::move()，std::forward()

### 移动语义std::move()与移动构造（赋值）语句

std::move()强制转为右值

```c++
class Test
{
    int *data;
    Test(int len)
    {
        data = new int[len];
    }
    Test(Test &&t)
    {
        data = t.data; //移动
        t.data = nullptr; //设为默认值，故右值引用不能为const，且data中的数据不会被释放。
    }
    operator Test &operator=(Test &&t)
    {
        delete[] data; //释放原先占用的空间
        data = t.data; //移动
        t.data = nullptr; //设为默认值，故右值引用不能为const，且data中的数据不会被释放。
    }
    ~Test()
    {
        if (!data)
        {
            delete[] data;
        }
    }
};
```

### 完美转发std::forward()

```c++
template <typename T>
void print(T &t)
{
    cout << "lvalue" << endl;
}
template <typename T>
void print(T &&t)
{
    cout << "rvalue" << endl;
}
template <typename T>
void TestForward(T &&v)
{
    print(v);
    print(std::forward<T>(v));
    print(std::move(v));
}
```

1. `TestForward(1)`：模板推导，`T = int`

   `v`是右值引用，是左值

   `std::forward<int>(v)`转发为v之前的值，是右值

   `std::move(v)`强制转为右值，是右值

2. `int x = 1 , TestForward(x)`：模板推导，`T = int &`，此时函数参数实则为`int & v`

   `v`是左值引用，是左值

   `std::forward<int &>(v)`转发为v之前的值，是左值

   `std::move(v)`强制转为右值，是右值

3. `int x = 1 , TestForward(std::forward<int>(x))`：模板推导，`T = int`

   `v`是右值引用，是左值

   `std::forward<int>(v)`转发为v之前的值，是右值

   `std::move(v)`强制转为右值，是右值

4. `int x = 1 , TestForward(std::move(x))`：与3相同

### 注意：谨慎定义复制语义，可能会导致自动隐式移动语义失效

构造与赋值同理，这里以构造为例：

```c++
struct S1
{
    std::string _s;
    S(std::string s) : _s(s) {}
};
struct S2
{
    std::string _s;
    S(std::string s) : _s(s) {}
    S(const S &s) : _s(s._s) {}
};
struct S3
{
    std::string _s;
    S(std::string s) : _s(s) {}
    S(const S &s) : _s(s._s) {} 
    S(S &&s) : _s(std::move(s._s)) {}
};
```

我们希望使用move语句进行移动构造，而不希望进行赋值：

1. `S1 a("abc") , S1 b(std::move(a))`：会隐式调用移动构造，结束后`a._s`的值为空。
2. `S2 a("abc") , S2 b(std::move(a))`：由于常量左值引用可以接受右值，故会进入到显式定义的复制语句中，产生冗余。
3. `S3 a("abc") , S3 b(std::move(a))`：进入显式定义的移动构造语句中，与1相同。

## 折叠表达式

便于展开可变模板参数包

- 一元右折叠`(E op ...)`：`e[1] op (... op (e[n-1] op e[n]))`
- 一元左折叠`(... op E)`：`((e[1] op e[2] op ...) op e[n]`
- 二元右折叠`(E op ... op I)`：`e[1] op (... op (e[n-1] op (e[n] op I))`
- 二元左折叠`(I op ... op E)`：`(((I op e[1]) op e[2] op ...) op e[n]`

理解：折叠展开的顺序是递归调用顺序。

```c++
template <typename ... Ts>
auto sum_right(Ts ... ts) return (ts + ...); //右折叠
template <typename ... Ts>
auto sum_left(Ts ... ts) return (... + ts); //左折叠
template <typename ... Ts>
auto sum_right2(Ts ... ts) return (ts + ... + 0); //二元右折叠
template <typename ... Ts>
auto sum_left2(Ts ... ts) return (0 + ... + ts); //二元左折叠

sum_right(1,2,3); // 1+(2+3)
sum_left(1,2,3); // (1+2)+3
sum_right2(1,2,3); // 1+(2+(3+0))
sum_left2(1,2,3); // ((0+1)+2)+3
sum_right(); // 报错
sum_right2(); // 0
```

可以传入其他参数

```c++
template <typename R, typename ... Ts>
auto sum_f(const R& f, Ts ... ts)
{
    return (f(ts) + ...);
}
auto sq = [](auto x)
{ return sqrt(x); };
auto sum = sum_f(sq, 1, 2, 3, 4); //平方根之和
```
