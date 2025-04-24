public: true
title: Endor
desc: A series of short stories, set in Endor and Valinor.
---

I'm writing a series of short stories, partly inspired by the universes of Tolkien, C.S. Lewis' [Space Triology](https://en.wikipedia.org/wiki/The_Space_Trilogy)<sup>([fandom](https://the-silent-planet.fandom.com/wiki/Ransom_trilogy), [narniafans](https://narniafans.com/books/the-space-trilogy/))</sup>, [Frieren](https://en.wikipedia.org/wiki/Frieren), Harry Potter, etc.

The temporary placeholder name for these, for now, is Endor <sup>([definition](https://tolkiengateway.net/wiki/Endor))</sup>.

### Chapters

{% for page in dir.pages %}
* <a href="{{link(page)}}">{{page.title}}</a>
{% %}

