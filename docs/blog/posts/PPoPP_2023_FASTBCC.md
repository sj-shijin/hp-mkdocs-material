---
  title: PPoPP_2023_FASTBCC
  description: 并行双连通分量计算
  date: 2024-01-29
  authors:
    - sj
  categories:
    - 并行算法
    - 图算法
---

双连通分量（BCC）的求解是图论中的基础问题，可以广泛应用于如平面性检验、中心性计算和网络分析等任务中。Hopcroft-Tarjan算法是串行求解BCC的经典算法，其时间复杂度$O(n+m)$与空间复杂度$O(n)$都在可接受的范围内，但由于其基于深度优先搜索（DFS）树框架，难以并行化。最初能够并行求解BCC的Tarjan-Vishkin算法可以基于任意生成树（AST）框架，但由于其使用了过多的额外空间$O(m)$，没有被广泛采用。后续算法采用广度优先搜索（BFS）树框架对Tarjan-Vishkin算法进行改进，将额外空间降低到$O(n)$，但由于BFS的特性，改进后的算法在直径较大的图中性能不佳。在该论文中，作者重新审视Hopcroft-Tarjan串行算法，提取出关键思想，结合了高效的并行单连通分量算法，实现了AST框架下使用$O(n)$额外空间的FAST-BCC算法。该算法流程简明，实现高效，在多种负载下均表现出较高的性能。

[:fontawesome-solid-file-pdf: 原论文](../assets/PPoPP_2023_FASTBCC/PPoPP_2023_FASTBCC.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/PPoPP_2023_FASTBCC/PPoPP_2023_FASTBCC_marp.html){.md-button}

<!-- more -->
