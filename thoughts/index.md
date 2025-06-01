title: Thoughts
---

{% for dir in dir.subDirs %}
<b>{{dir.title}}</b>
	<ul>
	    {% for page in dir.pages if 'incomplete' not in page.env %}
	    <li>
	        <a href="{{ link(page) }}">
	            {{page.title}}
	        </a>
	    </li>
	    {% %}
	</ul>
{% %}

