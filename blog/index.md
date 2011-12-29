---
layout: page
title: BIPY - Blog
---

<div id="posts">
  <h2>Blog Posts</h2>
  <ul>
    {% for post in site.posts %}
      <li><span>{{ post.date | date_to_string }}</span> - <a href="{{ site.url }}/{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</div>