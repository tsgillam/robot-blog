---
layout: default
title: Default Robot Blog
---

# {{ site.title }}

{{ site.description }}

---

## 📝 Latest Posts

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>– {{ post.date | date: "%B %d, %Y" }}</small>
    </li>
  {% endfor %}
</ul>
