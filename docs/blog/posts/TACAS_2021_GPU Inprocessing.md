---
  title: TACAS_2021_GPU Inprocessing
  description: GPU加速CDCL求解器的内处理过程
  date: 2024-03-21
  authors:
    - sj
  categories:
    - SAT问题
    - GPU算法
---

SAT问题是数学中的一个基础问题，而逻辑学、图论、计算机科学和运筹学等领域中的众多问题都可以转化为SAT问题。提高SAT求解器的性能，也就相当于提高了一大类问题的求解效率。在本论文中，作者希望通过GPU实现一个性能更高的SAT求解器，但GPU有限的存储空间成为了实现过程中的第一个阻碍。所以作者提出了一种并行回收垃圾存储空间的算法，相较于线性的垃圾回收算法具有极大的性能提升。作者还设计了一种在内处理过程中消除变量依赖的任务分配算法，使得内处理过程具有了一定的并行性。结合三阶段变量消去优化，并行内处理部分有平均1.8倍的性能提升。但是，可能由于该论文没有对CDCL SAT求解器的关键部分——冲突分析过程进行优化，导致GPU求解器对比CPU版本的整体提升并不大。

[:fontawesome-solid-file-pdf: 原论文](../assets/TACAS_2021_GPU%20Inprocessing/SAT%20Solving%20with%20GPU%20Accelerated%20Inprocessing.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/TACAS_2021_GPU%20Inprocessing/TACAS_2021_GPU%20Inprocessing.html){.md-button}

<!-- more -->