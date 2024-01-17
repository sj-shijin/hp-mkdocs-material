# C++STL算法库

编译时添加`-std=c++23`指令

## 带约束的算法（C++20）

命名空间std::ranges中包含各种算法，特点：可以直接用变量名，代表从begin到end进行算法。

```c++
#include <algorithm>
#include <vector>
#include <cstdint>

std::vector<std::uint64_t> v(10000);
std::ranges::sort(v);
```

**该命名空间中的函数似乎没有带execution的重载。**

所有带范围的函数都有ranges版本。

## STL并行执行（def in `<execution>`）

| 实例                      | 解释       | 版本    |
| ------------------------- | ---------- | ------- |
| std::execution::seq       | 单线程顺序 | C\+\+17 |
| std::execution::par       | 多线程顺序 | C\+\+17 |
| std::execution::par_unseq | 多线程无序 | C\+\+17 |
| std::execution::unseq     | 单线程无序 | C\+\+20 |

```c++
#include <algorithm>
#include <execution>
#include <vector>
#include <cstdint>

std::vector<std::uint64_t> v(10000);
std::sort(std::execution::par, v); //如函数能使用，将实例作为第一个参数
```

后续介绍算法时会指出能否使用execution。

## 不进行修改的序列操作（def in `<algorithm>`）

约定记号，[e,]代表可加execution指令，f(i)代表i个参数的函数。

| 函数（省略std::）                                            | 解释                                         | 版本    |
| ------------------------------------------------------------ | -------------------------------------------- | ------- |
| all_of([e,] begin, end, f(1)->bool)                          | -                                            | C\+\+11 |
| any_of([e,] begin, end, f(1)->bool)                          | -                                            | C\+\+11 |
| none_of([e,] begin, end, f(1)->bool)                         | -                                            | C\+\+11 |
| for_each([e,] begin, end, f(1))                              | -                                            |         |
| for_each_n([e,] begin, end, f(1))                            | 只进行n次的for_each                          | C\+\+17 |
| count([e,] begin, end, value)                                | -                                            |         |
| count_if([e,] begin, end, f(1)->bool)                        | -                                            |         |
| mismatch([e,] begin1, end1, begin2[, end2, f(2)->bool]) -> pair | 返回第一个不匹配的pair                       |         |
| find([e,] begin, end, value) -> iter                         | 第一个                                       |         |
| find_if([e,] begin, end, f(1)->bool) -> iter                 | 第一个                                       |         |
| find_if_not([e,] begin, end, f(1)->bool) -> iter             | 第一个                                       | C\+\+11 |
| find_first_of([e,] begin1, end1, begin2, end2[, f(2)->bool]) -> iter1 | 第一个序列中最先出现的第二个序列中的元素位置 |         |
| adjacent_find([e,] begin, end[, f(2)->bool]) -> iter         | 第一个相邻相等                               |         |
| search_n([e,] begin, end, count, value[, f(2)->bool]) -iter  | 序列中最先出现连续出现count个value的位置     |         |

注意：其中两个序列匹配函数`search`，`find_end`由于时间复杂度为n*m，未放在表中。

在`<functional>`中，存在可以作为search的参数的新匹配方法。

| 函数（省略std::）                                            | 解释                                                     | 版本    |
| ------------------------------------------------------------ | -------------------------------------------------------- | ------- |
| boyer_moore_searcher(begin, end[, hash(), f(2)->bool])       | 此为匹配串，要求：若f(a,b)\=\=true，则hash(a)\=\=hash(b) | C\+\+17 |
| boyer_moore_horspool_searcher(begin, end[, hash(), f(2)->bool]) | 此为匹配串，要求：若f(a,b)\=\=true，则hash(a)\=\=hash(b) | C\+\+17 |

```c++
#include <algorithm>
#include <functional>
#include <string>

std::string src = "12345654321";
std::string pat = "565";
auto it = std::search(src.begin(), src.end(), std::boyer_moore_horspool_searcher(pat.begin(), pat.end()));
```

## 进行修改的序列操作

| 函数（省略std::）                                            | 解释                                                         | 版本    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------- |
| copy([e,] begin1, end1, begin2)                              | 复制长度为两个序列的较小值                                   |         |
| copy_if([e,] begin1, end1, begin2, f(1)->bool)               | 复制为顺序，不是对应位置                                     | C\+\+11 |
| copy_n([e,] begin1, count, begin2)                           | 复制n个元素                                                  | C\+\+11 |
| copy_backward([e,] begin1, end1, end2)                       | 倒着复制，但顺序不变                                         |         |
| move([e,] begin1, end1, begin2)<br>move_backward([e,] begin1, end1, end2) | 与copy相同但进行move操作                                     | C\+\+11 |
| fill([e,] begin, end, value)<br>fill_n([e,] begin, count, value) |                                                              |         |
| transform([e,] begin1, end1, dst_begin, f(1))<br>transform([e,] begin1, end1, begin2, dst_begin, f(2)) -> iter | python中的map                                                |         |
| generate([e,] begin, end, f(0))<br>generate_n([e,] begin, count, f(0)) | 每次调用f生成一个数                                          |         |
| remove([e,] begin, end, value)<br>remove_if([e,] begin, end, f(1)->bool) | 删除，会改变位置，使用move                                   |         |
| remove_copy([e,] begin, end, dst_begin, value)<br>remove_copy_if([e,] begin, end, dst_begin, value) | 使用copy                                                     |         |
| replace([e,] begin, end, old_value, new_value)<br>replace_if([e,] begin, end, f(1)->bool, new_value) | 替换                                                         |         |
| replace_copy([e,] begin, end, dst_begin, old_value, new_value)<br>replace_copy_if([e,] begin, end, dst_begin, value, new_value) |                                                              |         |
| swap(&a, &b)<br>swap((&a)[N], (&b)[N])                       | 使用引用交换                                                 |         |
| swap_ranges([e,] begin1, end1, begin1)                       |                                                              |         |
| iter_swap(iter1, iter2)                                      | 使用指针交换                                                 |         |
| reverse([e,] begin, end)<br>reverse_copy([e,] begin, end, dst_begin) |                                                              |         |
| rotate([e,] begin, mid, end)<br>rotate_copy([e,] begin, mid, end, dst_begin) | 将[begin,mid)放置到[mid,end)后。                             |         |
| shift_left([e,] begin, end, n)<br>shift_right([e,] begin, end, n) | 超出范围时，如果为数字，会循环移动，如果为字符串或类实例，会置空 | C\+\+20 |
| shuffle(begin, end, g)                                       |                                                              | C\+\+11 |
| sample(begin, end, dst_begin, n, g)                          |                                                              | C\+\+17 |
| unique([e,] begin, end, f(2)->bool)<br>unique_copy([e,] begin, end, dst_begin, f(2)->bool) | 只会判断相邻的，多个相邻相同保留一个                         |         |

```c++
#include <algorithm>
#include <iterator>
#include <random>
#include <vector>

std::vector<int> v(10000);
std::random_device rd;
std::mt19937 g(rd()); // std::mt19937_64 g64(rd());
std::shuffle(v.begin(), v.end(), g);

std::vector<int> sv(100);
std::shuffle(v.begin(),v.end(),sv.begin(),100,g);
```

## 分割操作（def in `<algorithm>`）

| 函数（省略std::）                                            | 解释                                   | 版本    |
| ------------------------------------------------------------ | -------------------------------------- | ------- |
| is_partitioned([e,] begin, end, f(1)->bool)                  | 前部分为true，后部分为false            | C\+\+11 |
| partition([e,] begin, end, f(1)->bool) -> iter               | 分割，返回指向false的第一个            |         |
| partition([e,] begin, end, dst_begin_true, dst_begin_false, f(1)->bool) -> pair<iter,iter> | 结果分别放到两个序列中，返回两个迭代器 | C\+\+11 |
| stable_partition([e,] begin, end, f(1)->bool)                | 稳定的                                 |         |
| partition_point(begin, end, f(1)->bool) - iter               | 二分查找分割点                         | C\+\+11 |

## 排序操作（def in `<algorithm>`）

| 函数（省略std::）                                            | 解释                               | 版本    |
| ------------------------------------------------------------ | ---------------------------------- | ------- |
| is_sorted([e,] begin, end[, f(2)->bool])                     |                                    | C\+\+11 |
| is_sorted_until([e,] begin, end[, f(2)->bool]) -> iter       | 指向不满足的第一个                 | C\+\+11 |
| sort([e,] begin, end[, f(2)->bool])                          |                                    |         |
| partial_sort([e,] begin, mid, end[, f(2)->bool])             | 选择前mid-begin个最小/最大，并排序 |         |
| partial_sort_sopy([e,] begin, end, dst_begin, dst_end[, f(2)->bool]) | dst_end-dst_begin个                |         |
| stable_sort([e,] begin, end[, f(2)->bool])                   |                                    |         |
| nth_element([e,] first, nth, end[, f(2)->bool])              | 将第n大的数放到第n位               |         |

## 二分查找操作（def in `<algorithm>`）

| 函数（省略std::）                                            | 解释                         | 版本 |
| ------------------------------------------------------------ | ---------------------------- | ---- |
| lower_bound(begin, end, value[, f(2)->bool]) -> iter         | 默认小于，返回不满足的第一个 |      |
| upper_bound(begin, end, value[, f(2)->bool]) -> iter         | 默认小于，返回满足的最后一个 |      |
| binary_search(begin, end, value[, f(2)->bool])               | 查找相等                     |      |
| equal_range(begin, end, value[, f(2)->bool]) -> pair<iter, iter> | 返回相等的区间               |      |

## 有序序列的其他操作（def in `<algorithm>`）

| 函数（省略std::）                                            | 解释             | 版本 |
| ------------------------------------------------------------ | ---------------- | ---- |
| merge([e,] begin1, end1, begin2, end2, dst_begin[, f(2)->bool]) | 归并，各段不相交 |      |
| inplace_merge([e,] begin, mid, end[, f(2)->bool])            | 内部归并         |      |

## 有序序列的集合操作（def in `<algorithm>`）

| 函数（省略std::）                                            | 解释           | 版本 |
| ------------------------------------------------------------ | -------------- | ---- |
| includes([e,] begin1, end1, begin2, end2[,f(2)->bool]) ->bool | 集合2属于集合1 |      |
| set_difference([e,] begin1, end1, begin2, end2, dst_begin[, f(2)->bool]) | 集合1-集合2    |      |
| set_intersection([e,] begin1, end1, begin2, end2, dst_begin[, f(2)->bool]) | 交集           |      |
| symmetric_difference([e,] begin1, end1, begin2, end2, dst_begin[, f(2)->bool]) | 取不重复元素   |      |
| set_union([e,] begin1, end1, begin2, end2, dst_begin[, f(2)->bool]) | 取并集         |      |

## 堆操作（def in `<algorithm>`）

对于一个序列，堆的定义是：把序列看成二叉树，0是根节点，i的父亲是(i-1)/2，i的左子树为i\*2+1，i的右子树为i\*2+2，其中父节点的值均大于/小于子节点。

| 函数（省略std::）                                   | 解释                                                         | 版本    |
| --------------------------------------------------- | ------------------------------------------------------------ | ------- |
| is_heap([e,] begin, end[, f(2)->bool])              |                                                              | C\+\+11 |
| is_heap_until([e,] begin, end[, f(2)->bool]) ->iter | 返回第一个不满足堆性质的                                     | C\+\+11 |
| make_heap(begin, end[, f(2)->bool])                 | 默认大根堆                                                   |         |
| push_heap(begin, end[, f(2)->bool])                 | 约定begin到end-1是堆，调整最后一个值。                       |         |
| pop_heap(begin, end[, f(2)->bool])                  | 约定原始是堆，将根节点移出堆，结果begin到end-1是堆，最后一个元素是原始的根节点。 |         |
| sort_heap(begin, end[, f(2)->bool])                 | 原始是堆，结果是顺序数组。                                   |         |

## 最大/最小操作（def in `<algorithm>`）

| 函数（省略std::）                                            | 解释                     | 版本    |
| ------------------------------------------------------------ | ------------------------ | ------- |
| max(&a, &b[, f(2)->bool])                                    | 正确返回后者             |         |
| max_element([e,] begin, end[, f(2)->bool]) -> iter           |                          |         |
| min(&a, &b[, f(2)->bool])                                    | 正确返回前者             |         |
| min_element([e,] begin, end[, f(2)->bool]) -> iter           |                          |         |
| minmax(&a, &b) -> pair<&min,&max>                            |                          | C\+\+11 |
| minmax_element([e,] begin, end[, f(2)->bool]) -> pair<iter,iter> |                          | C\+\+11 |
| clamp(&value, &lo, &hi[, f(2)->bool])                        | 将val限制在[lo,hi]范围中 | C\+\+17 |

## 比较操作（def in `<algorithm>`）

| 函数（省略std::）                                            | 解释               | 版本    |
| ------------------------------------------------------------ | ------------------ | ------- |
| equal(&a, &b[, f(2)->bool])                                  |                    |         |
| lexicographical_compare([e,] begin1, end1, begin2, end2[, f(2)->bool]) | 字典序比较（小于） |         |
| lexicographical_compare_three_way(begin1, end1, begin2, end2[, f(2)]) | 三路比较运算符     | C\+\+20 |

三路比较简单介绍：

在C\+\+20中，比较运算符只有==和<=>（三路比较运算符）

使用方法，`(a<=>b)<0 => a<b`，`(a<=>b)==0 => a==b`，`(a<=>b)>0 => a>b`

返回值等在utility库中详细介绍

## 排列操作（def in `<algorithm>`）

| 函数（省略std::）                                            | 解释                       | 版本    |
| ------------------------------------------------------------ | -------------------------- | ------- |
| is_permutation(begin1, end1, begin2[, f(2) -> bool])<br />is_permutation(begin1, end1, begin2, end2,[, f(2) -> bool]) | 验证是否为一个排列（置换） | C\+\+11 |
| next_permutation(begin, end[, f(2)->bool])                   | 升序到降序的下一个         |         |
| prev_permutation(begin, end[, f(2)->bool])                   | 降序到升序的下一个         |         |

## 数值操作（def in `<numeric>`）

| 函数（省略std::）                                            | 解释                                       | 版本    |
| ------------------------------------------------------------ | ------------------------------------------ | ------- |
| iota(begin, end, value)                                      | 按序赋值value++                            | C\+\+11 |
| accumulate(begin, end, value[, f(2)])                        | 累加，初值value                            |         |
| inner_product(begin1, end1, begin2, value[, f1(2), f2(2)])   | 相乘相加，f1对应相加操作，f2对应相乘操作   |         |
| adjacent_difference([e,] begin, end, dst_begin[, f(2)])      | 后减前，第一个不变                         |         |
| partial_sum(begin, end, dst_begin[, f(2)])                   | 前缀和                                     |         |
| reduce([e,] begin, end, value[, f(2)])                       | 乱序的，可并行的accumulate                 | C\+\+17 |
| exclusive_scan([e,] begin, end, dst_begin value[, f(2)])     | 可并行的partial_sum，不包含第i个数的前缀和 | C\+\+17 |
| inclusive_scan([e,] begin, end, dst_begin value[, f(2)])     | 可并行的partial_sum，包含第i个数的前缀和   | C\+\+17 |
| transform_reduce([e,] begin, end, value[, f1(2), f2(1)])<br />transform_reduce([e,] begin1, end1, begin1, value[, f1(2), f2(2)]) | 可并行的inner_product（可单序列）          | C\+\+17 |
| transform_exclusive_scan([e,] begin, end, dst_begin, value, f1(2), f2(1))<br />transform_inclusive_scan([e,] begin, end, dst_begin, value, f1(2), f2(1)) |                                            | C\+\+17 |

## 未初始化内存上的操作（def in `<memory>`）

暂不考虑使用
