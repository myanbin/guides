---
layout: post
title:  如何重写 Git 历史
date:   2019-09-04 10:50:00
author:
  - 马艳彬 <mayanbin@xinhua.org>
categories: faq
index: 101
---

开发平台的 GitLab 在服务器端对所有推送的提交进行了身份验证，对于未在平台登记的姓名及电子邮箱，会拒绝接受。因此，对于历史的 Git 项目，各项目组需要重写其 Git 历史。

本文将介绍如何使用脚本来重写 Git 历史，操作者需对 Git 及命令行有一定基础。

> 由于本文涉及的操作较为复杂，建议将原始代码进行备份后再进行以下操作。

## 准备工作

为了顺利进行重写，你需要确认是否已经完成下列内容：

* 安装有 Git 和 Python 3 的类 Linux 本地开发环境

## 保持本地仓库为最新最全

将待重写的代码仓库克隆到本地，并保证本地仓库中的所有分支和标签与远端保持一致，并且为最新版本。

```sh
$ git clone https://path.to/foo/my-project.git
$ cd my-project
$ git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
```

然后，删除远端配置：

```sh
$ git remote remove origin
```

## 统计原有提交

使用下面的命令可以统计出原有提交数及提交作者的基本信息：

```sh
$ git shortlog --email --numbered --summary --all
```

在项目根目录下创建 `authors.txt` 来映射新旧作者的基本信息：等号左侧为原有提交的电子邮箱，右侧为在平台上登记的姓名及电子邮箱。下面是一个实际样例：

```
myanbin@gmail.com = 马艳彬 <mayanbin@xinhua.org>
hexenq@gmail.com  = 李骞 <liqian6@xinhua.org>
```

你可以通过下面的命令快速生成该文件，并手动替换其中的 `登记姓名 <登记邮箱>`：

```sh
$ git shortlog --email --summary --all | sed 's/^.*<\(.*\)>.*$/\1\t=\t登记姓名 <登记邮箱>/' | sort | uniq > ./authors.txt
```

如果历史提交中的部分人员未在平台上登记，可以使用幽灵用户 `Ghost <ghost@xinhua.dev>` 代替。

## 生成脚本并执行重写操作

下载 `gencmd.py` 脚本到项目根目录下，并在终端中执行命令：

```sh
$ wget https://help.xinhua.dev/uploads/documents/gencmd.py
$ python ./gencmd.py
```

上述脚本会生成一段以 `git filter-branch` 开头的命令，请审查该命令并在终端中手动执行。根据仓库大小，该命令可能需要几分钟时间。

## 验证是否成功

使用下面的命令来验证重写操作是否成功执行：

```sh
$ git for-each-ref --format="%(refname)" refs/original/ | xargs -n 1 git update-ref -d
$ git shortlog --email --numbered --summary --all
```

## 将改写后的提交推送到服务端

```sh
$ git remote add origin https://gitlab.xinhua.dev/foo/my-project.git
$ git push --set-upstream origin --all
$ git push --tags
```

## 最后的清理

删除刚才使用过的 `authors.txt` 和 `gencmd.py` 文件。

<!--
[^1]: 如果想保留原始的历史提交者姓名，也可以使用 `Ghost (王小虎) <ghost@xinhua.dev>` 代替。
-->