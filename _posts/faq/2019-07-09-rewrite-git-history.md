---
layout: post
title:  如何重写 Git 历史
date:   2019-07-22 10:50:00
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

* 安装有 Git 和 Python 3 的本地开发环境
* 提前将待重写的代码仓库克隆到本地

## 保持本地仓库为最新最全

保证本地仓库中的分支和标签与远端保持一致，并且为最新版本。

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
myanbin@gmail = 马艳彬 <mayanbin@xinhua.org>
hexenq@gmail  = 李骞 <liqian6@xinhua.org>
```

## 生成脚本并执行重写操作

将 `gencmd.py`[^1] 复制到项目根目录下，并在终端中执行命令：

```sh
$ python ./gencmd.py
```

复制上述命令的输出结果，并在终端[^2]中执行。

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

[^1]: 点击此处[下载该文件](https://gitlab.xinhua.dev/xhd/guides/snippets/1/raw)
[^2]: 如果你的本地环境是 Windows，请使用 Powershell 执行。
