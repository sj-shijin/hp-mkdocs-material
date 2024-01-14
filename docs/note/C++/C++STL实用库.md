# C++STL实用库

## Utility库介绍

分为与语言支持和通用库两部分

## 固定宽度整数类型（def in `<cstdint>`）

`int8_t/int16_t/int32_t/int64_t`：固定位数

`int_fast8_t/int_fast16_t/int_fast32_t/int_fast64_t`：最快的，可能使用更多空间

`int_least8_t/int_least16_t/int_least32_t/int_least64_t`：至少的，可能使用更多空间

`intmax_t`：最大的

`intptr_t`：指针的位数

无符号整型同理。

## 固定宽度浮点数类型（def in `<stdfloat>`）

`float16_t`：1s+5e+10p

`float32_t`：1s+8e+23p

`float64_t`：1s+11e+52p

`float128_t`：1s+15e+113p

`bfloat16_t`：1s+8e+7p(for ai)

## 数值界限（def in `<limits>`）

`numeric_limits<T>::max()`

`numeric_limits<T>::min()`

`numeric_limits<T>::infinity()`

`numeric_limits<T>::quiet_NaN()`

`numeric_limits<T>::signaling_NaN()`：进行运算时会提示。

## 字节（def in `<cstddef>`）

`enum class byte : unsigned char{};`

```c++
#include <cstddef>

std::byte b{x};
std::to_integer<int>(b);
// b可进行所有位运算
```

## 智能指针（def in `<memory>`）

| 类型            | 解释                                                   | 版本    |
| --------------- | ------------------------------------------------------ | ------- |
| unique_ptr\<T\> | 独占所有权，不能复制(可以从函数返回)，可以取值，取右值 | C\+\+11 |
| shared_ptr\<T\> | 共享所有权，可以复制                                   | C\+\+11 |
| weak_ptr\<T\>   | 临时所有权，转换为shared才可以进行访问                 | C\+\+11 |

```c++
unique_ptr<T> up1 = make_unique<T>(new T);
unique_ptr<T> up2(new T);

T* p1 = up1.release(); //释放up1，返回普通指针
auto up3 = move(up2);
T *p4 = new T;
up3.reset(p4); //更换绑定，原空间被释放
up3.reset(nullptr); //释放
```

```c++
shared_ptr<T> sp1 = make_share<T>(new T);
shared_ptr<T> sp2(new T);
shared_ptr<T> sp3(sp1); //sp1.use_count() == 2 ; sp3析构后会减少
//当最后一个shared_ptr被析构时，开辟的空间被释放
sp2.unique() == (sp2.use_count() == 1)
sp1.use_count() == 2
```

共享指针的循环引用问题：

```c++
class A
{
public:
  shared_ptr<B> Bp;
};
class B
{
public:
  shared_ptr<A> Ap;
};

shared_ptr<A> ptrA = make_shared<A>();
shared_ptr<B> ptrB = make_shared<B>();
ptrA->Bp = ptrB;
ptrB->Ap = ptrA;
//只会构造，不会析构，会导致内存泄漏
```

weak_ptr没有解引用功能，不会影响指向区域的内存的生命周期。

```c++
shared_ptr<T> sp1 = make_share<T>(new T);
weak_ptr<T> wp1 = sp1; //weak_ptr必须使用shared_ptr初始化
//此时sp1.use_count()不会增加
share_ptr<T> sp2 = wp1.lock(); //只能通过构造shared_ptr的方式解引用

wp1.expired() //检验该指针是否合法：即对应的地址是否已经被释放？空指针？
```

## 初始化列表（def in `<initializer_list>`）

`template< class T > class initializer_list;`

其中每个元素均为常量。用法与vector类似。多用于函数参数等。

## 三路比较运算符（def in `<compare>`）

C\+\+20可以通过定义两个运算符实现原有的六种运算符。

- `a <=> b`：存在多种返回值（见下），该返回值与0比较的结果（小于，等于，大于），分别对应a与b的大小关系。当`<,<=,>,>=`运算符缺省时，会自动使用`<=>`运算符得到结果。

- `a == b`：相等，返回bool值。当`!=`运算符缺省时，会自动使用`==`结果的逻辑反。

### 比较的类别

- 偏序关系（partial_ordering）

  偏序关系代表并非任意两值都具有序关系，但相等不一定不可分。例：浮点数的三路比较运算符。

  ```c++
  #include <compare>
  #include <limits>
  
  0.0 <=> -0.0 == partial_ordering::equivalent //相等不一定不可分
  1.0 <=> 1.0 == partial_ordering::equivalent
  1.0 <=> 2.0 == partial_ordering::less
  2.0 <=> 1.0 == partial_ordering::greater
  1.0 <=> numeric_limits<double>::quiet_NaN() == partial_ordering::unordered //存在不可比较的值
  ```

- 弱序关系（weak_ordering）

  弱序关系代表任意两值均具有序关系，但相等不一定不可分。例：自定义的非最简分数类。

  ```c++
  struct Fraction {
    int dividend;
    int divisor;
  };
  std::weak_ordering operator<=>(const Fraction& lhs, const Fraction& rhs) noexcept {
    auto lhs_n = lhs.dividend;
    auto lhs_d = lhs.divisor;
    auto rhs_n = rhs.dividend;
    auto rns_d = rhs.divisor;
  
    auto d = std::lcm(lhs_d, rhs_d);
    auto n1 = d / lhs_d * lhs_n;
    auto n2 = d / rhs_d * rhs_n;
    return n1 <=> n2;
  }
  ```

- 强序关系（strong_ordering）

  强序关系代表任意两值均具有序关系，但相等一定不可分。例：整数。

三种序关系条件依次增强，故较强的序关系可以向较弱的序关系隐式转换。

## 交换（def in `<utility>`）

- `swap`
- `T exchange(T &obj, U&& new_value)`：new_value转移到obj中，返回会obj的原始值。

## 类型操作（def in `<utility>`）

- `as_const`：返回一个常量引用
- `declval`：返回函数的返回值
- `decltype`：返回表达式的类型（比如lambda函数）
- `move`，`forward`：见C\+\+新特性的右值引用部分
- `move_if_noexcept`：如果类型T的移动构造函数被noexcept修饰符保证过，则返回`T&&`，否则返回`const T&`
- `forward_like`：可能返回带有const修饰的值，更完美的转发？

## 整数比较函数（def in `<utility>`）

- 不进行隐式类型转换的比较：`cmp_equal`，`cmp_not_equal`，`cmp_less`，`cmp_greater`，`cmp_less_equal`，`cmp_greater_equal`

  ```c++
  -1 > 0u == true
  cmp_greater(-1,0u) == false
  ```

- 不进行隐式转换的`in_range`：

  ```c++
  in_range<size_t>(-1) == false
  ```

## pair（def in `utility`）和tuple（def in `tuple`）

- pair

  ```c++
  pair<T1, T2> p1 = {t1, t2};
  auto p2 = make_pair(1, 3.14);
  p2.first == get<0>(p2) == get<int>(p2) == 1;
  p2.second == get<1>(p2) == get<double>(p2) == 1;
  ```

- piecewise_construct：用于消除构造函数歧义

  ```c++
  struct Foo
  {
      Foo(std::tuple<int, float>){} //构造函数1
      Foo(int, float){} //构造函数2
  };
  
  std::tuple<int, float> t(1, 3.14);
  std::pair<Foo, Foo> p1(t, t); //使用构造函数1
  std::pair<Foo, Foo> p2(std::piecewise_construct, t, t); //使用构造函数2
  ```

- tuple

  ```c++
  tuple<T1, T2, T3> tuple1 = {t1, t2, t3};
  auto tuple2 = make_tuple(1, "Foo", 3.14)
  get<0>(tuple1) == get<T1>(tuple);
  
  tuple_size<tuple<T1, T2, T3>> == 3; //运行时
  tuple_size_v<tuple<T1, T2, T3>> == 3; //编译时
  //pair同理
  ```

- 解构（tie，结构化绑定）

  ```c++
  pair<T1, T2> p1 = {t1, t2};
  T1 a;
  T2 b;
  tie(a, b) = p1;
  
  auto [a, b] = p1; //better
  //tuple同理
  ```

- apply：将pair，tuple解构到函数参数

  ```c++
  int add(int, int) {}
  apply(add, pair(1, 2));
  ```

## 汇总类型和类型擦除包装器

- optional（def in `<optional>`）

  ```c++
  std::optional<std::string> create(bool b)
  {
      if (b)
        return "Godzilla" ;
      return {};
  }
  auto create2(bool b)
  {
      return b ? std::optional<std::string>{"Godzilla"} : std::nullopt;
  }
  
  optional<string> o = create(false)
  o.has_value() == false
  o.value_or("no value") == "no value"
  create2(true).value == "Godzilla"
  ```

- variant（def in `<variant>`）比tuple更安全

  ```c++
  variant<int, float> v;
  v = 42; //自动保存到int中
  holds_alternative<int> v == true; //int有值
  holds_alternative<float> v == false; //double无值
  get<int>(v) == get<0>(v) == 42
  ```

- any（def in `<any>`）

  ```c++
  any a = 1;
  a.type().name() == "int";
  any_cast<int>(a) == 1;
  any_cast<double>(a); //报错
  a.has_value() == true;
  a.reset(); // a.has_value() == false
  ```

- expected（def in `<expected>`）(C\+\+23)

## Bitset（def in `<bitset>`）

```c++
bitset<4> a{12};
bitset<4> b{"0011"}
//位运算
//all，any，none，flip（取反）
b[2] = true; // 0111
b.count() == 3;
b.size() == 4;
b.to_ullong() == 0b0111ull;
b.to_string() == "0011";
```

## 函数对象

### 函数类

即重载了括号运算符`()`的类。

```c++
class FuncObj
{
public:
    void operator() (int arg) {}
}
FuncObj func;
func(val);
FuncObj()(val);
```

函数可以共享类中的状态。

```c++
class SumMe
{
    int sum{0};
 public:
    SumMe() = default;
    void operator()(int x) {
        sum += x;
    }
    int getSum() const {
        return sum;
    }
}

int main()
{
    vector<int> intVec{0, 1, 2, 3, 4, 5};
    SumMe sumMe = for_each(inVec.begin(), intVec.end(), SumMe());
    cout << sumMe.getSum();
}
```

可以将函数调用的结果储存在函数对象中。

### Lambda

本质上为定义了一个函数类，重载了（）运算符，返回一个实例（函数、函数指针）。

`[ captures ] < tparams > t-requires front-attr ( params ) specs exception back-attr trailing-type requires { body }`

capture作为函数类的私有成员，params作为重载函数的参数，body作为重载函数主体，trailing-type作为返回值（省略时会自动推断）

- captures捕获
  - [=]：按值的方式捕获所有变量，默认不可更改
  - [&]：按引用的方式捕获所有变量
  - [a,&b]：按值捕获a，对值的捕获可以进行初始化，按引用捕获b
  - [this]：按引用的方式捕获当前对象
  - [\*this]：按值的方式捕获当前对象
- specs
  - mutable：允许body更改按值捕获的参数和调用non-const成员函数。

### `function`类（def in `<functional>`）

```c++
class Test
{
    Test(int num) : num_(num) {}
    void add_print(int i) const { cout << num_ + i << endl; }
    int num_;
}

std::function<void(int)> f = [](int x){cout << x <<endl;};

std::function<void(const Test&, int)> f_add_print = &Test::add_print;
f_add_print(567,1); // 568
const Test t(1234);
f_add_print(t,1); // 1235

std::function<int(const Test&)> f_get_num_ = &Test::num_;
cout << f_get_num_(t); //1234

//可以接受多种函数（标准函数，函数类实例，lambda函数，类成员函数等）
//可使用函数形式的调用
//会产生一定性能损失，使用了虚函数，编译器能进行的优化较少
```

- invoke：进行函数调用的函数

  ```c++
  //接上
  invoke(f,1); //函数+参数
  invoke(&Test::add_print, t, 1); //成员函数+类实例+参数
  invoke(&Test::num_, t); //可视为成员函数+类实例
  ```

- bind：组合现有的函数，创建闭包

  ```c++
  void f(int x1, int x2, int &x3,const int &x4) {}
  
  using namespace std::placeholders; //for _1,_2,...
  
  int n1 = 7, n2 = 8;
  auto bdf = bind(f, _2, 5, n1, n2); //此处使用n的值创造了闭包，不会被改变
  n1 = 10, n2 = 12;
  bdf(1, 2, 1001); // 调用了f(2,5,7,8)，1，1001是多余的参数
  ```

- ref和cref：提示函数此处为引用参数传递。

  ```c++
  //接上
  auto bdf2 = bind(f, _2, 5, ref(n1), cref(n2));
  n1 = 111, n2 = 222;
  bdf2(1, 2, 1001); // 调用了f(2,5,111,222);
  ```

### 运算符函数对象

- plus,minus,multiplies,divides,modulus,negate
- equal_to,not_equal_to,greater,less,greater_equal,less_equal
- logical_and,logical_or,logical_not
- bit_and,bit_or,bit_xor,bit_not

## 哈希支持（def in `<functional>`）

```c++
auto std_hasher = hash<strting>{};
size_t val = std_hasher("123");
```

注意：整型的std::hash会返回其原来的值，不能以此为基础做多个整型的hash。

## 日期和时间（def in `chrono`）

```c++
auto start{chrono::system_clock::now()};
//计时器system_clock（系统时间）,steady_clock（无闰秒），high_resolution_clock(shortest tick period)
//c++20新增 utc_clock,tai_clock,gps_clock,file_clock

auto end{chrono::system_clock::now()};
chrono::duration<double, std::nano> duration{end - start};
// std::nano, std::micro, std::milli, (默认为秒) ，std::ratio<60>(分钟) ，std::ratio<3600>(小时)
//c++20新增 std::ratio<86400>，std::ratio<604800>，std::ratio<2629746>，std::ratio<31556952>

cout << duration.count() << endl; //c++11
cout << duration << endl; //c++20
```

### 与CPU时间戳计数器（rdtsc指令）的对比

- 与cpu频率和是否休眠有关（Nehalem架构后解决）
- 乱序执行：该指令执行时待测量的代码可能已经运行完毕（执行前增加一个内存屏障解决）
- 每个核心都有自己的TSC（Nehalem架构后解决单个处理器的跨核同步，但多处理器由设计决定）
- 虚拟化（云服务器，docker）：可能不对该指令进行处理

**建议使用chrono，会自动选择合适的时钟源。**

## 基本字符串转换（def in `charconv`）

- to_char
- from_char

## 格式化库（def in `format`）

- 参数索引

  ```c++
  format("...{}...{}...{}", x, y, z);
  format("...{0}...{1}...{0}", x, y);
  //不能混合使用
  ```

- 类型规格与格式选择

  `format("{0:}",x)`：在冒号后指定格式`[[fill]align][sign][#][0][width][.precision][type]`

  1. width

     占用的最小宽度，{w}代表动态宽度，取自该参数的后一个(或指定索引)。

     ```c++
     int i {42};
     std::cout << std::format("|{:5}|", i) << std::endl;
     // |   42|
     std::cout << std::format("|{:{}}|", i, 5) << std::endl;
     // |   42|
     ```

  2. [fill]align（有效的前提是设置width）

     fill是未达到width时的填充字符，align代表字段中的对齐方式：`<`：左对齐，`>`：右对齐，`^`：居中对齐

     ```c++
     int i {42};
     std::cout << std::format("|{:<7}|", i) << std::endl;
     // |42     |
     std::cout << std::format("|{:>7}|", i) << std::endl;
     // |     42|
     std::cout << std::format("|{:_>7}|", i) << std::endl;
     // |_____42|
     std::cout << std::format("|{:_^7}|", i) << std::endl;
     // |__42___|
     ```

  3. sign：`+`：显示正数和负数符号，`-`：只显示负数符号，`(space)`：空格代表负数显示负号，整数使用空格。

     ```c++
     int i {42};
     std::cout << std::format("|{:<5}|", i) << std::endl; // |42   |
     std::cout << std::format("|{:<+5}|", i) << std::endl; // |+42  |
     std::cout << std::format("|{:< 5}|", i) << std::endl; // | 42  |
     std::cout << std::format("|{:< 5}|", -i) << std::endl; // |-42  |
     ```

  4. `#`：备用格式，为整数时在二进制，八进制，十六进制前添加`0b,0,0x`，为浮点数时始终输出小数点。

  5. type

     - 整数：`d`：十进制整数，`x`：小写十六进制整数，`X`：大写十六进制整数，`o`：八进制整数，`b`：二进制整数。
     - 浮点数：`f`：固定点表示法，`e`：小写科学计数法，`E`：大写科学计数法，`g`：自动选择f或e，`G`：自动选择f或E，`a`：小写十六进制，`A`：大写十六进制。
     - 字符：`c`：字符，所有整数type
     - 字符串：`S`
     - 布尔：`s`：文本输出true或false，所有整数type，和字符`c`。
     - 指针：`p`

  6. precision

     只能用于浮点数（小数位数）和字符串（输出字符数）。与width类似可以接受参数。

     ```c++
     double d {3.1415 / 2.3};
     std::cout << std::format("|{:12g}|", d) << std::endl;
     // |    1.365870|
     std::cout << std::format("|{:12.2}|", d) << std::endl;
     // |        1.37|
     std::cout << std::format("|{2:{0}.{1}f}|", 12, 3, d) << std::endl;
     // |       1.366|
     ```

  7. `0`：如果设定了width，但没有设置对齐，则在数值前补0。

- 自定义类型的格式化输出

  自定义模板类formatter：方法parse（处理标识符）和方法format（输出）。

  [formatter](https://en.cppreference.com/w/cpp/utility/format/formatter)

- format_to和format_to_n：可以将format的结果输出到一个output iterator中

- formatted_size：输出format的结果的zi'fu
fu
