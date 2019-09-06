---
layout: post
title:  如何给项目成员设置 GitLab 权限
date:   2019-08-27 10:50:00
author: 
  - 马艳彬 <mayanbin@xinhua.org>
categories: faq
index: 0
---

当项目组申请到一个 GitLab 群组后，平台会指定至少一人作为该群组的所有者 Owner。此人负责该群组日常的人员管理。

建议将开发者添加到具体的 Project 中，这是因为，**如果将开发者添加到群组中的话，他将默认拥有该群组下所有 Project 的权限**。

对于项目中的核心开发人员，我们建议将其权限设置为 Maintainer。在 Project 中，Maintainer 具有 Developer 的所有权限，以及可以操作受保护分支、添加或移除项目成员、管理 Runner 等。

对于项目中的一般开发人员，我们建议将其权限设置为 Developer。在 Project 中，Developer 可以创建新的分支、拉取和推送代码到非保护分支、创建 Merge Request 等。

如果你想了解更多关于 GitLab 权限的介绍，可以 [查看这里](https://gitlab.xinhua.dev/help/user/permissions)。
