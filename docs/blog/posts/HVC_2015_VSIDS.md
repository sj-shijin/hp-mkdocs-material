---
  title: HVC_2015_VSIDS
  description: SAT常用技巧VSIDS的图论解释
  date: 2024-01-10
  authors:
    - sj
  categories:
    - SAT问题
    - 图算法
---

现代SAT求解器中普遍使用VSIDS方法及其变种作为启发式搜索的方法之一，该论文对这个方法的合理性给出了解释，对SAT问题的启发式搜索策略的选择具有指导性的意义。VSIDS方法是优先选择在最近推断过的子句中，出现次数多的变量，在后续的变量枚举时优先枚举。由于子句代表了变量之间的相关性，作者使用图论中的社区结构和桥接变量进行解释。VSIDS高效的原因主要包括：挑选高中心性的桥接变量、倾向于从较小的社区中选择变量和倾向于从最近的社区中选择变量。作者对VSIDS的有效性分析较为完备，对该论文进一步思考，社区结构性强的SAT问题具有良好的可分性，可以通过这种可分性提高SAT问题的并行性。

[:fontawesome-solid-file-pdf: 原论文](../assets/HVC_2015_VSIDS/HVC_2015_VSIDS.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/HVC_2015_VSIDS/HVC_2015_VSIDS_marp.html){.md-button}

<!-- more -->
