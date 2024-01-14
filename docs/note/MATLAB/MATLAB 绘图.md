# MATLAB 绘图

## 1.创建图像窗体

```matlab
f=figure(___) %创建Figure对象
figure(f) %将f作为当前图窗，并显示在其他所有图窗上方
figure(Name,Value) %使用一个或多个名称-值组合修改窗体的属性
figure('Name','figurename') %将图窗的名称设置为'figurename'
```

## 2.创建子图

```matlab
subplot(m,n,p) 
subplot(m,n,p,'replace');
```

将当前图窗分为m*n的网格，并在下标为p的位置子图。

'replace'则会清空当前子图中的内容。

```matlab
subplot(3,3,4) %在当前图窗的左中区域绘制子图
subplot(3,3,[5,6,8,9]) %在当前图窗的右下大区域绘制子图
```

## 3.二维曲线（plot）

```matlab
plot(X,Y)
plot(X,Y,LineSpec)
```

如果X和Y都是向量，则它们的长度必须相等。

如果X和Y都是矩阵，则它们的大小必须相等，函数绘制对应列向量的曲线，曲线数量与列数相同。

LineSpec为设置曲线的线型、标记符号和颜色。

| 线型 | 说明 | 线型 | 说明   |
| ---- | ---- | ---- | ------ |
| -    | 实线 | :    | 点线   |
| --   | 虚线 | -.   | 点划线 |

| 标记 | 说明 | 标记 | 说明   |
| ---- | ---- | ---- | ------ |
| o    | 圆圈 | ^    | 上三角 |
| +    | 加号 | v    | 下三角 |
| *    | 星号 | >    | 右三角 |
| .    | 点   | <    | 左三角 |
| x    | 叉号 | p    | 五角形 |
| s    | 方形 | h    | 六角形 |
| d    | 菱形 |      |        |

| 颜色 | 说明 | 颜色 | 说明   |
| ---- | ---- | ---- | ------ |
| r    | 红色 | m    | 品红色 |
| y    | 黄色 | c    | 青蓝色 |
| b    | 蓝色 | w    | 白色   |
| g    | 绿色 | k    | 黑色   |

```matlab
plot(X,Y,'r--o') %红色虚线，点标记为圆圈。
plot(X,Y,'b.') %蓝色散点。
```

## 4.直方图（histogram）

## 5.条形图（bar）、水平条形图（barh）

## 6.其他图窗设置

- 在图窗中绘制多个图形

  ```matlab
  hold on
  ```

- 坐标区域（axis）

  ```matlab
  axis([0,pi,-1,1]) %x轴的范围是0~pi，y轴的范围是-1~1
  axis([0,+inf,-inf,inf]) %x轴的左侧为0，右侧为默认值，y轴范围默认。
  ```

- 添加标题（title）

  ```matlab
  title('titlename')
  ```

  为当前图窗添加标题，如果是子窗的话就为子窗添加标题。

- 添加x轴标签（xlabel）、添加y轴标签（ylabel）

  ```matlab
  xlabel('xlabelname')
  ylabel('ylabelname')
  ```

- 添加图例（legend）

  ```matlab
  legend('legendname1','legendname2',...)
  legend(___,'Location','Lname')
  ```

  按照该图窗或子图中图像的绘制顺序添加图例。

  Location用于调整图例在图像上的位置。

  | Lname | 位置说明 | Lname        | 位置说明 |
  | ----- | -------- | ------------ | -------- |
  | North | 上方     | NorthEast    | 右上方   |
  | South | 下方     | NorthWest    | 左上方   |
  | East  | 右方     | SouthEast    | 右下方   |
  | West  | 左方     | SouthWest    | 左下方   |
  | Best  | 最佳位置 | LnameOutside | 图框外侧 |

  ```matlab
  plot(X1,Y1);
  plot(X2,Y2);
  legend('line1','line2','Location','EastOutside');
      % 图例位于右侧图框外
  ```

- 在含有子图的图窗中添加总标题（suptitle）

  ```matlab
  suptitle('suptitlename')
  ```

## 7.三维绘图

- 产生网格（meshgrid）

  ```matlab
  [X,Y]=meshgrid(1:4,-1:1)
  reselt:
  X =	1	2	3	4
  	1	2	3	4
  	1	2	3	4
  Y =	-1	-1	-1	-1
  	0	0	0	0
  	1	1	1	1
  ```

  X，Y大小相同，且可以表示网格上每个点的坐标。

- 绘制网格图（mesh）

  ```matlab
  mesh(X,Y,Z)
  ```

  X，Y，Z为大小相同的矩阵，Z为X-Y平面网格点上的高度值。

  mesh为只有线色无面色的网格图，线的颜色与高度相关。

- 绘制曲面图（surf）

  ```matlab
  surf(X,Y,Z)
  surfc(X,Y,Z)
  shading interp; %去掉网格使曲面光滑
  ```

  X，Y，Z为大小相同的矩阵，Z为X-Y平面网格点上的高度值。

  surf为线色为黑色且面色与高度相关的曲面图。

  surfc在surf的基础上还会在X-Y平面上显示等高线。

- 三维曲线（plot3）

  ```matlab
  plot3(X,Y,Z)
  ```

  与plot类似。

- 通过函数绘图（ezmesh,ezsurf）

  ```matlab
  ezmesh('f(x,y)')
  ezsurf('f(x,y)')
  ```

  绘制$z=f(x,y)$的图像。

  ```matlab
  ezmesh('x.^2+y.^2')
  ezsurf('sin(x).*cos(y)')
  ```
