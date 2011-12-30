---
layout: page
title: BIPY - Blog
---

<div id="posts">
  <h1>Blog posts</h1>
    {% for post in site.posts %}
		<div class='post-title'><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></div>
		<div class='meta'>
		Written on {{ post.date | date_to_string }}, and filled under {% for tag in post.tags %}{{ tag | array_to_sentence_string }}{% endfor %}
		</div>
      <p />
    {% endfor %}
</div>