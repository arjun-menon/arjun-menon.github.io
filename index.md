title: Arjun Menon
desc: Arjun Menon's essays, thoughts & notes.
---
<style>
.content {
	font-family: {{ fancy_sans_1 }};
	font-size: normal;
}
h1, h2 {
	margin-top: 1em;
}
ul {
	line-height: 1.6em;
}
.datenote {
	color: gray;
}
.am-icon {
	display:inline; border-radius: 16%;
}
.mdm-icon {
	display:inline; border-radius: 35%;
}
.endnote-mail {
	font-family: 'IM Fell English', {{ std_serif_1 }};
	font-size: large;
}
</style>
{{
	icon_hw = '14px'
	am_icon = link('AM-favicon-32x32')
	am = f'<img class="am-icon" src="{am_icon}" height="{icon_hw}" width="{icon_hw}"/>'
	medium_icon = link('medium-logo-square')
	mdm = f'<img class="mdm-icon" src="{medium_icon}" height="{icon_hw}" width="{icon_hw}"/>'
}}

Welcome to my little corner on the internet. I'm Arjun Menon. I'm a software engineer who enjoys programming, reading (and learning new things), writing, and good conversation. Some of my favorite topics include computer science / software, religion, politics, history, technology, science, etc.

{# ### Writings #}

I write here and [on medium](https://medium.com/@arjungmenon). A few of my writings, organized by topic, are:{# Some of my pieces include: #}
* Essays:
	* On faith:
		* {{am}} [My Hope]({{link('my-hope')}}) (also on {{mdm}} [medium](https://medium.com/@arjungmenon/my-hope-bb8d0178797b)) <span class="datenote">(Jan 18, 2020)</span>
		* {{mdm}} [Another Perspective on Hope](https://medium.com/@arjungmenon/another-perspective-on-hope-b812f6388fdc) <span class="datenote">(Jan 24, 2024)</span>
		* {{mdm}} [My Reflections on Ezekiel 36:25–27 and Isaiah 42:19–20](https://medium.com/@arjungmenon/ezekiel-36-25-27-and-isaiah-42-19-20-945028192388) <span class="datenote">(Apr 16, 2020)</span>
	* On politics and the Christian faith:
		* {{mdm}} [A disturbing thing about Christianity in North America](https://medium.com/@arjungmenon/one-disturbing-thing-on-christianity-in-north-america-9dae8088c0e4) <span class="datenote">(Aug 4, 2023)</span>
	* On life and things in general:
		* {{mdm}} [Organizing my time](https://medium.com/life-and-things/carving-out-my-time-4596332ae631) <span class="datenote">(Sep 21, 2024)</span>
	* On Canadian/etc. politics:
		* {{am}} [BC's 2024 Provincial Election, and the dire need for Electoral Reform]({{link('bc-2024-and-electoral-reform')}}) <span class="datenote">(since Oct 2024)</span>
		* {{mdm}} [Transferable Vote: a simple form of electoral reform that both the NDP and Liberals could agree on](https://medium.com/canada-forward/transferable-vote-a-simple-form-of-electoral-reform-that-both-the-ndp-and-liberals-could-agree-on-e1be752e2224) <span class="datenote">(Dec 31, 2024)</span>
		* {{mdm}} [What on earth was the NDP and Jagmeet Singh thinking? Two options to consider](https://medium.com/canada-forward/what-on-earth-was-the-ndp-and-jagmeet-singh-thinking-838e45a0daef) <span class="datenote">(Dec 28, 2024)</span>
		* {{mdm}} [Ideas for reducing emissions / pollution](https://medium.com/politics-and-systems/possible-solutions-to-reducing-pollution-carbon-emissions-d87f37ebf458) <span class="datenote">(Dec 29, 2024)</span>
* {{am}} [Fiction]({{link('fiction')}}): I'm slowly starting to write a series of short stories, in the fantasy genre.
{# * [Thoughts]({{link('thoughts')}}): Just some short things and thoughts that I'm scribbling down. #}

I hope the stuff I write contains good ideas, or is encouraging / uplifting / hope-inducing, or otherwise edifying in some way.

### Software

I'm looking for new job opportunities at the moment. Feel free to take a look at my open source works [**on GitHub**](https://github.com/arjun-menon), or my [résumé](https://gratom.com/arjun-menon/resume/), or the recommendations I've received on [LinkedIn](https://www.linkedin.com/in/arjungmenon/). If you know of any jobs that I might be a good fit for, please send them my way!

* Some of my recently-updated open source software includes:
	* [Alteza](https://github.com/arjun-menon/alteza): a static site generator (used by this site).
	* [PyPage](https://github.com/arjun-menon/pypage): a template language & engine (also used by this site).
	* [CashTrack](https://github.com/gratom-inc/CashTrack)<sup>(wip)</sup>: a work-in-progress cash flow tracking tool.

* Some of my older open source software includes:
	* [NeoLisp](https://github.com/novarc/NeoLisp): an experimental LISP dialect.
	* [Tax Analyzer](https://github.com/arjun-menon/tax-analyzer): gives you an NYC income tax breakdown with a graph. [Check it out here](https://arjun-menon.com/tax-analyzer).
	* [Distributed graph algorithms](https://github.com/arjun-menon/Distributed-Graph-Algorithms): implementations of a few distributed graph algorithms, where each node in the graph is a process, and IPC is used to solve graph problems.
	* [Multi Adblock Detect](https://github.com/arjun-menon/multi-adblock-detect) ([npm](https://www.npmjs.com/package/multi-adblock-detect)): a library containing a React hook for detecting ad blockers.

### Endnote

You can reach out to me at <span class="endnote-mail">arj9 at pm dot me</span>, at my addresses listed elsewhere, or other platforms.

I hope to write more stuff in the near future, and publish it here as well as elsewhere.


{#

<p>
<ol>
{% for d in dir.subDirs %}
{% if d.title and d.shouldPublish and d.hasIndexPage %}
<li><a href="{{link(d)}}">{{d.title}}</a></li>
{% endif %}
{% endfor %}
</ol>

&mdash; Arjun Menon

#}
