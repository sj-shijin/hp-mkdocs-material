---
  title: CP_2012_GLUCOSE Restart
  description: GLUCOSE求解器中的重启策略
  date: 2024-04-04
  authors:
    - sj
  categories:
    - SAT问题
---

SAT问题是一个经典的NP完全问题。许多其他领域的问题都可以转化为SAT问题，并利用SAT求解器进行求解。搜索重启是现代SAT求解器的关键部分之一。一个优秀的重启策略可以提高现代SAT求解器的效率。作者将现代SAT求解器看作“子句生成器”，并使用文字块距离(LBD)对子句质量进行衡量。作者使用全局平均和局部平均的LBD作为动态评估子句质量的方法，并根据两者之间的差距，判断是否进行重启。针对该重启策略的实验表明：该重启策略能显著提高SAT问题中不可满足实例的判定效率，但对可满足实例没有显著的效率提升。作者又提出，当本次搜索中已赋值的变量数量显著多于之前搜索的平均数量时，对重启操作进行阻塞，可以帮助可满足实例的判定。我认为本文提出的重启策略和阻塞策略想法简明、实现有效，有助于后续SAT求解器的设计。

[:fontawesome-solid-file-pdf: 原论文](../assets/CP_2012_GLUCOSE%20Restart/Refining%20restarts%20strategies%20for%20SAT%20and%20UNSAT.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/CP_2012_GLUCOSE%20Restart/CP_2012_GLUCOSE%20Restart.html){.md-button}

<!-- more -->