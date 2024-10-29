public: true
title: BC's 2024 Provincial Election
---

We need electoral reform in BC as soon as possible. BC came dangerously close to putting <abbr title="climate-change-denying & anti-vaxx">anti-science</abbr> pro-nimby conservative nutjobs in power. It is no small thing to endanger the future of a province with millions of people over an inability to enact electoral reform. The real harm that a Con victory would have caused people for four whole years cannot be understated. The <u>Legislative Assembly of British Columbia has the authority to pass electoral reform without subjecting the decision to an unnecessary referendum</u>.

#### Ridings where Split Votes made a difference

These ridings either had their progressive vote split between NDP and Green, or their conservative vote split by independents:

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
<th><em>Progressive Margin<br/>over Con + Ind.</em></th>
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
<td><em>{{f'{(r.con - r.ndp):n}'}}</em></td>
<td>{{f'{r.progressive_margin:n}'}} ({{f'{round((r.progressive_margin/r.total)*100,2):n}'}}%)</td>
<td>{{f'{(r.con+r.other):n}'}}</td>
<td><b>
<span style="color: {% if r.progressive_margin2 > 0 %}green{% else %}darkred{% %};">
{{f'{r.progressive_margin2:n}'}}
</span></b> ({{f'{round((r.progressive_margin2/r.total)*100,2):n}'}}%)</td>
<td>
{% if r.winner != r.hypo_winner %}
{{r.winner}} → {{r.hypo_winner}}
{% else %}
Stays {{r.winner}}
{% endif %}
</td>
</tr>
{%%}
</table>

{{
	PR = '<abbr title="Proportional Representation">PR</abbr>'
	RCV = '<abbr title="Ranked Choice Voting">RCV</abbr>'
}}

With <abbr>RCV</abbr> (Ranked Choice Voting), a probable outcome would have been that the NDP picks up a net of 5 seats (NDP flips 7, Conservatives flip 2). The outcome, with {{RCV}}, would have been the NDP at 52 seats, the Cons at 39 seats, and the Greens at 2 seats. Progressives would have held 54 seats (58%) in the legislature, instead of the 49 seats today.

With <abbr>PR</abbr> (Proportional Representation), a likely outcome would have been the NDP at <abbr title="(0.4487/(0.4487+0.0824+0.4327))*93 ~= 43">43 seats</abbr>, the Cons at <abbr title="(0.4327/(0.4487+0.0824+0.4327))*93 ~= 42">42 seats</abbr>, and the Greens at <abbr title="(0.0824/(0.4487+0.0824+0.4327))*93 ~= 8">8 seats</abbr>. With {{PR}}, progressives would have had a slightly thinner majority of 51 seats (55%). {{PR}} would effectively have required some kind of agreement between the NDP and Greens, in order to govern. I favour {{PR}}.

On a side note, it's highly probable that {{RCV}} (or {{PR}}) would lead to more Green votes, and the Green party would most likely have ended up with more seats, especially since the risk of vote wastage with vote splitting often steers many people away from smaller parties, even if they really like a smaller party.


#### Independent Candidates

Most independent candidates held conservative views.

I've excluded the Ladysmith-Oceanside riding from the list above, since the independent spoiler candidate there ([Adam Walker](https://en.wikipedia.org/wiki/Adam_Walker_(Canadian_politician))) was a former NDP MLA who had been expelled from the NDP. This riding was won by the NDP, so Adam Walker's presence did not spoil this seat for progressive voters.

The two ridings which would have flipped from the NDP to the Cons were:

* Richmond-Steveston: former BC United candidate [Jackie Lee](https://en.votemate.org/bc2024/candidates/8680) ([news article](https://www.richmond-news.com/2024-bc-votes/mixed-messages-for-bc-united-candidate-in-richmond-9508820)) was running here.

* Vernon-Lumby: former BC United candidate [Kevin Acton](https://www.vernonmorningstar.com/local-news/acton-ready-to-run-for-conservatives-in-vernon-lumby-riding-if-tapped-7512647) and a Libertarian candidate [Robert Johnson](https://www.castanet.net/news/Vernon/509798/Vernon-Lumby-riding-gains-Libertarian-candidate-Robert-Johnson) were running here.

The four ridings above, won by the Cons, which would have stayed with the Cons, that had independent candidates were:

* Penticton-Summerland: former BC United candidate [Tracy St. Claire](https://www.pentictonherald.ca/news/article_82a26fda-7796-11ef-a66e-576f40276dbf.html), [Roger Harrington](https://www.summerlandreview.com/election/harrington-runs-as-independent-in-penticton-summerland-riding-7566997) ([FB](https://www.facebook.com/Roger4MLA/)), and [Anna Paddon](https://www.castanet.net/news/Penticton/511427/Meet-Anna-Paddon-independent-candidate-in-Penticton-Summerland) ran here. Anna Paddon got 144 votes, and she seems to have been a progressive candidate. Roger Harrington who got 827 votes, on the other hand, appears to be conservative who's re-posted insane conspiracy theory videos on Facebook, and seems to be a supporter of [Corinne Mori](https://www.nelsonstar.com/election/kootenay-central-election-2024-independent-candidate-corinne-mori-7564643), a conservative and anti-vaxxer who ran as an independent for the Kootenay Central riding.

* Kelowna Centre: [Michael Humer](https://www.kelownacapnews.com/local-news/meet-michael-humer-independent-candidate-for-kelowna-centre-7564981) was the independent candidate here. He said he was "running to represent the fiscally responsible, socially inclusive centre-right voter". He doesn't seem as extreme or insane as the typical BC Conservative, so it's possible that under RCV, votes for him would have trickled down to both the NDP and the Cons.

* Boundary-Similkameen: former PPC candidate [Sean Taylor](https://www.pentictonwesternnews.com/local-news/former-peoples-party-candidate-running-for-mla-of-boundary-similkameen-7551429) ran here, and got 779 votes. The PPC is a single-issue far-right party that calls for a moratorium on immigration.

* Langley-Walnut Grove: [Carlos Suaréz Rubio](https://en.votemate.org/local2022/candidates/6828) was the independent here, but his page says he's with BC Cons, even though Misty Van Popta was the BC Con for this riding. No idea what the story was here; perhaps his candidacy was rejected by the Cons, and so he decided to run as an independent.

#### Sources

This is based on the [final vote count](https://electionsbcenr.blob.core.windows.net/electionsbcenr/Results_7097_GE-2024-10-19_Party.html) published on the Elections BC website. You can also explore the election results with an interactive map [on Global News](https://globalnews.ca/news/10801085/bc-election-results-live-2024-vote/).

You can check out the [Python code for this page here](https://github.com/arjun-menon/arjun-menon.github.io/tree/master/essays/pol/bc-2024).

