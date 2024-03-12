---
  title: SPAA_2021_Parallel Shortest Paths
  description: 并行单源最短路算法
  date: 2024-01-16
  authors:
    - sj
  categories:
    - 并行算法
    - 图算法
---

单源最短路（SSSP）问题是图论中的经典问题，对其理论与实现的研究都具有重大意义。目前，大部分并行SSSP算法基于Δ-Stepping，即以Δ为步长进行Dijkstra算法，并在子过程中进行Bellman-Ford算法。然而，超参数Δ的选择与图的结构、权重分布及具体实现相关，而且对性能的影响极大。在本文中，作者提出了惰性批量优先队列（LAB-PQ），并基于现有的并行SSSP算法，构建了新的Stepping算法框架，实现了超参数不敏感的并行SSSP算法。新算法在理论上具有较低复杂度，实现后在多种不同的负载下均表现出较高的性能。

[:fontawesome-solid-file-pdf: 原论文](../assets/SPAA_2021_Parallel%20Shortest%20Paths/SPAA_2021_Parallel%20Shortest%20Paths.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/SPAA_2021_Parallel%20Shortest%20Paths/SPAA_2021_Parallel%20Shortest%20Paths_marp.html){.md-button}

<!-- more -->
