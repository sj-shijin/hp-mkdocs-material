# LaTeX 基础

编辑器：VSCode/Texworks

排版工具：Texlive

## 开始

```latex
\documentclass{article}
% 这里是导言区
\begin{document}
Hello, world!
\end{document}
```

以上为纯英文排版。

```latex
\documentclass[UTF8]{ctexart}
% 导言区
\begin{document}
你好，world!
\end{document}
```

以上为中英文混排。

## 标题、作者、日期

```latex
\documentclass[UTF8]{ctexart}
\title{你好，world!}
\author{shijin}
\date{\today}
\begin{document}
\maketitle % 在文档中将导言区定义的标题、作者、气体按照预定的格式展示
你好，world!
\end{document}
```

## 章节、段落、目录

```latex
\documentclass[UTF8]{ctexart}
\title{你好，world!}
\author{Liam}
\date{\today}
\begin{document}
\maketitle
\tableofcontents % 在标题、作者、日期后插入目录***生成正确的目录一般需要运行两次***
\newpage % 换页
%\chapter{} 一般用于书籍
\section{你好中国}
中国在 East Asia.\\ % 换行，不加则视为连续文本，或\newline
中国有34个省级行政区。
\subsection{Hello Beijing}
北京是 capital of China.

beijing %空一行为另起一段，或\par
\subsubsection{Hello Dongcheng District}
\paragraph{Tian'anmen Square}
is in the center of Beijing
\subparagraph{Chairman Mao}
is in the center of 天安门广场。
\subsection{Hello 山东}
\paragraph{山东大学} is one of the best university in 山东。
\end{document}
```

## 数学公式

具体见[LaTeX 数学符号公式](LaTeX 数学符号公式.md)

```latex
\usepackage{amsmath} % 加载支持数学环境的宏包
\begin{document}
Einstein 's $E=mc^2$. % 行内公式
$$ E=mc^2. $$ % 行间公式
\[E=mc^2. \] % 行间公式
\begin{equation}
E=mc^2.
\end{equation} % 带有编号的行间公式
\end{document}
```

公式引用：

```latex
\usepackage{hyperref}
\begin{equation} \label{eq1}
E=mc^2.
\end{equation} % 带有编号的行间公式

\autoref{eq1}
```

## 图片

```latex
\usepackage{graphicx} % 加载宏包
\begin{document}
\includegraphics{a.jpg}
\includegraphics[width = textwidth*.8]{a.jpg} % 等比例缩放至页面宽度的百分之八十
\end{document}
```

## 表格

```latex
\begin{tabular}{|l|c|r|}
 \hline
操作系统& 发行版& 编辑器\\
 \hline
Windows & MikTeX & TexMakerX \\
 \hline
Unix/Linux & teTeX & Kile \\
 \hline
Mac OS & MacTeX & TeXShop \\
 \hline
通用& TeX Live & TeXworks \\
 \hline
\end{tabular}
```

## 浮动体（调整图片和表格的位置）

```latex
\usepackage{graphicx} % 加载宏包
\begin{figure}[htbp] % 指定理想位置 htbp is here,top,bottom,float page
\centering % 居中
\includegraphics[width = 12cm]{a.jpg}
\caption{有图有真相} % 设置标题，会自动给加上编号
\label{pic1} % 设置标记，使用\ref{pic1}引用编号
\end{figure}

\begin{figure*} %跨栏图片
...
\end{figure*}
```

## 参考文献

```latex
\begin{thebibliography} {99} % 99代表引用的上限
\bibitem{lable1} Jin Shi...
\end{thebibliography}
```

引用：`\cite{lable1}`，lable1与文献标签对应。

## 参考文献（BibTeX）

`.tex`文件：

```latex
\bibliographystyle{unsrt}

\bibliography{xxx} % 与bib文件名对应
```

`xxx.bib`文件：

```latex
@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, {\L}ukasz and Polosukhin, Illia},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}
```

引用：`\cite{vaswani2017attention}`，与bib文件标签（第一个参数）对应

编译：使用带有BibTeX的编译链。

## 版面设置

- 页边距

  ```latex
  \usepackage{geometry}
  \geometry{papersize={20cm,15cm}}
  \geometry{left=1cm,right=2cm,top=3cm,bottom=4cm}
  %导言区
  ```

- 页眉页脚

  ```latex
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \lhead{shijin}
  \chead{\today}
  \rhead{158xxxxxxxx}
  \lfoot{}
  \cfoot{\thepage} % 页码
  \rfoot{}
  %导言区
  ```

- 首行缩进

  ```latex
  \usepackage{indentfirst}
  \setlength{\parindent}{2.45em} % 两个小四号中文字的长度
  %导言区
  ```

- 行间距

  ```latex
  \usepackage{setspace}
  \onehalfspacing % 1.5倍行间距
  %导言区
  ```

- 段间距

  ```latex
  \addtolength{\parskip}{.4em} %在原有的基础上增加段间距（负值减小）
  %导言区
  ```
  
- 参考文献右上角引用

  ```latex
  \newcommand{\upcite}[1]{\textsuperscript{\cite{#1}}}
  \upcite{}
  ```

  
