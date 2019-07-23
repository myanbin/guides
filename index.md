---
layout: default
title: {{ site.name }}
---

<section class="hero-content">
  <h1 class="project-name">{{ site.title }}</h1>
  <h2 class="project-description">{{ site.description }}</h2>
  <a href="{{ site.baseurl }}/firststep/" class="btn">如何开通平台帐号</a>
  <a href="{{ site.baseurl }}/tutorial/getting-started.html" class="btn">第一次上手使用</a>
  <a href="{{ site.baseurl }}/download/" class="btn">常用软件下载</a>
</section>

<section class="section-container">
  <main class="main-content">
    <h1>基础教程</h1>
    <ul class="posts">
      {% assign tutorials = site.categories.tutorial | sort: "index" %}
      {% for post in tutorials %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a><span class="required">必读</span></li>
      {% endfor %}
    </ul>
    <h1>规范文档</h1>
    <ul class="posts">
      {% assign regulations = site.categories.regulation | sort: "index" %}
      {% for post in regulations %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
    <h1>手册指南</h1>
    <ul class="posts">
      {% assign handbooks = site.categories.handbook | sort: "index" %}
      {% for post in handbooks %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
    <h1>FAQ</h1>
    <ul class="posts">
      {% assign faqs = site.categories.faq | sort: "index" %}
      {% for post in faqs %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
  </main>
</section>
