---
layout: post
title:  第一次上手使用
date:   2019-07-10 10:50:00
author: 
  - 马艳彬 <mayanbin@xinhua.org>
  - 李骞 <liqian6@xinhua.org>
categories: tutorial
index: 0
---

当你开通平台帐号后，请按下面的步骤进行相应的初始化配置。

## 修改平台密码

初次登录后，请尽快修改初始的平台密码，以确保帐号密码安全。

## 完善个人信息

你可以完善个人信息，比如上传一张独一无二的头像或编辑一段自我介绍。

## 首次使用 GitLab 前的配置

如果你是一名开发人员，还需要在使用 GitLab 前做如下配置。

### 设置用户信息

在你的本地开发环境上，请确保按如下的格式配置与你平台帐号一致的姓名和电子邮箱：

```sh
$ git config --global user.name 王小虎
$ git config --global user.email wangxiaohu@xinhua.org
```

### 设置 GitLab 操作密码

如果你想进行推送、拉取等 GitLab 操作，那么还需要设置 GitLab 的操作密码。请在 GitLab 的 Settings -> Password 页面中设置此密码。

<!-- 
## 阅读使用规范

为了规范平台使用，提高开发效率，保证开发质量，请在使用平台提供的功能前阅读 [新华开发平台使用规范](criterion-of-use.html)
 -->