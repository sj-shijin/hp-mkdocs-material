---
  title: EUROCRYPT_2018_SubSieve
  description: 子格筛/Dimensions for Free
  date: 2024-09-23
  authors:
    - sj
  categories:
    - 格密码
---

格中最短向量问题（SVP）是格密码学中的核心难题。格密码中许多底层问题（NTRU，SIS，LWE）的密码学分析都可以归结为格中最短向量问题。SVP求解算法分为两类：枚举与筛选。枚举算法使用搜索与剪枝对全空间进行遍历；筛选算法对大量向量进行两两组合，保留新生成的短向量，逐步降低向量集合的整体长度。该论文对筛法进行改进，作者注意到筛法的结果中包含大量的短向量，如果只关注格中的最短向量，会导致其他的短向量结果被浪费。于是作者提出，在求解n维格的SVP时，只要对n-d维格进行筛法SVP求解，再使用代数方法将结果提升到n维。作者实现的新筛法相较于其他筛法速度提升10倍。我认为作者充分利用了现有结果中的信息，筛法的时间与空间复杂度均为指数级，在低维子格中进行筛法求解不仅可以缩短求解时间，而且可以降低存储空间的需求。

[:fontawesome-solid-file-pdf: 原论文](../assets/EUROCRYPT_2018_SubSieve/Shortest%20vector%20from%20lattice%20sieving%20a%20few%20dimensions%20for%20free.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/EUROCRYPT_2018_SubSieve/EUROCRYPT_2018_SubSieve.html){.md-button}

<!-- more -->