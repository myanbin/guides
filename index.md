---
layout: default
title: 首页
---

<section class="hero-content">
  <h1 class="project-name">需要帮助？</h1>
  <h2 class="project-description">{{ site.description }}</h2>
  <a href="{{ site.baseurl }}/firststep/" class="btn">如何开通平台帐号</a>
  <a href="{{ site.baseurl }}/article/getting-started.html" class="btn">第一次上手使用</a>
  <a href="{{ site.baseurl }}/article/download.html" class="btn">常用软件下载</a>
</section>

<section class="section-container">
  <main class="main-content">
    <h1>基础教程</h1>
    <ul class="posts">
      {% assign tutorials = site.categories.tutorial | sort: "index" %}
      {% for post in tutorials %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> <span class="my-label">必读</span></li>
      {% endfor %}
    </ul>
    <h1>规范文档</h1>
    <ul class="posts">
      <li><a href="{{ site.baseurl }}/article/management-regulations.html">技术局代码管理平台管理细则（草案）</a></li>
      <li><a href="{{ site.baseurl }}/article/criterion-of-use.html">技术局代码管理平台使用规范（草案）</a></li>
      <li><a href="{{ site.baseurl }}/public/registration-form-v6.xlsx" download="技术局代码管理平台注册登记表-v6.xlsx">附件：技术局代码管理平台注册登记表</a><span class="my-label">新版</span></li>
    </ul>
    <h1>手册指南</h1>
    <ul class="posts">
      {% assign handbooks = site.categories.handbook | sort: "index" %}
      {% for post in handbooks %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
    <h1>常见问题 FAQ</h1>
    <ul class="posts">
      {% assign faqs = site.categories.faq | sort: "index" %}
      {% for post in faqs %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
  </main>
</section>
