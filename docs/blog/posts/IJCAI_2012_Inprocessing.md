---
  title: IJCAI_2012_Inprocessing
  description: 内处理规则
  date: 2024-03-28
  authors:
    - sj
  categories:
    - SAT问题
---

SAT问题是数学中的一个基础问题，而逻辑学、图论、计算机科学和运筹学等领域中的众多问题都可以转化为SAT问题。为了提高SAT求解器的性能，现代求解器往往会使用多种推理规则对子句进行化简。这些操作在求解过程前被称为预处理，在求解过程中被称为内处理。本文的作者认为混合使用多种化简技术可能存在求解过程不完整的问题，缺乏相关的理论支持。于是作者通过分析现有的技术，提取出其中的关键步骤，绘制出化简技术之间的关系图。随后提出了一个内处理规则框架，并且证明只要遵循该框架就可以保证求解问题的完整性。作者还将被广泛认可的求解技术套用到框架中证明其合理性。我认为这个内处理框架能够为未来SAT求解器的设计提供指导性的帮助。

[:fontawesome-solid-file-pdf: 原论文](../assets/IJCAI_2012_Inprocessing/Inprocessing%20Rules.pdf){.md-button}
[:simple-slides: 幻灯片](../assets/IJCAI_2012_Inprocessing/IJCAI_2012_Inprocessing.html){.md-button}

<!-- more -->