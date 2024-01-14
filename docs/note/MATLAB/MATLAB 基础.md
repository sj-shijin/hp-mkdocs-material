# MATLAB 基础

## 1.常用命令

| 命令名称 | 功能简介       |
| -------- | -------------- |
| clear    | 清空工作区     |
| clc      | 清空命令行窗口 |
| clf      | 清空图像窗口   |

## 2.基本函数

| 函数名称 | 功能简介     |
| -------- | ------------ |
| abs      | 绝对值（模） |
| sqrt     | 算术平方根   |
| exp      | 自然指数     |
| log      | 自然对数     |
| round    | 四舍五入     |
| fix      | 舍去小数     |
| size     | 测量矩阵大小 |
| length   | 数组长度     |
| numel    | 元素总数     |
| sort     | 排序         |
| find     | 查找         |

- 一般函数介绍

  ```matlab
  return1=func(parm,'name',value)
  [return1,return2]=func(parm,'name',value)
  [~,return2]=func(parm,'name',value)
  ```

  如果只需要多个返回值中的一部分，可以将其他返回值的用~代替
  调用函数时可以通过一个或多个名称-值组合传递部分变量。

- 声明函数

  ```matlab
  function return1=functionname(parm1,parm2)
    return1=value1;
  end
  function [return1,return2]=functionname(parm1,parm2)
    return1=value1;
    return2=value2;
  end
  ```

  若函数所在的文件名为functionname.m，且其放置于matlab的搜索路径中，则在所有其他文件中均可调用该函数。
  若不然，只能在当前文件中调用该函数。

- sort的用法

  ```matlab
  B=sort(___)
  [B,I]=sort(___)
  ```

  [B,I]表示返回值保存在B中，其索引保存在I中。

  ```matlab
  sort(A)
  sort(A,dim)
  sort(___,direction) % direction in ['ascend'(default),'descend']
  ```

  dim为常数，按照指定的维度进行排序
  direction为字符串，指定排序方向

- find的用法

  ```matlab
  k=find(___)
  [row,col]=find(___)
  [row,col,v]=find(___)
  ```

   k为线性索引向量

   row，col为返回元素的行和列下标

   v为对应的元素值

  ```matlab
  find(x)
  find(x,n)
  find(x,n,direction) % direction in ['first'(default),'last']
  ```

  寻找x中的每个非零元素的索引（更多的时候会使用逻辑运算符）

  n表示指定direction方向下的前n个索引。

## 3.条件为true时执行语句（if，elseif，else）

```matlab
if expression
    statements
elseif expression
    statements
else
    statements
end
```

## 4.循环语句（for）

```matlab
for index = values
    statements
end
```

```matlab
for i=1:100
    statements
end
for i=50:-2:0
    statements
end
```

## 5.矩阵相关函数

| 函数名称'name' | 功能简介         |
| -------------- | ---------------- |
| zeros          | 零矩阵           |
| ones           | 单位矩阵         |
| diag           | 对角矩阵         |
| linspace       | 线性等分数组     |
| logspace       | 对数等分数组     |
| dot            | 求两个向量的内积 |
| det            | 求矩阵的行列式   |
| inv            | 求矩阵的逆       |
| rref           | 化为行最简型     |
| eig            | 特征值、特征向量 |
| ploy           | 特征多项式       |
