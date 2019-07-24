---
layout: post
title:  如何将原有代码迁移到 GitLab
date:   2019-06-16 07:50:00
author:
  - 马艳彬 <mayanbin@xinhua.org>
categories: faq
index: 100
---

通过本指南，你可以了解到如何将原有代码迁移到平台的 GitLab 上。

## 准备工作

为了顺利进行迁移，你需要确认是否已经完成下列内容：

* 安装有 Git 的本地开发环境
* 提前在 GitLab 上创建一个空的项目仓库
* 如果你的 Git 存在历史提交，请参照这里 [重写 Git 历史]({{ site.baseurl }}/faq/rewrite-git-history.html)

## 从其他 Git 仓库进行迁移

在本地开发环境上执行下面命令，将所有分支与标签推送到新 Git 服务器上：

```bash
$ git remote set-url origin https://gitlab.xinhua.dev/foo/my-project.git
$ git push --set-upstream origin --all
$ git push --tags
```

## 从 Subversion 仓库进行迁移

我们使用 Git 官方提供的 SVN 衔接的工具来完成 SVN 到 GitLab 的代码迁移。

首先，我们需要使用 `authors.txt` 来映射 SVN 作者到 Git 作者的关系，其格式如下：

```csv
wangxiaohu = 王小虎 <wangxiaohu@xinhua.org>
lixiaoyao  = 李逍遥 <lixiaoyao@xinhua.org>
```

接着执行下面的命令从 SVN 服务器进行克隆：

```bash
$ git svn clone -s --authors-file=authors.txt https://ptah.to/svn my-project
```

以上命令会将 SVN 服务器上的代码拉取并保存到了本地的 `my-project` 目录。

最后一件要做的事情是，将你的新 Git 服务器添加为远程仓库并推送到上面。

```bash
$ git remote add origin https://gitlab.xinhua.dev/foo/my-project.git
$ git push --set-upstream origin --all
$ git push --tags
```
