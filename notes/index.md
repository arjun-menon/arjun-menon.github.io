---
title: Notes
---

<ul>
    {% for file in dir.pages %}
    <li>
        <a href="{{ link(file) }}">
            {{file.title}}
        </a>
    </li>
    {% endfor %}
</ul>


