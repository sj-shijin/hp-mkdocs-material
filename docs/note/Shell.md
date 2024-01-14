# Shell

[MIT计算机教育中缺失的一棵](https://missing-semester-cn.github.io/)

## 基本shell指令

```shell
#***多用--help***
#***多用man <指令>***
#输出
echo
#查看命令路径
which echo
#查看当前目录
pwd
#更换当前目录
cd ..(父目录).(当前目录)/(根目录)~(主目录)-(之前的目录)
#展示目录下的文件，可加路径
ls
ls -l #详细信息
#重命名或移动文件
mv
#重命名并复制文件
cp
#删除，非递归
rm
rmdir
#新建文件夹
mkdir
#递归查找文件，可进行相应的操作
find <查找目录> -name "文件名" -type 文件类型 --exec 执行命令
#在文件中查找，
grep [sth] "文件名"
```

## 输入输出流

`<`：改变输入流

`>`：改变输出流（覆盖）

`>>`：改变输出流（追加）

`|`：管道，将左侧的输出作为右侧的输入

```shell
#输出到文件
echo hello > hello.txt
#读取文件并从标准输出流输出
cat hello.txt
#改变标准输入流，改变标准输出流，实现了复制
cat < hello.txt > hello2.txt
#输出ls的最后1行
ls -l | tail -n1
#接受输入流输出到文件的同时，也输出到标准输出流
tee
```

改变输出流时，进行写入操作的shell，如果shell没有root权限，即使使用了sudo执行了命令，输出的操作依然会被拒绝。

可以使用管道操作将sudo作用于可以写入的命令以修改被保护的文件。

## root权限

```shell
#一般可以使用sudo临时使用root权限
sudo
#改变到root用户，此时命令前的$会变为#
sudo su
exit
```

## 单引号与双引号

```shell
foo=bar // 声明变量
echo "value is $foo" // value is bar
echo 'value is $foo' // value is $foo
```

## 符号

```shell
mcd.sh
    mcd() {
        mkdir -p "$1"
        cd "$1"
    }
source mcd.sh
mcd test //创建了一个test文件夹并进入
```

- `$0`：正在运行的指令
- `$1`：第一个参数
- `$?`：上一条指令的错误代码
- `$_`：上一个参数
- `$#`：参数的数量
- `$$`：进程id
- `$@`：所有的参数，可以通过for进行调用
- `!!`：会被替换为上一条指令
- `{}`：展开，`abc.{jpg,png}`等于`abc.jpg abc.png`
- `<变量名>=$(指令名)`：在变量中保存输出，注意等号两端不能有空格
- glob符号详见Git.md

## 脚本编写

```shell
#检查脚本是否规范
shellcheck abc.sh
```

脚本与函数的区别：

1. 脚本运行在一个新的进程中，函数运行在当前进程中。
2. 脚本在每次被使用时加载，函数在定义时被加载，
3. 脚本不一定是shell语言，可以使用python或其他语言。

脚本的第一行称为shebang行，由`#!`开始，后面跟可执行文件的绝对路径，若如shebang行，则默认使用当前shell。

```shell
#建议使用第一种方法类似于在$PATH中运行可执行文件
#!/usr/bin/env python
#!/usr/local/bin/python
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
```

```shell
if [[ $1 = "--help" ]] || [[ $1 = "-h" ]]
then
    echo "这是一个测试demo"
    echo "这个脚本怎么使用，干嘛的，注意点巴拉巴拉"
    exit 0
fi
echo "脚本传入参数$1"
```
