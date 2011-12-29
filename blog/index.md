---
layout: page
title: BIPY - Blog
---

<div id="posts">
  <h1>Blog Posts</h1>
    {% for post in site.posts %}
		<div class='post-title'><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></div>
		<div class='meta'>
		{{ post.date | date_to_string }}
		</div>
		<div class='abstract'>
      {{ post.content | truncatewords  }}
      </div>
      <p />
    {% endfor %}
</div>