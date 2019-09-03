---
layout: post
title:  第一次上手使用
date:   2019-08-14 10:50:00
author: 
  - 马艳彬 <mayanbin@xinhua.org>
categories: tutorial
index: 0
---

当你开通平台帐号后，请按下面的步骤进行相应的初始化配置。

## 修改平台密码

初次登录后，请尽快修改初始的平台密码，以确保帐号密码安全。修改密码时应该保证新密码至少为 10 位，且必须包括数字、大写字母和小写字母。

如果你忘记了平台密码，也可以通过注册时提供的邮箱找回。

## 确认及完善个人信息

登录平台后，请访问 [我的帐号](https://xinhua.dev/account/profile) 来确认姓名、拼音、电子邮箱和手机号码等个人信息是否正确。如果有误，请及时联系相关的部门管理员进行修改。

你也可以继续完善个人信息，比如上传一张独一无二的头像或编辑一段自我介绍。

## 首次使用 GitLab 前的配置

如果你是一名开发人员，还需要在使用 GitLab 前做如下配置。

### 设置用户信息

在你的本地开发环境上，请确保按如下的格式配置与你平台帐号一致的姓名和电子邮箱：

```sh
$ git config --global user.name 王小虎
$ git config --global user.email wangxiaohu@xinhua.org
```

> 如果此处的姓名和电子邮箱配置错误，你将无法向 GitLab 服务端推送代码。

### 设置 GitLab 操作密码

如果你想进行推送、拉取等 GitLab 操作，那么还需要在 [此页面](https://gitlab.xinhua.dev/profile/password/edit) 中设置 GitLab 的操作密码。密码至少为 10 位，且必须包括数字、大写字母和小写字母。

## 阅读使用规范

为了规范平台使用，提高开发效率，保证开发质量，请在使用平台提供的功能前阅读 [技术局代码管理平台使用规范（草案）]({{ site.baseurl }}/article/criterion-of-use.html)。
