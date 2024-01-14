# C++代码分析工具(sanitizers+valgrind)

## sanitizers

一般内置于编译器中，以下为编译选项：

```shell
-fsanitize=address #检测地址错误
-fsanitize=memory #检测内存错误
-fsanitize=leak #检测内存泄漏
-fsanitize=thread #检测线程竞争
-fsanitize=undifined #检测未定义行为

-fno-omit-frame-pointer #保留函数指针，便于回溯
```

## valgrind

```shell
apt install valgrind
```

a.out为编译文件，编译选项有-g

### memcheck

内存泄漏等内存问题

```shell
valgrind --tool=memcheck --log-file=memcheck.log --leak-check=yes  ./a.out
```

### cachegrind

缓存分析器

```shell
valgrind --tool=cachegrind ./a.out
callgrind_annotate cachegrind.out.pid | grep -v “???” > cachegrind.log
```

cachegrind.out.pid为cachegrind工具的输出文件，pid替换为真实值。

### callgrind

函数分析器

```shell
valgrind --tool=callgrind ./a.out
#线程分离
valgrind --tool=callgrind --separate-threads=yes ./out
callgrind_annotate callgrind.out.pid | grep -v “???” > callgrind.log
```

callgrind.out.pid为callgrind工具的输出文件，pid替换为真实值。

#### 使用gprof2dot/dot进行可视化

```shell
apt install graphviz # dot命令
```

```shell
valgrind --tool=callgrind --callgrind-out-file=callgrind.out ./a.out
```

```shell
python gprof2dot.py -f callgrind -n 0.5 -e 0.5 -s callgrind.out | dot -Tpng -o perf.png
```

### massif

内存分析器

```shell
valgrind --tool=massif ./a.out
```

可视化查看工具

```shell
sudo apt install massif-visualizer
massif-visualizer massif.out.pid
```

massif.out.pid为massif工具的输出文件，pid替换为真实值。

### Helgrind

多线程分析器（暂时未使用）

```shell
valgrind --tool=helgrind ./a.out
```
