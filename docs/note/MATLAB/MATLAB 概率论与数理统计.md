# MATLAB 概率论与数理统计

## 1.常用统计函数

| 函数名称'name' | 功能简介 |
| -------------- | -------- |
| mean           | 均值     |
| sum            | 总和     |
| prod           | 乘积     |
| cumsum         | 累积和   |
| cumprod        | 累积乘积 |
| std            | 标准差   |
| var            | 方差     |
| skewness       | 偏度     |
| kurtosis       | 峰度     |
| max            | 最大值   |
| min            | 最小值   |
| range          | 极差     |
| cov            | 协方差   |
| corrcoef       | 相关系数 |

- 基本用法

  ```matlab
  name(A)
  name(A,dim)
  name(A,vicdim) % except cumsum,cumprod
  name(___,nanflag) % nanflag in ['includenan','omitnan']
  ```
  
  若A为矩阵，默认对列向量进行操作，返回与列数相同的行向量。

  dim为常数，按照指定的维度，对其他维度进行操作

  vecdim为向量，在指定的多个维度上进行操作

  nanflag为字符串，指定任意计算过程中包括还是忽略NaN值。

- cumsum,cumprod的特殊用法

  ```matlab
  cumsum(___,direction)
  cumprod(___,direction) % direction in ['',reverse']
  ```

  在指定的维度逆向运行

- std,var的特殊用法

  ```matlab
  std(A,W)
  var(A,w)
  std(A,W,dim);std(A,w,vicdim)
  var(A,w,dim);var(A,w,vicdim)
  ```

  w为0（默认）或1。当w为0时，标准差或方差按N-1实现归一化（样本）；当w为1时，标准差或方差按N实现归一化（总体）。

- max,min的特殊用法

  ```matlab
  M=max(___);[M,I]=max(___)
  M=min(___);[M,I]=min(___)
  ```

  [M,I]表示返回值保存在M中，其索引保存在I中。

  ```matlab
  max(A,[],dim);max(A,[],vicdim)
  min(A,[],dim);min(A,[],vicdim)
  C=max(A,B)
  ```
  
  C返回从A或B中提取的最大元素的数组。
  
- cov,corrcoef的用法

  ```matlab
  cov(A)
  corrcoef(A)
  ```

  以A的列向量为不同的随机变量。

## 2.通用分布函数（随机数、概率密度、累积分布、逆累积分布、期望方差、参数估计）

| 函数名称'name' | 参数说明  | 函数说明                    |
| -------------- | --------- | --------------------------- |
| 'unid'         | N         | 1,2,...,N上均匀分布（离散） |
| 'bino'         | N,P       | 参数为N，P的二项分布        |
| 'poiss'        | lambda    | 参数为lambda的泊松分布      |
| 'unif'         | A,B       | [A,B]上均匀分布（连续）     |
| 'exp'          | lambda    | 参数为lambda的指数分布      |
| 'norm'         | mu,sigma  | 参数为mu，sigma的正态分布   |
| 'chi2'         | N         | 自由度为N的卡方分布         |
| 't'            | N         | 自由度为N的t分布            |
| 'F'            | N~1~,N~2~ | 自由度为N~1~，N~2~的F分布   |

- 生成随机数

  ```matlab
  R=namernd(A1,A2,A3,m,n)
  R=random('name',A1,A2,A3,m,n)
  ```

  A1,A2,A3为分布对应的参数

  m,n为生成随机数的行和列

  ```matlab
  R1=randsrc(m,n,[x;p])
  ```

  R1为生成m行n列的离散随机分布，x(i)对应的概率为p(i)

- 计算概率密度函数值

  ```matlab
  Y=namepdf(X,A1,A2,A3)
  Y=pdf('name',X,A1,A2,A3)
  ```

  Y为X处的概率密度函数值

- 计算累积分布函数值

  ```matlab
  Y=namecdf(X,A1,A2,A3)
  Y=cdf('name',X,A1,A2,A3)
  ```

  Y为X处的累积分布函数值

- 计算逆累积分布函数值

  ```matlab
  X=icdf('name',alpha,A1,A2,A3)
  ```

  X为分布函数的下alpha分位点

- 计算期望与方差

  ```matlab
  [M,V]=namestat(A1,A2,A3)
  ```

  M,V分别为分布函数的期望与方差
  
- 进行参数估计（极大似然估计）

  ```matlab
  phat=mle('name',data)
  [phat,pci]=mle('name',data,alpha) % default alpha = 0.05
  ```

  返回参数的估计值以及置信区间（置信度为1-alpha）

## 3.假设检验函数

- U检验法（方差已知，单个正态总体均值的假设检验）

  ```matlab
  h=ztest(x,m,sigma,alpha) % default alpha = 0.05
  [h,sig,ci,zval]=ztest(x,m,sigma,alpha,tail) % tail in [0,1,-1]
  ```

  x为样本，m为待检验均值，sigma为方差

  若h=0，则在显著性水平alpha下，不能拒绝原假设

  若h=1，则在显著性水平alpha下，可以拒绝原假设

  sig为观察值的概率，当sig为小概率时对原假设提出质疑

  ci为真正均值的1-alpha置信区间，zval为统计量的值。

  若原假设为$H_0:\mu=\mu_0=m$

  若tail=0，表示备择假设为$H_1:\mu\ne\mu_0=m$

  若tail=1，表示备择假设为$H_1:\mu>\mu_0=m$

  若tail=-1，表示备择假设为$H_1:\mu<\mu_0=m$

- t检验法（方差未知，单个正态总体均值的假设检验）

  ```matlab
  h=ttest(x,m,alpha) % default alpha = 0.05
  [h,sig,ci]=ttest(x,m,alpha,tail) % tail in [0,1,-1]
  ```

  各参数意义同上
  
- Jarque-Bera检验

  ```matlab
  [h,p]=jbtest(x)
  [h,p]=jbtest(x,alpha)
  ```

  检验样本是否来自正态分布

- Kolmogorov-Smirnov检验

  ```matlab
  [h,p]=kstest(x)
  [h,p]=kstest(x,'alpha',alpha)
  ```

  单样本的K检验法，检验样本是否符合标准正态分布

  ```matlab
  [h,p]=kstest2(x1,x2)
  [h,p]=kstest2(x1,x2,'alpha',alpha)
  ```

  双样本的K检验法，检验两个样本是否来自同一连续分布。

- Lilliefors检验

  ```matlab
  [h,p]=lillietest(x)
  [h,p]=lillietest(x,'alpha',alpha)
  ```

  检验样本是否来自正态分布

## 4.方差分析函数

- 单因素方差分析

  ```matlab
  [p,tbl,stats] = anova1(Y)
  [p,tbl,stats] = anova1(Y,group)
  anova1(Y,group,'off')
  ```

  group为组别向量，长度与y的列数相同，y中对应于group中相同的值的列向量（或值）是为同一水平的一部分。

  若没有group，默认y的每个列向量为单独的一个水平。

  p为拒绝原假设的最低显著性水平

  tbl为方差分析表

  stats为储存统计信息的结构体。

  'off'不弹出图表（默认弹出方差分析表）

- 双因素方差分析

  ```matlab
  [p,tbl,stats] = anova2(Y)
  [p,tbl,stats] = anova2(Y,reps)
  anova2(Y,reps,'off')
  ```

  reps为重复试验次数。y中的行数应为reps的整数倍，其比值为因素A的水平数。Y可以理解为reps个矩阵纵向拼接而成。每个矩阵表示一次试验的结果。此时可以探究有交互作用的双因素方差分析。

  若没有reps，默认实验次数为1，此时探究无交互作用的双因素方差分析。

## 5.回归分析函数

- ```matlab
  [b,bint,r,rint,stats]=regress(y,X)
  [___]=regress(y,X,alpha)
  ```

  y为响应数据，指定为$n\times1$数值矩阵。

  X为预测变量矩阵，指定为$n\times p$数值矩阵，每一列表示不同的预测变量。

  如果需要计算具有常数项的模型系数估计值，在矩阵X中加入一个由1组成成的列。y与X的行数必须相同。

  b为系数估计值，为$p\times1$向量。

  bint为系数估计值的置信边界下限和置信边界上限，为 $p\times2$ 矩阵，第一列为置信下界，第二列为置信上界。

  r为残差，为$n\times1$向量。

  rint为用于诊断离群值的区间，为$n\times2$矩阵。

  stats为模型统计量，包括$R^2$统计量，$F$统计量，$p$值。X必须包含一个由1组成的列，因为统计量的计算基于有常数项的模型假设。
  
- ```matlab
  stepwise(X,y)
  stepwise(X,y,inmodel,penter,premove)
  ```

  X为自变量矩阵，每个列表示一个自变量的所有取值

  y为因变量列向量，y的行数与X的行数相同。

  inmodel表示最初在模型中的自变量，默认为空。

  penter表示允许自变量进入模型的最大p值，即若模型外自变量的p值小于penter，则其具有显著性，penter可以理解为显著性水平alpha，默认为0.05。

  premove表示允许自变量保留在模型中的最大p值，即若模型内自变量的p值大于premove，则不具有显著性，默认为0.1。

## 6.histcounts——直方图计数

- ```matlab
  N=histcounts(___)
  [N,edges]=histcounts(___)
  [N,edges,bin]=histcounts(___)
  ```

  N为每个区间内的计数值

  edges为每个区间的边缘

  bin的大小与x相同，给出x中每个元素所在的计数区间
  
- ```matlab
  histcounts(x,nbins)
  ```

  nbins为等分区间数

- ```matlab
  histcounts(x,edges)
  ```

  edges=[x~1~,x~2~,...,x~n~]

  统计区间为[x~1~,x~2~),[x~2~,x~3~),...,[x~n-1~,x~n~]，所以N的长度比edges少1

- ```matlab
  histcounts(x,nbins,'normalization',value)
  % value in ['count','countdensity','cumcount','probability','pdf','cdf']
  ```

  'count'(default)：计数

  'countdensity'：单位宽度计数

  'cumcount'：累积计数

  'probability'：转换为相对概率

  'pdf'：概率密度函数的估计（单位宽度+相对概率）

  'cdf'：累计概率密度函数的估计

## 7.inpolygon——位于多边形区域内部或边缘上的点

- ```matlab
  in=inpolygon(xq,yq,xv,yv)
  [in,on]=inpolygon(xq,yq,xv,yv)
  ```

  in,on的大小与查询点xq,yq相同，其值为逻辑值：1(true)，0(false)。

  in(i)=1表示点i在多边形区域内或边缘上；on(i)=1表示点i在多边形边缘上。

- ```matlab
  xv=[x1,x2,...,xi,NaN,xi+1,...,xn]
  yv=[y1,y2,...,yi,NaN,yi+1,...,yn]
  ```

  用NaN将多个多边形进行区分。

- ```matlab
  numel(xq(in)) % 位于多边形区域内部或边缘上的点的个数
  plot(xq(in),yq(in),'.') % 绘制...
  plot(xq(in&~on),yq(in&~on),'.') % 绘制严格位于内部的点
  ```
