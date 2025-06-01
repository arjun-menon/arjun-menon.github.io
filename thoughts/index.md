title: Thoughts
---
<style>
.datenote {
	color: gray;
	font-size: smaller;
}
</style>

{% for dir in dir.subDirs %}
<b>{{dir.title}}</b>
	<ul>
		{% for page in dir.pages if 'incomplete' not in page.env %}
		<li>
			<a href="{{ link(page) }}">
				{% if 'strong' in page.env %}
				<strong>{{page.title}}</strong>
				{% else %}
				{{page.title}}
				{% endif %}
			</a>
			&nbsp;&nbsp;<span class="datenote">({{page.getIdeaDate('%b %-d, %Y')}})</span>
		</li>
		{% %}
	</ul>
{% %}

