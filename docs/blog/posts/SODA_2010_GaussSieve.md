---
  title: SODA_2010_GaussSieve
  description: 高斯筛
  date: 2024-10-07
  authors:
    - sj
  categories:
    - 格密码
---

格中最短向量问题（SVP）是格密码学中的核心难题。格密码中许多底层问题（NTRU，SIS，LWE）的密码学分析都可以归结为格中最短向量问题。SVP求解算法分为两类：枚举与筛选。筛选算法对大规模的向量集合进行内部组合，逐步降低向量集合的整体长度。AKS/NV筛在筛选之前就确定了向量集合的大小，对于筛选产生的重复向量无能为力。作者认为先前筛法效率较低的原因为：大量重复向量导致算法的空间和时间效率降低。于是作者先提出列表筛，从空列表开始添加经过筛选的质量较高的向量；再提出高斯筛，针对列表筛中存在的长向量进行更新。在理论层面，作者使用球体堆积理论通过SVP规模确定算法空间大小。我认为该论文在理论与实践层面都有价值，能够得到高质量的短向量集合，后续如果需要在空间受限的情况下进一步改进，可能需要与枚举算法结合。

[:fontawesome-solid-file-pdf: 原论文](../assets/SODA_2010_GaussSieve/Faster%20exponential%20time%20algorithms%20for%20the%20shortest%20vector%20problem.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/SODA_2010_GaussSieve/SODA_2010_GaussSieve.html){.md-button}

<!-- more -->