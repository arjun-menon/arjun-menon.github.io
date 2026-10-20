title: Arjun Menon
desc: Arjun Menon's essays, thoughts & notes.
---
<style>
.content {
	font-family: {{ fancy_sans_1 }};
}
body, p {
	font-size: 16px;
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
.endnote-mail {
	font-family: 'IM Fell English', {{ std_serif_1 }};
	font-size: large;
}
</style>

Welcome to my little corner on the internet. I'm Arjun Menon. I'm a software engineer who enjoys programming, reading (and learning new things), writing, and good conversation.

I am currently working [CaseVisit](https://casevisit.com/), and some other small side consulting gigs, and volunteering in my spare time.

### Software

I love building useful (and fun) software.

I'm looking for new work opportunities at the moment. Feel free to take a look at my open source work [**on GitHub**](https://github.com/arjun-menon), or my [résumé](https://gratom.com/arjun-menon/resume/), or the recommendations I've received on [LinkedIn](https://www.linkedin.com/in/arjungmenon/). If you know of any work that I might be a good fit for, please send them my way!

* Some of my recently-updated hobby projects includes:
	* [Alteza](https://github.com/arjun-menon/alteza): a static site generator (used by this site).
	* [PyPage](https://github.com/arjun-menon/pypage): a template language & engine (also used by this site).
	* [CashTrack](https://github.com/gratom-inc/CashTrack)<sup>(wip)</sup>: a work-in-progress cash flow tracking tool.
	* [Tax Analyzer](https://github.com/arjun-menon/tax-analyzer): gives you an NYC income tax breakdown with a graph. [**Check it out here!**](https://arjun-menon.com/tax-analyzer)

* Some of my older hobby projects includes:
	* [NeoLisp](https://github.com/novarc/NeoLisp): an experimental LISP dialect.
	* [Distributed graph algorithms](https://github.com/arjun-menon/Distributed-Graph-Algorithms): implementations of a few distributed graph algorithms, where each node in the graph is a process, and IPC is used to solve graph problems.
	* [Multi Adblock Detect](https://github.com/arjun-menon/multi-adblock-detect) ([npm](https://www.npmjs.com/package/multi-adblock-detect)): a library containing a React hook for detecting ad blockers.
	* [test_cmd](https://github.com/arjun-menon/test_cmd): a command-line black box <small>`stdin/stdout/stderr`</small>-based testing tool.

{#
### Toronto

I live in Toronto. I'm always up to meet up in-person for coffee/tea and chat, or to chat on the phone.

I've started a few public meetup groups here in Toronto:
* [Toronto Bible Study, Prayer, and Other Christian Books Group](https://www.meetup.com/toronto-bible-study-prayer-and-other-christian-books-group/): this group currently has recurring Sunday church event (for the Toronto _[NewLife church](https://nlife.ca/)_), as well as a biweekly Bible study.
* [NDP, Liberal & Green Supporters](https://www.meetup.com/ndp-liberal-green-party-supporters-group/): a group for progressive political organizing and action, with an emphasis on defending Canada from conservatives, and on enacting electoral reform.
* [Fantasy and Sci-Fi Writers Creative Collective](https://www.meetup.com/fantasy-sci-fi-writing-meetup-group/): a group for people interested in writing sci-fi and fantasy fiction. (I haven't organized any events for it yet.)
#}

### Endnote

You can reach out to me at <span class="endnote-mail">arj9 at pm dot me</span>, at my addresses listed elsewhere, or other platforms.

I live in Toronto. I'm always up to meet up in-person for coffee/tea and chat, or to chat on the phone.

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
