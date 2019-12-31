---
layout: post
title:  推送代码时提示 Unauthorized name or email 错误怎么办
date:   2019-08-22 10:50:00
author:
  - 马艳彬 <mayanbin@xinhua.org>
categories: faq
index: 131
---


![推送代码报错]({{ site.baseurl }}/uploads/images/git-push-error.png)

为了保证任何一段代码可溯可查，开发平台的 GitLab 在服务器端对所有推送的提交进行了身份验证，对于未在平台登记的姓名及电子邮箱，会拒绝接受。你在向 GitLab 服务端推送代码时遇到  Unauthorized name or email 错误，即说明你提交时使用的姓名或电子邮箱有问题。

你可以按如下步骤进行修复。

查看本地的 Git 历史，如果只有最近一个提交是错误的，那么可以重新配置你的 Git 用户信息并改写本次提交：

```sh
$ git config --global user.name 王小虎
$ git config --global user.email wangxiaohu@xinhua.org
$ git commit --amend --reset-author
```

如果有多个提交均出错，那么请参考 [如何重写 Git 历史]({{ site.baseurl }}/article/rewrite-git-history.html) 来改写你的 Git 历史。
