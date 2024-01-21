---
title: 如何开启Blog插件
description: 第一个Blog
date: 2024-01-21
authors:
  - sj
categories:
  - Material for MkDocs
---

Blog是material for mkdocs中的一个内置插件。

<!-- more -->

## 设置`mkdocs.yml`

```yaml
plugins:
  - blog #会自动生成docs/blog/
nav:
  - 博客:
    - blog/index.md
```

## 发布Blog

直接在`blog/posts/`中撰写markdown文件。

- 文件元数据设置

  ```yaml
  title: 如何开启Blog插件
  description: 第一个Blog
  date: 2024-01-21
  authors:
    - sj
  categories:
    - Material for MkDocs
  ```

- 添加摘录

  使用`<!-- more -->`标记，上方的内容会在博客主页显示。

- 添加作者

  在`blog/`目录下新建文件`.authors.yml`

  ```yaml
  authors:
    sj:
      name: ShiJin
      description: website owner
      avatar: https://github.com/sj-shijin.png # 设置为在线图片。如果为本地图片，index界面和内容界面相对路径不同，会出现找不到图片的情况。
  ```
