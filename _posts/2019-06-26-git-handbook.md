---
layout: post
title:  Git 简易使用手册
date:   2019-07-10 10:50:00
author: 
  - 李骞 <liqian6@xinhua.org>
  - 马艳彬 <mayanbin@xinhua.org>
categories: handbook
index: 0
---

## 安装

Git 提供了所有平台的二进制安装包，你可以按照下面的说明在你的开发环境上安装。

### Windows

使用下面提供的安装包进行安装

[32位版]({{ site.baseurl }}/uploads/softwares/Git-2.22.0-32-bit.exe) &middot; [64位版]({{ site.baseurl }}/uploads/softwares/Git-2.22.0-64-bit.exe)

### Linux

可以直接用系统提供的包管理工具进行安装

在 CentOS / RedHat / Fedora 类 Linux 上用 yum 安装：

```sh
$ yum install git
```

在 Ubuntu 等类 Debian 系统上，可以用 apt-get 安装：

```sh
$ apt-get install git
```

通过源代码安装（[点击下载源代码包]({{ site.baseurl }}/uploads/softwares/git-2.24.1.tar.gz)）：

```sh
$ tar -zxf git-2.24.1.tar.gz
$ cd git-2.24.1
$ make configure
$ ./configure --prefix=/usr
$ make all doc info
$ sudo make install install-doc install-html install-info
```

### macOS

macOS 上可以通过其包管理器 homebrew 进行安装。首先使用下面命令来安装 homebrew 工具：

```sh
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

然后，通过 homebrew 来安装：

```sh
$ brew install git
```

## 创建新仓库

创建新文件夹并打开，然后执行

```sh
$ git init
```

以创建新的 Git 仓库。

## 检出仓库

执行如下命令可以在你的本地开发环境上创建一个仓库的克隆版本：

```sh
$ git clone https://gitlab.xinhua.dev/path/to/repository
```

如果是在远端服务器上，你可以使用下面命令：

```sh
$ git clone git@gitlab.xinhua.dev:/path/to/repository
```

## 工作流

你的本地仓库由 Git 维护的三棵“树”组成。

第一个是你的工作目录，它持有实际文件；

第二个是缓存区（Index），它像个缓存区域，临时保存你的改动；

最后是 HEAD，指向你最近一次提交后的结果。

![工作流]({{ site.baseurl }}/uploads/images/git-trees.png)

## 添加与提交

你可以计划改动（把它们添加到缓存区），使用如下命令：

```sh
$ git add <filename>
$ git add *
```

这是 Git 基本工作流程的第一步；使用如下命令以实际提交改动：

```sh
$ git commit -m "initial commit"
```

现在，你的改动已经提交到了 HEAD，但是还没到你的远端仓库。

## 推送改动

你的改动现在已经在本地仓库的 HEAD 中了。执行如下命令以将这些改动提交到远端仓库，`<shortname>` 为远程仓库的简称，一般使用 `origin`：

```sh
$ git push <shortname> master
```

可以把 `master` 换成你想要推送的任何远程分支。 

如果你还没有克隆现有仓库，并欲将你的仓库连接到某个远程服务器，你可以使用如下命令添加：

```sh
$ git remote add <shortname> <server>
```

如此你就能够将你的改动推送到所添加的服务器上去了，通过 `-u` 参数设置本地当前分支的上游分支（upstream）：

```sh
$ git push -u <shortname> master
```

在设置完上游分支后，如果不写远程仓库名，则默认推送至 `origin` 仓库：

```sh
$ git push
```

## 分支

Git 鼓励频繁地使用分支来进行开发。在你创建或克隆仓库的时候，git 会创建一个名字叫 `master` 的默认分支。在其他分支上进行开发，完成后再将它们通过 Merge Request 合并到主分支上。

![分支]({{ site.baseurl }}/uploads/images/git-branches.png)

例如，创建一个叫做 `dev` 的分支，并切换过去：

```sh
$ git checkout -b dev
```

进行开发，之后将分支推送到远端仓库：

```sh
$ git push origin dev
```

最后在 GitLab 页面中开启新的 Merge Request 请求将 `dev` 分支合并到 `master` 分支。


## 更新与合并

要更新你的本地仓库至最新改动，执行：

```sh
$ git pull
```

以在你的工作目录中 获取（fetch） 并合并（merge）远端的改动。

要合并其他分支到你的当前分支（例如 `dev`），执行：

```sh
$ git merge <branch>
```

正常情况下，Git 都会尝试去自动合并改动。但是，自动合并并非次次都能成功，并可能导致冲突（conflicts）。 这时候就需要你修改这些文件来人肉合并这些冲突（conflicts）。改完之后，你需要执行如下命令以将它们标记为合并成功：

```sh
$ git add <filename>
```

在合并改动之前，也可以使用如下命令查看：

```sh
$ git diff <source_branch> <target_branch>
```

## 标签

在软件发布时创建标签，是被推荐的实践。这是个既有概念，在 SVN 中也有。可以执行如下命令以创建一个叫做 1.0.0 的标签：

```sh
$ git tag 1.0.0 1b2e1d63ff
```

1b2e1d63ff 是你想要标记的提交 ID 的前 10 位字符。使用如下命令获取提交 ID：

```sh
$ git log
```

你也可以用该提交 ID 的少一些的前几位，只要它是唯一的即可。

你还可以不写 ID，这样默认会使用当前工作分支最新的提交ID：

```sh
$ git tag 1.0.0
```

默认情况下，`git push` 并不会把标签推送到远端服务器上，只有通过显式命令才能推送标签到远端仓库。其命令格式如同推送分支：

```sh
$ git push origin --tags
```


## 替换本地改动

假如你做错事（自然，这是不可能的），你可以使用如下命令替换掉本地改动：

```sh
$ git checkout -- <filename>
```

此命令会使用 HEAD 中的最新内容替换掉你的工作目录中的文件。已添加到缓存区的改动，以及新文件，都不受影响。

假如你想要丢弃你所有的本地改动与提交，可以到服务器上获取最新的版本并将你本地主分支指向到它：

```sh
$ git fetch origin
$ git reset --hard origin/master
```

## 忽略特殊文件

Git 为我们提供了 .gitignore 文件，只要在这个文件中申明哪些文件你不希望添加到 Git 中去，这样当你使用 `git add .` 的时候这些文件就会被自动忽略掉。当然，.gitignore 文件本身要放到代码仓库里。

不需要从头写 .gitignore 文件，GitLab 已经为我们准备了各种配置文件，只需要组合一下就可以使用了。在 GitLab 仓库界面中新建文件，选择 .gitignore 类型的 template，再选择合适的语言就可以了。

对于需要忽略哪些文件，一般有如下几个原则：

1. 忽略操作系统自动生成的文件，比如缩略图、系统隐藏文件等；
2. 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如 Java 编译产生的 .class 文件；
3. 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

.gitignore 配置格式需要注意如下几点：

1. 所有空行或者以注释符号 # 开头的行都会被 Git 忽略。
2. 可以使用标准的 glob 模式匹配(所谓的 glob 模式是指 shell 所使用的简化了的正则表达式)。
3. 匹配模式最后跟反斜杠(/)说明要忽略的是目录。
4. 要忽略指定模式以外的文件或目录,可以在模式前加上惊叹号(!)取反。


## 常用命令列表

以下为 Git 常用命令列表，供日常使用参考：

```sh
$ git init                                                  # 初始化本地 git 仓库（创建新仓库）
$ git config --global user.name 王小虎                       # 配置用户名
$ git config --global user.email wangxiaohu@xinhua.org      # 配置邮件
$ git clone git@gitlab.xinhua.dev:/path/to/repository       # clone 远程仓库
$ git status                                                # 查看当前版本状态（是否修改）
$ git add foo                                               # 添加 foo 文件至 index
$ git add .                                                 # 增加当前子目录下所有更改过的文件至 index
$ git commit -m 'initial commit'                            # 提交
$ git commit --amend -m 'initial commit'                    # 合并上一次提交（用于反复修改）
$ git commit -am 'initial commit'                           # 将 add 和 commit 合为一步
$ git rm foo                                                # 删除 index 中的文件
$ git log                                                   # 显示提交日志
$ git log -1                                                # 显示 1 行日志 -n 为 n 行
$ git log -5
$ git log --stat                                            # 显示提交日志及相关变动文件
$ git log -p -m
$ git show dfb02e6e4f2f7b573337763e5c0013802e392818         # 显示某个提交的详细内容
$ git show dfb02                                            # 可只用 commit id 的前几位
$ git show HEAD                                             # 显示 HEAD 提交日志
$ git show HEAD^                                            # 显示 HEAD 的父（上一个版本）的提交日志 ^^ 为上两个版本 ^5 为上 5 个版本
$ git tag                                                   # 显示已存在的 tag
$ git tag -a 2.0.0 -m 'xxx'                                 # 增加 2.0.0 的 tag
$ git show 2.0.0                                            # 显示 2.0.0 的日志及详细内容
$ git log 2.0.0                                             # 显示 2.0.0 的日志
$ git diff                                                  # 显示所有未添加至 index 的变更
$ git diff --cached                                         # 显示所有已添加 index 但还未 commit 的变更
$ git diff HEAD^                                            # 比较与上一个版本的差异
$ git diff HEAD -- ./lib                                    # 比较与 HEAD 版本 lib 目录的差异
$ git diff origin/master..master                            # 比较远程分支 master 上有本地分支 master 上没有的
$ git diff origin/master..master --stat                     # 只显示差异的文件，不显示具体内容
$ git remote add origin https://gitlab.xinhua.dev/path/to/repository
$ git branch                                                # 显示本地分支
$ git branch --contains 50089                               # 显示包含提交 50089 的分支
$ git branch -a                                             # 显示所有分支
$ git branch -r                                             # 显示所有原创分支
$ git branch --merged                                       # 显示所有已合并到当前分支的分支
$ git branch --no-merged                                    # 显示所有未合并到当前分支的分支
$ git branch -m master master_copy                          # 本地分支改名
$ git checkout -b master_copy                               # 从当前分支创建新分支 master_copy 并检出
$ git checkout -b master master_copy                        # 上面的完整版
$ git checkout features/performance                         # 检出已存在的 features/performance 分支
$ git checkout --track hotfixes/BJVEP933                    # 检出远程分支 hotfixes/BJVEP933 并创建本地跟踪分支
$ git checkout 2.0.0                                        # 检出版本 2.0.0
$ git checkout -b dev origin/develop                        # 从远程分支 develop 创建新本地分支 dev 并检出
$ git checkout -- README                                    # 检出 HEAD 版本的 README 文件（可用于修改错误回退）
$ git merge origin/master                                   # 合并远程 master 分支至当前分支
$ git cherry-pick ff44785404a8e                             # 合并提交 ff44785404a8e 的修改
$ git push origin master                                    # 将当前分支 push 到远程 maste r分支
$ git push origin :hotfixes/BJVEP933                        # 删除远程仓库的 hotfixes/BJVEP933 分支
$ git push --tags                                           # 把所有 tag 推送到远程仓库
$ git fetch                                                 # 获取所有远程分支（不更新本地分支，另需 merge）
$ git fetch --prune                                         # 获取所有原创分支并清除服务器上已删掉的分支
$ git pull origin master                                    # 获取远程分支 master 并 merge 到当前分支
$ git mv README README.zh                                   # 重命名文件 README 为 README.zh
$ git reset --hard HEAD                                     # 将当前版本重置为 HEAD（通常用于 merge 失败回退）
$ git rebase
$ git branch -d hotfixes/BJVEP933                           # 删除分支 hotfixes/BJVEP933（本分支修改已合并到其他分支）
$ git branch -D hotfixes/BJVEP933                           # 强制删除分支 hotfixes/BJVEP933
$ git ls-files                                              # 列出 git index 包含的文件
$ git show-branch                                           # 图示当前分支历史
$ git show-branch --all                                     # 图示所有分支历史
$ git whatchanged                                           # 显示提交历史对应的文件修改
$ git revert dfb02e6e4f2f7b573337763e5c0013802e392818       # 撤销提交 dfb02e6e4f2f7b573337763e5c0013802e392818
$ git ls-tree HEAD                                          # 内部命令：显示某个 git 对象
$ git rev-parse v2.0                                        # 内部命令：显示某个 ref 对于的 SHA1 HASH
$ git reflog                                                # 显示所有提交，包括孤立节点
$ git show HEAD@{5}
$ git show master@{yesterday}                               # 显示 master 分支昨天的状态
$ git log --pretty=format:'%h %s' --graph                   # 图示提交日志
$ git show HEAD~3
$ git show -s --pretty=raw 2be7fcb476
$ git stash                                                 # 暂存当前修改，将所有至为HEAD状态
$ git stash list                                            # 查看所有暂存
$ git stash show -p stash@{0}                               # 参考第一次暂存
$ git stash apply stash@{0}                                 # 应用第一次暂存
$ git grep "delete from"                                    # 文件中搜索文本 delete from 字符串
$ git gc
$ git fsck
```