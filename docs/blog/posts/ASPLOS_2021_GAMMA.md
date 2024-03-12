---
  title: ASPLOS_2021_GAMMA
  description: 稀疏矩阵乘法
  date: 2024-03-07
  authors:
    - sj
  categories:
    - 稀疏矩阵乘法
---

稀疏矩阵乘法是计算机领域中的基础问题，是许多稀疏算法的核心，如稀疏深度神经网络，稀疏线性和张量代数，图分析等。通过提高运行速度或是降低所需的缓存空间，都可以提高稀疏矩阵乘法在cpu与gpu上的运行效率。该论文从优化访存的角度出发，利用Gustavson算法，使得稀疏矩阵乘法的数据流行平稳化，从而使得内存的访问局部连续化。作者还针对该访存模式设计了片上存储结构和对应的动态调度算法，相较于同类的硬件系统提高了性能并降低了片上储存空间。

[:fontawesome-solid-file-pdf: 原论文](../assets/ASPLOS_2021_GAMMA/ASPLOS_2021_GAMMA.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/ASPLOS_2021_GAMMA/ASPLOS_2021_GAMMA_marp.html){.md-button}

<!-- more -->