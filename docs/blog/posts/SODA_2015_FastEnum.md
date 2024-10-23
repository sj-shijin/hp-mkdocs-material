---
  title: SODA_2015_FastEnum
  description: 快速枚举格上最短向量
  date: 2024-09-30
  authors:
    - sj
  categories:
    - 格密码
---

格中最短向量问题（SVP）是格密码学中的核心难题。格密码中许多底层问题（NTRU，SIS，LWE）的密码学分析都可以归结为格中最短向量问题。SVP求解算法分为两类：枚举与筛选。枚举算法使用递归投影进行遍历；筛选算法对大规模的向量集合进行内部组合，逐步降低向量集合的整体长度。Kannan提出的理论枚举算法虽然具有较低的时间复杂度，但由于预处理过程过于耗时，没有被用于实际求解。作者对Kannan的算法进行了分析，采用了简化预处理过程，增加递归步长等多种方法，实现了时间复杂度较低且实际可行的枚举算法，表现优于现有的枚举算法和筛法。我认为论文中算法提升效率的核心是增加递归步长，虽然没有改进理论时间复杂度，但提升了实际求解效率，后续可以尝试使用BKZ算法以及剪枝进一步提升枚举算法的效率。

[:fontawesome-solid-file-pdf: 原论文](../assets/SODA_2015_FastEnum/Fast%20Lattice%20Point%20Enumeration%20with%20Minimal%20Overhead.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/SODA_2015_FastEnum/SODA_2015_FastEnum.html){.md-button}

<!-- more -->