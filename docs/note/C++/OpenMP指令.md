# OpenMP指令

[OpenMPRefCard](OpenMPRefCard.pdf)

## 编译使用

```bash
g++ ... -fopenmp
```

## 是否使用OpenMP

```c++
#if _OPENMP

#else

#endif
```

## 并行模块

```c++
#pragma omp parallel num_threads(8)
{
    omp_set_num_threads(8); //设置线程数，优先级低于从句中的num_threads(8)
    int tid = omp_get_thread_num(); //获得线程编号
    int num_threads = omp_get_num_threads(); //获得并行区运行的线程数
    double clock = omp_get_wtime(); //获得openmp wall clock时间（秒）
    double wtick = omp_get_wtick(); //获得wtime的时间精度
}
#pragma omp <directive name> <clause>
```

## parallel

所有从句都可以连续使用

```c++
#pragma omp parallel <clause>
# if(expression) //expression为真则并行
# num_threads(num) //设置线程数，优先级低于if从句
# default(shared|none) //默认共享变量
# shared(args) //指定共享变量，默认为共享变量
# private(args) //为每个线程创建一个私有变量，需要初始化（临时变量）
# firstprivate(args) //同private，但是从主程序中初始化
```

## for/parallel for

对for循环的三个表达式有限制，参考官方手册

```c++
#pragma omp parallel num_threads(8)
{
#pragma omp for 
    for (int i = 0; i < n; i++)
    {
        
    }
}
#pragma omp <directive name> <clause>

# nowait //由于for结束时带有隐式同步，使用nowait取消
# lastprivate(args) //同private，将执行最后一个循环的线程的私有数据赋值给主线程变量
# collapse(n) //展开n重循环
# ordered //声明后续具有潜在的顺序执行部分，与下一句配合使用
# pragma omp ordered //for中，在critical的基础上顺序执行
# schedule(type[,chunk]) //控制调度方式（循环数n，线程数p）
    # static //每个线程n/p个
    # dynamic //每个线程1个，动态调度
    # guided //自定义chunk的dynamic
    # auto
    # runtime //由系统环境变量决定
# reduction(identifier:args) //将args作为私有变量计算，并在最后计算所有结果后返回
//例
#reduction(+:tot) //返回所有线程tot结果之和
# +,*，&，|，^,&&,||,max,min
```

## sections

同步构造，每个section分配一个线程

```c++
#pragma omp sections
{
#pragma omp section
    code1()
#pragma omp section
    code2()
}
```

## 其他

```c++
#pragma omp barrier //等待最慢的线程（同步）
#pragma omp single //某段代码单线程执行，带隐式同步（使用nowait取消）
#pragma omp master //指定主线程执行，无隐式同步
#pragma omp critical //某段代码互斥执行
#pragma omp atomic //原子操作
```

## 注意false sharing

多个线程避免读取同一个缓存行
