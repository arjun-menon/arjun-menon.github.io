public: true
title: BC's 2024 Provincial Election
---

These are the ridings progressive voters would have won, had the progessive vote _not been split_ between NDP and Green:

{{
	from process_data import Riding
	progressive_splits = Riding.progressiveSplits()
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
<th><em>Con Victory <br/> Margin</em></th>
</tr>
{% for r, i in zip(progressive_splits, range(1, len(progressive_splits) + 1)) %}
<tr>
<td><b>{{i}}</b></td>
<td>{{r.name}}</td>
<td>{{f'{r.ndp:n}'}}</td>
<td>{{f'{r.green:n}'}}</td>
<td><b>{{f'{r.progressive_vote:n}'}}</b></td>
<td>{{f'{r.con:n}'}}</td>
<td><b>{{f'{(r.progressive_vote - r.con):n}'}}</b></td>
</tr>
{%%}

</table>
