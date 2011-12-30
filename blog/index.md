---
layout: page
title: BIPY - Blog
---

<div id="posts">
  <h1>Blog posts</h1>
    {% for post in site.posts %}
		<code>{{ post.date | date_to_string }}</code> » <span class='post-title'><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></span>
		<div class='meta'>
		Tags: {% for tag in post.tags %}{{ tag | array_to_sentence_string }}{% endfor %}
		</div>
      <p />
    {% endfor %}
</div>