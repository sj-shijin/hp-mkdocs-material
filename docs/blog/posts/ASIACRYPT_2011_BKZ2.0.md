---
  title: ASIACRYPT_2011_BKZ2.0
  description: BKZ2.0
  date: 2024-10-14
  authors:
    - sj
  categories:
    - 格密码
---

格基约化算法是格密码学中的核心算法，也是进行格分析的核心步骤。格基约化可以求解近似SVP，并帮助枚举和筛法求解精确SVP。BKZ算法是实践中最佳的格基约化算法，其思想为分块进行投影格上的精确枚举算法，求解SVP，并将结果作为正交基，经典的LLL算法可以看作块大小为2的BKZ算法。在研究中，作者发现对BKZ算法运行时间影响最大的是枚举子算法。作者使用深度剪枝、局部块预处理和优化枚举半径三种方法进行改进，并提出BKZ2.0算法，可以在高维格中进行块大小较大的BKZ格基约化。除此之外，作者提出了一种模拟BKZ算法预期结果与运行时间的算法，不仅可以帮助分析时间复杂度，而且可以改进格上困难问题的安全性估计。我认为作者对于算法优化的思路值得借鉴，而且模拟算法的提出有助于后续的算法设计。

[:fontawesome-solid-file-pdf: 原论文](../assets/ASIACRYPT_2011_BKZ2.0/BKZ%202.0:%20Better%20Lattice%20Security%20Estimates.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/ASIACRYPT_2011_BKZ2.0/ASIACRYPT_2011_BKZ2.0.html){.md-button}

<!-- more -->