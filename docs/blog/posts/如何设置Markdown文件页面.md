---
title: 如何设置Markdown文件页面
description: markdown中嵌入的html组件（类似bootstrap）
date: 2024-01-22
authors:
  - sj
categories:
  - Material for MkDocs
---

包括对markdown中的yaml属性（front matter）进行设置，以及嵌入式的html组件。详细信息见[mkdocs-material-reference](https://squidfunk.github.io/mkdocs-material/reference/)

<!-- more -->

## front matter设置

front matter是在每个markdown文件开头使用`---`包围的符合yaml语法的模块。

```yaml
title: h1 title # 用于侧边栏导航，社交卡片等
description: brief intro # 用于页面标签描述，社交卡片等
status: new # 在导航栏的右侧显示页面状态的图标，已定义new和deprecated
template: custom.html # 使用特定的页面模板
```

### 设置页面状态

需要额外在`mkdocs.yml`中设置，可以为页面状态添加说明：

```yaml
extra:
  status:
    new: Recently added
```

还可以[自定义页面状态](https://mkdocs-material.github.io/examples/page-status/)。

## 提示

提示是带有颜色的强调型文本。需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

基础用法如下：

```markdown
!!! note "自定义提示标题"

    空一行，缩进四个空格为提示内容

??? note "默认折叠的提示"

???+ note "默认展开的可折叠提示"

!!! note inline "靠左显示提示"

!!! note inline end "靠右显示提示"
```

默认支持提示类型：

- note
- abstract
- info
- tip
- success
- question
- warning
- failure
- danger
- bug
- example
- quote

## 注释

注释是一个可以嵌套定义的一个小标记，点击可以弹出一个小窗口。需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - attr_list
  - md_in_html
  - pymdownx.superfences
```

基础用法如下，注释标记会添加在（1）的位置：

```markdown
Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! (1)
    { .annotate }

    1.  :woman_raising_hand: I'm an annotation as well!
```

## 按钮

按钮是一个可悬停激活，可执行链接或js脚本的块。需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - attr_list
```

基础用法如下：

```markdown
[Subscribe to our newsletter](#){ .md-button }

[Subscribe to our newsletter][Demo]{ .md-button }

  [primary color]: ../setup/changing-the-colors.md#primary-color
  [accent color]: ../setup/changing-the-colors.md#accent-color 
  [Demo]: javascript:alert$.next("Demo")
```

## 代码块

需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
```

代码复制按钮，在代码块中启用[注释](# 注释)：

```yaml
theme:
  features:
    - content.code.copy
    - content.code.annotate
```

添加代码标题、代码行号、突出显示行：

````markdown
```py title="标题" linenums="1" hl_lines="2 3"
import numpy
import pandas
import matplotlib
```
````

行内代码块语法高亮，`#!python range()`：

```markdown
显示python语法：`#!python range()`
```

## 内容选项卡

内容选项卡可以在同一位置切换内容，需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tabbed:
      slugify: !!python/object/apply:pymdownx.slugs.slugify
        kwds:
          case: lower
```

设置整个文档的所有内容选项卡同时切换：

```yaml
theme:
  features:
    - content.tabs.link
```

基础用法如下：

```markdown
=== "第一个内容"

    第一部分的内容，任何markdown文本

=== "第二个内容"

    第二部分的内容，任何markdown文本
```

## 数据表

默认启用，在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - tables
```

可排序的表格，需要在`docs/javascripts/tablesort.js`和`mkdocs.yml`中设置：

``` js
document$.subscribe(function() {
    var tables = document.querySelectorAll("article table:not([class])")
    tables.forEach(function(table) {
    new Tablesort(table)
    })
})
```

``` yaml
extra_javascript:
    - https://unpkg.com/tablesort@5.3.0/dist/tablesort.min.js
    - javascripts/tablesort.js
```

从文件导入表[插件](https://timvink.github.io/mkdocs-table-reader-plugin/)

## mermaid图

需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
```

## 脚注

需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - footnotes
```

基础用法：

```markdown
第一个脚注[^1]，第二个脚注[^2]。
[^1]: 直接在同一行进行脚注
[^2]:
    换行后空四格进行脚注
```

## 文字格式

需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - pymdownx.critic # 批注 {--删除线--} {++下划添加线++} {~~删除线~>添加线~~} {==高亮==} {>>评价<<}
  - pymdownx.caret # 上箭头 ^上标^ ^^下划线^^
  - pymdownx.tilde # 波浪线 ~下标~ ~~删除线~~
  - pymdownx.mark # 文本高亮 ==高亮==
  - pymdownx.keys # 渲染键盘按键 ++按键1+按键2+按键3++
```

## 网格

需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions: 
  - attr_list
  - md_in_html
```

网格卡片，悬停时有悬浮效果，使用列表语法：

```markdown
<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

```markdown
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>
```

块语法：

```markdown
<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

通用网格：

````markdown
<div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>
````

## 图标和标签

需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - attr_list
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
```

## 图像

需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - attr_list
  - md_in_html
```

可以提供对齐，明暗模式改变图片，图像标题（HTML）等功能。

图像自动缩放插件[glightbox](https://github.com/blueswen/mkdocs-glightbox)：

```shell
pip install mkdocs-glightbox
```

```yaml
plugins:
  - glightbox
```

## 列表

无序列表和有序列表默认支持，需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - def_list # 定义列表
  - pymdownx.tasklist:
      custom_checkbox: true # 任务列表
```

定义列表可以枚举任意键值对的列表，基础用法如下：

```markdown
`Lorem ipsum dolor sit amet`

:   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
    tellus non sem sollicitudin, quis rutrum leo facilisis.

`Cras arcu libero`

:   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
    ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

    Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
    Nam vulputate tincidunt fringilla.
    Nullam dignissim ultrices urna non auctor.
```

## 数学公式

提供MathJax和KaTex两个库，设置有所区别[官方文档](https://squidfunk.github.io/mkdocs-material/reference/math/)。

## 工具提示

需要在`mkdocs.yml`中设置：

```yaml
markdown_extensions:
  - abbr
  - attr_list
  - pymdownx.snippets
theme:
  features:
    - content.tooltips
```

基础用法如下：

```markdown
[链接名](https://链接.com "悬停提示")

[链接名][链接引用]

  [链接引用]: https://链接.com "悬停提示"

:material-information-outline:{ title="其他元素使用属性列表添加悬停提示" } 
```

缩写和词汇表（[全局设置](https://squidfunk.github.io/mkdocs-material/reference/tooltips/#adding-a-glossary)）：

```markdown
The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
```
