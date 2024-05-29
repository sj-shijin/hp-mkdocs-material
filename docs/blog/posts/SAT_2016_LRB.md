---
  title: SAT_2016_LRB
  description: SAT求解器学习率分支启发算法
  date: 2024-05-30
  authors:
    - sj
  categories:
    - SAT问题
---

SAT问题是一个经典的NP完全问题。许多其他领域的问题都可以转化为SAT问题，并利用SAT求解器进行求解。分支启发是现代SAT求解器的关键部分之一。一个优秀的分支启发算法可以加速学习子句的生成，提高现代SAT求解器的效率。分支启发关注的问题是搜索过程中如何选择下一个进行赋值的变量。作者将该问题类比于强化学习领域的多臂赌博机问题，将变量赋值期间对生成学习子句的贡献率类比于多臂赌博机的收益。作者使用指数移动平均计算期望收益，同时结合步长和权重衰减技巧提高搜索的局部性，加入原因侧补偿项提高收益的完整性，最终提出学习率分支(LRB)启发算法。该算法相较于被广泛应用的经典分支启发算法VSIDS，具有显著的性能提升，而且计算开销较小，可以应用于后续的SAT求解器。

[:fontawesome-solid-file-pdf: 原论文](../assets/SAT_2016_LRB/Learning%20rate%20based%20branching%20heuristic%20for%20SAT%20solvers.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/SAT_2016_LRB/SAT_2016_LRB.html){.md-button}

<!-- more -->