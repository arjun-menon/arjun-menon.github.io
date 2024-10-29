public: true
title: BC's 2024 Provincial Election
---

These ridings either had the progessive vote split _(between NDP and Green)_, or the Conservative vote split with independents:

{{
	from process_data import Riding
	vote_splits = Riding.voteSplits
}}


<style>
table, td {
	border: 1px solid black;
}
th, td {
	border-style: dotted;
	padding: 3px;
}
td {
	text-align: center;
}
</style>

<table>
<tr>
<th>№</th>
<th>Riding Name</th>
<th>NDP Vote</th>
<th>Green Vote</th>
<th>Progressive Vote <br/> Total</th>
<th>Con Vote</th>
<td><em>Con <br/> Margin</em></td>
<th><em>Progressive<br/>Margin</em></th>
<td>Con+Ind.<br>Vote</td>
<th><em>Progressive Margin<br/>over Con+Ind.</em></th>
<td><em><small>Hypothetical Flip w/<br/>Ranked Choice Voting</small></em></td>
</tr>
{% for r, i in zip(vote_splits, range(1, len(vote_splits) + 1)) %}
<tr>
<td><b>{{i}}</b></td>
<td>{{r.name}}</td>
<td>{{f'{r.ndp:n}'}}</td>
<td>{{f'{r.green:n}'}}</td>
<td><b>{{f'{r.progressive_vote:n}'}}</b></td>
<td>{{f'{r.con:n}'}}</td>
<td><em>{{f'{r.win_margin:n}'}}</em></td>
<td><b>{{f'{r.progressive_margin:n}'}}</b> ({{f'{round((r.progressive_margin/r.total)*100,2):n}'}}%)</td>
<td>{{f'{(r.con+r.other):n}'}}</td>
<td><b>
{{f'{r.progressive_margin2:n}'}}
</b> ({{f'{round((r.progressive_margin2/r.total)*100,2):n}'}}%)</td>
<td>
{% if r.winner != r.hypo_winner %}
{{r.winner}} → {{r.hypo_winner}}
{% else %}
Stays {{r.winner}}
{%%}
</td>
</tr>
{%%}
</table>

This is based on the [final vote count](https://electionsbcenr.blob.core.windows.net/electionsbcenr/Results_7097_GE-2024-10-19_Party.html) published on the Elections BC website. Also [on Global News](https://globalnews.ca/news/10801085/bc-election-results-live-2024-vote/).

You can see the [Python code for this page here](https://github.com/arjun-menon/arjun-menon.github.io/tree/master/essays/pol/bc-2024).

