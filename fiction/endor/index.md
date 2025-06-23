---
title: "Endor: On Truth & Lies"
desc: "Endor: a story about truth & lies, some elves, magic, a bad king, etc."
---
<style>
h3 { font-size: 135%; color: darkgoldenrod; padding-top: 6px; }
h4 { font-size: 124%;  color: goldenrod; padding-top: 5px; }
h5 { font-size: 100%;  color: goldenrod; padding-top: 5px; }

.floating-bubble {
  font-size: 17.5px;
  border-radius: 20px;
  box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.3);
  padding: 11.5px 9px;
  width: fit-content;
  margin: 0 auto;
}

p {
   /*text-indent: 1.2em;*/
   text-indent: 0.25em;
}

.para_first::first-letter {
  font-size: 3em;
  initial-letter: 2;
  float: left;
}
.para_first, .pg {
  text-indent: 0;
}

.pg {
  font-style: italic;
}

</style>

<p><div class="heading floating-bubble" style="background-color: orange;">
Note<sup>1</sup>: This is a <em>work-in-progress</em>, and is frequently being updated these days.
</div></p>

<p><div class="heading floating-bubble" style="background-color: #ffcb00;">
Note<sup>2</sup>: this story interleaves <em>parallel perspectives</em>. Chapter subheadings indicate which.
</div></p>

<p><div class="heading floating-bubble" style="background-color: mediumpurple; text-align: center;">
Note<sup>3</sup>: most chapters comes with a piece of music to be enjoyed along with the chapter.<br>
You might need to click the ▶ play button twice, and be logged into Spotify on your browser.
</div></p>

{#
<p><div class="heading floating-bubble" style="background-color: silver;">
Note<sup>4</sup>: this story is inspired by an essay I'm working on called <em><a href="{{link('conservatives-and-lies')}}">Conservative Politicians & Lies</a></em>.
</div></p>
#}

{{
ch_num = 0
def chn(check_n = None):
    global ch_num
    ch_num += 1
    if check_n is not None:
        assert(check_n == ch_num)
    return ch_num
chrs = {}
places = {}
}}

{% def spotify_embed track_id caption %}
<figure style="float: right;">
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{{track_id}}?utm_source=generator" width="250" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
<figcaption style="text-align: center;"><h5><em>Music: {{caption}}</em></h5></figcaption>
</figure>
{% %}

{{
council_of_elrond = ("3Knohqfb9jeYzL6wMZiWLM", "The Council of Elrond")
children_tinlicker = ("3PUnmXpIRfLa8yI9wfgJPC", "Children by Tinlicker")
unicorns_rest = ("1z9JX28wuVnQ0KDN1jdDVP", "Unicorn's Rest<br>by Bill Brown")
arise_es_posthumus = ("6WtGYhmAmMcrIr6sj86FDC", "Arise by E.S. Posthumus")
the_mandalorian = ("6tJFtthY0rI1x06qb8NjK0", "The Mandalorian")
celtic_lore = ("0dErnwCOJio6gkYfzPUfSa", "A Celtic Lore<br>by Adrian Von Ziegler")
machina_del_diablo = ("21sBRQODrIuLIrwK5VdGfV", "Machina del Diablo")
cornfield_chase = ("6pWgRkpqVfxnj3WuIcJ7WP", "Cornfield Chase<br>by Hans Zimmer")
the_riders_of_rohan = ("1mJxXKuqwo0TBwf13vBUKH", "The Riders of Rohan")

chapter_music_mapping = {
    1: council_of_elrond,
    2: children_tinlicker,
    3: unicorns_rest,
    4: arise_es_posthumus,
    5: the_mandalorian,
    6: celtic_lore,
    7: machina_del_diablo,
}

def spotify():
    global ch_num
    if ch_num not in chapter_music_mapping:
        raise Exception("Chapter %d does not have a music mapping." % ch_num)
    track_id, caption = chapter_music_mapping[ch_num]
    write(spotify_embed(track_id, caption))
}}
### Part 1: Zior and Lies

#### Chapter {{chn(1)}}: In Aeterna, and going to Endor

{{ spotify() }}

<p class="pg">From the perspective of beings in the eternal realm of immortals, Aeterna:</p>

{{
places['Aeterna'] = "eternal realm of the undying. Loosely based on J.R.R. Tolkien's [Valinor](https://en.wikipedia.org/wiki/Valinor). "
}}

<p class="para_first">
Aeterna, the realm of the undying, existed in a dimension anything unlike our universe of planetary worlds inhabited by carbon-based organic life forms. The eternal beings of Aeterna, eldil, lived across these hexagonal and other polygon-shaped platforms, that floated across the endless sky. The horizon was scattered with them. They were all at different altitudes, and they were never adjacent. Most of these platforms were lush green, covered with grass and trees. Buildings and other structures made of stone or marble interrupted the greenery. Crystal glass escalators and circular iridescent magical portals connect them to one another. Interspersed between these platforms were puffy white clouds with glistening streams of water steadily pouring out of them. Rainbow streaks often marked these magical waterfalls. At the bottom, all that’s visible is a gentle rising mist that dissipates as it gets higher.</p>

{{
chrs['Rohan'] = "an eternal being (eldila) who goes down to Endor as a young elf, confront Philateros, etc. The eldila are very loosely based on the C.S. Lewis [Space Trilogy](https://en.wikipedia.org/wiki/The_Space_Trilogy)'s<sup>([fandom](https://the-silent-planet.fandom.com/wiki/Ransom_trilogy), [narniafans](https://narniafans.com/books/the-space-trilogy/))</sup> [eldil](https://the-silent-planet.fandom.com/wiki/Eldil), but in this story they are more elf-like in features, etc. The elves are also loosely inspired by the elves in Tolkien's world, the manga [Frieren](https://en.wikipedia.org/wiki/Frieren), etc."

chrs['Alethea'] = "an eternal being (eldila) who goes down to Endor as an old elven wizard, brings truth, etc. The name Alethea means truth as well, per [this Wikipedia article](https://en.wikipedia.org/wiki/Alethea)."
}}
“Let’s go down to Endor”, said Rohan, speaking to Alethea, “it’s been a while since we’ve been down there”.

{{
places['Alpha Centauri'] = "the star system that this story takes place. See Wikipedia on [Alpha Centauri](https://en.wikipedia.org/wiki/Alpha_Centauri)."
places['Proxima Centauri'] = "the exosolar system that this story takes place. See Wikipedia on [Proxima Centauri](https://en.wikipedia.org/wiki/Proxima_Centauri)."
places['Endor'] = "the planet this story takes place in. The name is taken from J.R.R. Tolkien's [Endor](https://tolkiengateway.net/wiki/Endor), which in LOTR lore is the Quenya name for Middle-earth. "
}}
The immortal eldil of Aeterna could cross dimensions, and visit our universe, and descend down to the planets, whenever they wished. Endor was a planet of Proxima Centauri (in the Alpha Centauri system) that Rohan and Alethea had a long history with. Endor had one giant Pangaea-like continent and several smaller island continents, and most of the land was covered in tropical rainforests, cities, towns, and other settlements. Elves, humans, dwarves, talking trees, and other creatures inhabited the land. Magic filled the air, and every creature used magic in some way. Wizards from all species invented new kinds of magic all the time, and traded in magical recipes, spells, and all sorts of magical objects.

Alethea was sitting on a white couch with gold streaks patterns, in Rohan's living room.

“How long do you think you’ll want to hang around this time?” asked Alethea.

The eldila of Aeterna could go down as humans, or as elves, or as other creatures. If they went down as elves, they kept a full breadth of magical powers. They could choose to go down keeping their memories and knowledge and skills and power, which most did.

But in terms of memory, they also had the choice to down tabula rasa. In this case, they would start with a blank state, with no memories. However, they still retained a faint connection to the beings in Aeterna, whom they could hear through soft whispering thoughts in their mind. When they went back to Aeterna, they remembered everything again, with the memory of their short human life added on. Some took this route as a challenge.

“A hundred years or so,” said Rohan, waving his hands.

“I’ll join you for a dozen years or so”, replied Alethea.

##### Naiadryl
{{
chrs['Naiadryl'] = "a translucent pet octopus, who can fly, and who lives with Alethea."
}}
Her pet, Naiadryl, a translucent octopus, was curled up near her feet, with the tips of his tentacles resting comfortably in between her toes. Naiadryl had a fiercely independent spirit. He could move around with ease, go through the portals, and scale the crystal glass stairs that linked and connected all the hexagons together with great speed and agility, as well as fly and float in the air. Naiadryl loved to play. He'd been hanging out with Alethea for a thousand years or so.

Alethea stared intently at Naiadryl’s slightly-squishy gelatinous head, and grabbed his cheeks tightly. Naiadryl’s cheeks turned a bit pink as a result of her tight grip, but he didn’t mind. Naiadryl loved Alethea.

"Go off now, I'll be back in a decade or two," she told Naiadryl, who understood. He gave her a big giant hug, and scurried toward Rohan, and gave his palm a small squeeze as well. Then Alethea watched as Naiadryl ascended a particularly long set of crystal stairs with ease. There was a rainbow-streaked waterfall halfway up. Naiadryl stopped at the edge of a stair, jumped off and gently flew towards the flowing water, and started playing and splashing around in the water flowing down.

##### Leaving

Even though it wasn't cold, snow that never melted occasionally floated across the air. Around a quarter of the trees were covered in snow. This snow was cool, light, and eminently edible with a fresh watery deliciousness. The sun never stopped shining in Aeterna, and the snow resting on leaves and elsewhere glittered like diamonds in the endless sunlight.

Rohan and Alethea got up and walked towards a portal on their platform. Alethea scooped up snow off a tree's leaf, and held it in her mouth, feeling its crisp crunchy coolness for a while, before swallowing the snow. They were heading to another hexagonal block where there was a portal to the planet Endor.

They stepped through the circular portal, and stepped out the other side. A cobblestone path led down to a town square. There were some tall spirally cylindrical towers scattered about the woods nearby. A few eldil were walking around, some flying in the air, and some sitting on tree branch or on the ground.

##### Baklava

As they walked down the tree-lined cobblestone path, they passed by some delicacy plates. Magical marble stands that were about four feet high, with engravings and relief art of magical creatures and nature, with flat surfaces on top, had these silver plates on them, with various kinds of delicacies. Coming up with a recipe was a work of art, and when someone came up with a recipe for a new delicacy, they'd program and create a magical stand that regenerated these delicacies forever. People could enjoy them whenever (as food never went bad in Aeterna), and they'd be magically replenished. Sometimes the author of the recipe would go back and make little tweaks and changes, so it never really stayed the same.

No one needed to eat food in Aeterna, since everyone in Aeterna was immortal. The food was all zero calories, and the purpose of food in Aeterna was purely for enjoying eating. When you ate food in Aeterna, you got to taste it deeper than you ever could in the planetary realm, and what you ate just simply dissolved and disappeared into thin air.

<img src="{{link('baklava-wiki-ir')}}" style="width:200px; height:auto; float: right;">

Rohan stopped by a stand with some golden looking stuff. Looking closer, these were baklava, with the flakiest filo pastry layers you've ever encountered, with layers of honey and rosewater mixed in with pieces of sliced almonds and crushed pistachios. Alethea and Rohan popped a piece each into their mouths. Crunch. Crunch. Crunch. They took a moment to enjoy its delicate taste and rosy aroma.

##### On to Endor

Then, they reached the portal that went to Endor. There was a small line-up of five eldil ahead of them.

#### Chapter {{chn(2)}}: Nauriel and some thieves

{{ spotify() }}

<p class="pg">From the perspective of Nauriel, on Endor:</p>

{{
chrs['Nauriel'] = "a half-elf half-human who lives on Endor, and is the main character of the 2nd parallel storyline here."
}}

<p class="para_first">
My friend (and roommate) was thoroughly sick and bedridden, and I wanted to find a cure quickly.</p>

##### Visiting Pelegrin
{{
chrs['Pelegrin'] = "a wizard who worked as a town doctor and apothecary."
}}

I went to Pelegrin, a local wizard who was both a doctor and an apothecary. Pelegrin towered over me, eyebrows furrowed, with his bushy mustache looking down at me with suspicion, as though he didn’t trust me. I had stolen a transparency potion of his when I was a little kid, and he hadn’t forgotten that.

“My friend is sick. He has an awful headache, and he can’t see well. He says he sees things through a white mist.” I said.

“I know what that is. I have a potion that’ll cure him right up. It’ll be eight gold coins.” Pelegrin replied.

“I don’t have eight gold coins. Could I give you three for now, and five later?” I asked.

“I’m afraid I’ll need it now. This illness won’t kill him,” replied Pelegrin, continuing to eye me suspiciously.

I didn’t want to press the matter, so I left quietly. I went and sat on a rock nearby, pondering what to do next.

##### My Churro

I was a bit hungry.

Thankfully, I had a scroll in my pocket (along with other scrolls) for my favorite snack. One that I myself had painstakingly and carefully engineered over several iterations over years.

I learned a spell to make churros when I was eight years old, but over the years, I made a lot of little tweaks to it. I had adjusted the spell to have the churro's outer fried layer be exactly the level of crunchy I liked, the inside have the soft airy chewiness I enjoyed, and change the white sugar to maple sugar powder, and lastly incorporated chai spices into the dough bread mix (that I copied from a chai tea spell). After years of tweaking, I'd achieved what I call perfection with it. It was a party favorite.

I opened up the scroll, and conjured up a stick of my unique churro. Munching on the churro cured some of the disappointment I felt at how Pelegrin still saw me.

##### Grunt's Keep

I walked over to a corner of the town, by the woods. There was a little wooden shack there, with a hand-crafted wooden sign with little wooden sticks nailed together that spelled out "Grunt's Keep". Some illumination spell gave the sign a faint firefly-like glow. Inside, was a little bar, frequented by not-so-trustworthy people, and various kinds of outcasts.

I went over to a table with the least scary looking group of people, and asked, “Is there any way I could come about five gold coins?”

{{
chrs['Tim'] = "a strong dwarf, and the leader of a small band of thieves."
}}
“Hullo, I’m Tim. We have a little job a bit north of here. Help us out, and five coins is yours,” replied a burly looking dwarf.

“Whereto?” I asked.

“The fewer questions, the better”, Tim replied.

<figure style="float: right;">
<img src="{{link('chico-staring-from-a-bed')}}" style="width:200px; height:auto;">
<figcaption style="text-align: center;"><h5><em>Chico's stare</em></h5></figcaption>
</figure>

##### Chico
{{
chrs['Chico'] = "Tim's pet dog, a miniature schanuzer, with a fiesty personality."
}}
Tim had a small dog, a miniature schnauzer (with mostly black hair but with white-haired eyebrows and a white-haired mustache and beard) sitting next to him, who gazed at me intently.

"That's Chico. He's a good boy," Tim added.

The next day they gave me a merchant’s outfit, which they’d magically shrunk to my size. We got into a carriage, which was pulled by these translucent iridescent mist-like beings that looked like seahorses.

Chico sat across from me, and continued to stare at me with a soul-piercing intensity.

#### Chapter {{chn(3)}}

{{ spotify() }}

<p class="pg">From the perspective of Rohan and Alethea:</p>

<p class="para_first">
“Let’s pick a form.” Rohan said.</p>

Rohan decided to take the form of a small young elf.

Alethea took the opposite route and adopted the form of an old elven wizard.

##### On the mountainside

In a few moments, they emerged out of a portal in a cave on a mountain beside the city Zior. They made their way down.

This mountainside and its valley marked the place where humans had first arrived in Endor, about a thousand years ago. An engraved bronze plaque near the portal commemorated this event. Inscribed on it was:

> _**Humans Reaching Proxima Centauri and the planet Endor**_

> An enormous spaceship glittering with thousands of lights emanating from small windows.

> The inhabitants of Endor look up to the ship, and examine it, both from afar, and up close.

> Humans in the ship blast a cacophony of radio waves in all directions, hoping to be understood.

> The people of Endor, who have perfected the art of magic, cast a spell that automatically translates.

> Representatives from Endor _and across Proxima Centauri_ magically transport themselves to the human spaceship.

> Long, deep, meaningful conversations follow, for many days, and they get to know each other.

> The beings of Proxima Centauri graciously invite the humans to join them, and settle down, and live permanently on the planet Endor. _Unlike the beings of other star systems._

> The humans’ ship gradually descends, swaying gently, and lands on the planet Endor, with their ship protected and gently held in the safe embrace of the powerful magic of some talented elves.

> The humans settle down in Endor, with the generous support of the beings living in Endor.

> The humans discover new trades, crafts, and various other productive things to do in Endor.

> Humans learn to do magic, and blend it with their technology, to fabricate new kinds of magic.

> Life is forever transformed by the arrival of humans to Endor.

A few small travelers’ outposts dotted the mountainside, serving food and drink. Several had food and drink that was magically replenished, without the need for attendance by someone. A few rare outposts had a powerful interactive magical interface, where you could just imagine what edible you wanted, allowed it to read that thought of yours, and the food or drink you wanted would be magically conjured up before you.

A planet-wide centralized system of credit lines meant you could get whatever you wanted, and pay for it later. But, of course, people deep in debt had to use coins.

##### Andy

As they got close to the bottom of the mountain, they reached a dwarven settlement built on the last slight downward slope of the mountain. The unpaved rocky path gave way to cobblestone roads.

{{
chrs['Andy'] = "dwarf, who gives Rohan and Alethea a place to rest the night, after their arrival to Endor."
}}
As they were passing by a row of houses, an old dwarf popped out and said, “Oh wow! How long have you been around? It’s been a long time since we’ve seen any elves here.”

Rohan replied, “We just arrived.”

“I’m Andy. If you’re looking for a place to sleep tonight, I’d love to have you stay over.” Andy said.

They were looking to rest, so they took up Andy’s generous offer.

Andy's sod-roofed house was cozy inside. There were a few bird swings hanging from the ceiling, and he had a small cardinal bird sitting on his table next to his notebook. A parrot perched by a bookshelf as well.

##### Ildris
{{
chrs['Ildris'] = "an eldil visiting Endor in bird form (as a bright red cardinal)."
}}

Andy had a circle of seven cushy deep couches, with a round table in the center that was scattered with books, scrolls, a few fountain pens, an open ink bottle, and parchments with things scribbled on them. Rohan and Alethea sunk into two couches. As they were chatting, the red cardinal flew over and looked inquisitively at them.

Suddenly, the cardinal spoke, "it's good to have you here".

Andy interjected, "this is Ildris, he's a visiting eldil actually".

{{
chrs['Iluvatar'] = "very similar to Tolkien's [Iluvatar](https://tolkiengateway.net/wiki/Il%C3%BAvatar)."
}}

"True, but that's not quite the full story", the red cardinal bird named Ildris replied, with a wizened voice that sounded steeped in wisdom. "I was a human four hundred fifty years ago. Iluvatar took me up, and turned me into an eldil while I was still alive on Earth. This is my third visit to the realm of the mortals."

Alethea found Ildris' choice of bird form both peculiar and amusing. 


{#
TODOs:
- A cardinal with the spirit of an immortal human who was invited to Aeterna. (wiki image embed?)
- The Cardinal talks about the simulations and spirits being placed in stasis ... for later ... analysis ... but doesn’t say too much more about it ... he was picked out early ... all of this is revealed/done in dialog.
- An annoying regular parrot who repeats himself. In his small brain, he’s annoyed and mildly jealous at the cardinal’s frequent incessant chit-chat chatter, which all the hit creatures seemed to pay great heed to.
- Virtual projection from Aeterna?
#}

#### Chapter {{chn(4)}}

{{ spotify() }}

<p class="pg">From the perspective of Nauriel:</p>

<p class="para_first">
I was quite anxious about joining these robbers. But if my friend couldn’t work, I couldn’t afford to cover the rent on my own, and we’d lose our house. We were already late on last month’s rent. I kept quite mum on the way to wherever we were going. The last thing I wanted to do was irritate these professional thieves with my small talk. I didn’t want to get tossed out for asking some annoying question.</p>

After about a day, and after having unhappily relieved myself in the woods while an annoying bird watched me, I began to make out the outline of some city.

{{
chrs['Olin'] = "highly talented human wizard, and wand maker. Loosely based on Harry Potter's [Ollivander](https://harrypotter.fandom.com/wiki/Garrick_Ollivander)."
}}
“Have you heard of Olin?” said Tim, who sat across from me.

“No, I haven’t. Who’s that?” I said, curious to know more.

“Well, he’s only the best wand maker in a thousand miles.” Tim said, with mischievous grin.

“Are we doing something for him?” I asked.

“No, do we look like we work for a living to you?” Tim replied, incredulously.

I surmised the plan was to Robin. “Well…isn’t all this stealing a form of work...?” I replied.

“It’s fun, actually. I don’t really need to do it anymore. I do it for the thrill of it. Our last heist was enough to retire on. But that was too boring for me. Besides, I have an escape token that’ll transport me right back home if anything goes wrong, so I’ve got nothing to worry about.” Tim said, sounding confident and excited.

“What if you get killed before you can escape?” I asked Tim.

Tim quickly replied, “Do I look like I started doing this yesterday?”

##### Kae
{{
places['Kae'] = "the city where Olin has his shop."
}}
As we got close to the city, apparently named Kae, a fear and anxiety grew in my stomach. I wanted to leave and go back home. Perhaps a homemade remedy would have sufficed.

But I was too scared to leave now. What would Tim and his friends do if I tried to bail on them now?

We got off the carriage by some woods close enough to the city that I could see rooftops through the foliage.

{#
TODOs:
- Chico, the dog with the seriousness of a general at war.
- Chico mind communicating with the elves. Chico talking about random stuff he’s heard. (Chico dog photo embed?) 
-  An annoying eldil knowing everything, but who won't share anything with us mortal?
#}

{{
chrs['Arlo'] = "a member of Tim's crew of robbers."
}}
A bearded man, Arlo, who had sat silently by Tim during our journey (but always nodding in agreement to things Tim said) waved his hands over the misty seahorses, saying some mysterious words, and I saw them turn into a watery looking liquid and go into a vial he wore as a necklace. He then repeated the motions with our carriage, and our carriage shrunk to thimble size. He picked it up from the ground and put it in his pocket.

“Your job will be to grab some tiny bags of fairy wing dust that Olin has in his storage room,” Tim said with a tone which indicated that I didn’t have a choice about the task, adding “It shouldn’t take you long. We’ll keep him distracted and preoccupied while you nab six bags. Each of your coat’s six pockets can conceal a bag; a concealment spell has been cast on them, so no one can detect them once the bags are in your pockets.”

Tim pulled up a hand-scrawled map and pointed to the top right corner, and said “There’s a trapdoor near these shelves. Sneak in and follow the short tunnel to the end; that’s where Olin’s storage room is. Arlo will put a quietness spell on you which will still the air surrounding you, so you’re not heard.”

##### Olin's wand shop
As we walked nonchalantly into Olin’s wand shop, my heart was beating so loudly that had it not been for Arlo’s silencing spell, I think everyone would have heard it. Olin had a round face, most clean shave, except very thin long wispy white goatee several centimeters long. It swung about as he walked over to greet us.

Tim strolled up and said confidently “We’re looking for a training wand for my niece. Do you have any recommendations?”

“Oh, yes, we have lots of different kinds of training wands. What kind of magic is she training in?”

“Healing magic,” said Tim.

“Alright. Let me get you a catalog of what we have”.

As Olin was grabbing a catalog file that had “<small>HEALING TRAINING WANDS</small>” scribbled on the side, he noticed my overly anxious facial expression and asked, “Are you alright?” with genuine kindness and care.

“I’m alright. Just a bit tired,” I replied. I felt bad about what I was about to do.

I slowly moved away, pretending to look around the shop, while Tim peppered Olin with questions about the pros and cons of various wands. As I inched closer to what seemed like the trapdoor, I prayed and hoped that Arlo’s spell held. I lifted its dirty handle and slipped in quickly. I heard it close with a thud. But assuming that Arlo’s spell worked, I’d be fine. The tunnel wasn’t too long. At the end of it was a circular wooden door with a wavy bronze handle. I didn’t notice a keyhole. I turned the handle, and I was inside.

##### Olin's wand shop's storage room

There was a veritable cornucopia of things in here. Wand making was a complex art that involved many ingredients that varied depending on the kind of wand to be made.

I carefully looked around. I couldn’t stop looking at all the objects that surrounded me. There were so many fascinating things. I could easily get lost examining these things for hours. I hated the fact that I had so little time to spend here.

Tim had forgotten to tell me where to find this dust. What did he expect me to do? Look for a bag labeled fairy wing dust? Thankfully, I had a locating spell up my sleeve--one that I learned as a kid, and which has been useful to me for many years. I muttered an incantation. A soft yellow light accompanied by a slight humming sound emanated a few shelves away. I walked over, toward a shelf, where there was a box conveniently labeled “fairy wing dust”. I only saw three bags inside the box. Well, that would have to do, I thought. I pocketed the three bags. But just as I was about to leave, I saw an open box on a table that piqued my curiosity. I went over to look at it. In it was the most elaborate wand I had ever seen. Instead of wood, this wand seemed to be made of metal and was covered in a twirling gold and glistening green pattern. I grabbed the wand and tucked it in an inner pocket of my coat. It pressed against my chest.

I gently opened the trapdoor and came out. When I got out, the shop seemed empty. Then, through the window, I saw that Tim was with Olin, trying out a wand, casting small conjuring spells with it, making little colorful flowers pop out of the end of it.

#### Chapter {{chn(5)}}

{{ spotify() }}

<p class="pg">From the perspective of Rohan and Alethea:</p>

<p class="para_first">
Andy, friendly dwarf, asked Rohan, “What do you want to do while you’re here?”.</p>

Rohan replied, “Help folks out a bit here and there. Perhaps create some new spells that’ll be useful and improve lives.”

“That sounds wonderful.” Alethea added, “I’m hoping to do a bit of the same, but I also want to take a look at the political state of affairs on Endor and see if there are any people being oppressed or who need help.”

“The people of Zior might need your help actually...,” said the dwarf quietly, without explaining further.

##### Visiting Zior
{{
places['Zior'] = "a small kingdom that been under the rule of an evil king for about fifty years."
}}
Rohan and Alethea left a few days later. After some travel, they reached a large human settlement in Zior. There was a certain mysterious somber and taciturn feel to it. “This place wasn’t like this a hundred years ago... I wonder what happened,” said Alethea.

There was sickness here too; they saw people coughing. One person was sitting outside shirtless, leaning against a house’s wall, and their skin was covered in rashes or blisters.

Elves were immune to disease and sickness, so they themselves had nothing to worry about. But Rohan and Alethea's hearts went out to these people, and a feeling of sadness coming from empathy washed over them for what the people here were going through.

Alethea whispered, “I have a feeling or sense that tells me that this person knows what’s going on here.”

Rohan walked over to the rash-covered human and asked, “What happened here?” They looked up at her with sadness and said, “The king has ruined our city. We used to be a happy city, well-to-do, full of learning and knowledge, and people traveled from far places to study at the institutions of learning in Zior.”

“What changed?”

##### Philoteras and his lying

{{
chrs['Philoteras'] = "the evil king of Zior. Loosely based on a fairly well-known evil bumbling fool south of the border of Canada, who [has attacked knowledge and truth](https://archive.is/iMCaK) for years. The name Philoteras is of Koine Greek construction, and roughly translates to friend of the monster/beast."
}}
“About fifty years ago, a man named Philoteras was elected our ruler by the narrowest of margins. He lied all the time{#<sup>[c.f.](https://en.wikipedia.org/wiki/False_or_misleading_statements_by_Donald_Trump)</sup>#}, incessantly, about anything and everything. He never cared about the people and just cared about the glory and the power and the trappings of office.”

“How did he get away with all that lying?”

{{
chrs['Therion'] = "the evil dragon that helped Philoteras deceive people. Based on the red dragon in [Revelation 12:3](https://www.biblegateway.com/passage/?search=Revelation+12%3A3&version=NIV), who a few verses later in [Relevation 12:9](https://www.biblegateway.com/passage/?search=Revelation%2012%3A9&version=NIV) is indicated to be a symbolic image for Satan: _\"The great dragon was hurled down—that ancient serpent called the devil, or Satan, who leads the whole world astray. He was hurled to the earth, and his angels with him\"_."
}}
“The red dragon Therion from the Dead Mountains made him a wand that helped him deceive people. He used it to cast a spell over this city that dulled people’s sense of discernment between what is true and what is a lie.”

“What about the people at your places of learning? Were not the teachers and learned people there immune to this spell of deception?”

“Indeed, they were immune to it. Most of them blocked it from themselves. But he lied and lied and convinced people that our places of learning were all about brainwashing people. He called the very people who spoke out against him and his lies liars, even though he was the biggest liar we’d seen in a position of power in over a century. He surrounded himself with evil and obsequious people, and elevated himself so that many deceived people failed to see his wickedness and looked up to him as though he was good.”

“How did he stay on for so long?”

“He canceled elections, and became a king. Many were deceived by his lies, and so he had a cadre of supporters to help him cling on to power as well. He also cut off funding for education, so most of the learned people left Zior. The institutions of learning shuttered, and the people that remained fell deeper into his black hole of lies. Many weak ones in our city fell for his deception spell, and felt like there was nothing wrong, and failed to see the evil and suffering that was before their very eyes. And, also, he threw anyone who resisted or wasn’t sycophantic towards him or didn’t address him as ‘_our dear and beloved king_’ into a gulag in a foreign land, to be tortured. Our people got sick. We became poor.”

“What did he have against education and places of learning?”

“Education at our places of learning taught people to think and discern between truth and lies better, even without magic. In addition, our greatest teachers and learned people fought to counter the evil deception spell he’d cast over our city. But, alas, the dragon’s magic was too strong for us to overcome at the time...”

##### Philoteras and protection spells

“What’s the rash you have?”

“It’s pixie trail fever.”

Pixies gave off these little trails of used-up manna when they did their tiny bits of magic, and these trails were blown around by the wind. When humans or dwarves inhaled them, it got them quite sick. Some even died.

“Didn’t I give you all a spell a hundred years ago that eradicated it?” Alethea piped in.

“Yes, you did. No one had pixie trail fever fifty years ago. But this evil king Philoteras and his friends told people that the spells we cast on our children to make them immune to various diseases were actually hurting them, even though we had a hundred years of evidence of your spells working. And people believed his lies, became deceived, and they stopped casting protection spells on their children. My parents refused to listen to his nonsense, but he threatened to imprison parents who tried to cast protection spells on their children. My parents were adjunct instructors, and hence not that well off, so we could not afford to move like some of our friends.”

##### Therion's hatred

“Who benefits from all this?”

“I don’t know, to be honest. I know that the red dragon that he got the wand of deception from hated humans. In fact, that dragon hated humans, dwarves, elves, and most creatures. I think that dragon just wanted to see us suffer. I think it gets a perverse pleasure or schadenfreude when it sees us getting sick and dying. And that too, from a disease like pixie trail fever, which we had defeated in the past. I’m sure that dragon is laughing in his cave when he thinks about how we’re suffering and dying from pixie trail fever.”

Alethea felt sad when she heard all of this.

#### Chapter {{chn(6)}}

{{ spotify() }}

<p class="pg">From the perspective of Nauriel:</p>

<p class="para_first">
I walked out of the door of Olin’s shop. “We missed you there for a bit!” Olin said warmly, smiling at me cheerfully. I felt really bad that I had stolen from such a nice, genuinely kind man. I glanced at Tim, trying to indicate that it was perhaps time to go. Tim seemed to have gotten the signal, and he told Olin, “I think I’ll need to think it over, chat with my niece, to decide which one to get. Thank you for showing us your wares.” “You’re most welcome,” replied Olin.</p>

We slowly trudged back to the woods climbing up a sloping rocky path. Arlo took the miniature carriage, and carefully placed it on a small patch of forest that was clear of trees. He began casting a spell. Just as the carriage was growing bigger, I heard a loud screeching noise as though from a bird, but I saw no bird anywhere. When I turned around, I saw Olin stepping out of a portal, and he looked angry. “You don’t know what you’ve stolen!” “I’m sorry,” I whispered. “I’m sure these guys put you up to it. That’s the wand of the king of Zior! It’s a wand that was crafted by a dragon. I was working on adding more manna to it. That king didn’t even pay me for it; he just threatened to hurt me and my family if I didn’t modify the wand the way he wanted.”

Tim spoke up and said, “Hey, I’m sorry about that, but we didn’t steal your wand. We did help ourselves to some of your fairy wing dust as we do need to make a living, but we’re not interested in your wands. They’re not as easy to sell. We don’t know anything about this wand. We’re going to be leaving now.” Tim took out a little button-like object and cast it on the ground between us and the carriage, and as soon as it hit the ground, a bubble of light surrounded us and the carriage (but not Olin as he was a bit further away from us), and everything went dark for a few seconds.

I felt around my arms; and I could still feel my arms, but I felt weightless, and felt like a light wind was blowing around me, in the darkness. A few seconds later, we reappeared near the woods, near the little shack where I’d found this gang. “Any idea what he was talking about?” asked Tim. “Nope,” I lied. “That escape token cost me a lot, and I wasn’t expecting to need it to escape from the wand maker.” Arlo added, “Olin’s one of the finest wizards around. I don’t think we had much of a choice.” Tim said, “Well, I think we’ll need to subtract the cost of it from the payout for our new friend here.” “I didn’t do anything wrong,” I protested, knowing that wasn’t entirely true. “Your share would just about cover the cost of our escape token. I’m sorry this job didn’t work out for you, but maybe you can make something on our next job.” “What...,” I mumbled, and slowly started walking back home.

I thought to myself that, well, if anything, even if we couldn’t pay rent, at least I had a fancy new wand to play with.

#### Chapter {{chn(7)}}

{{ spotify() }}

<p class="pg">From the perspective of Rohan and Alethea:</p>

<p class="para_first">
“We should have come down here sooner. We should have kept a closer eye on Zior.” Rohan muttered. “You go and confront the king. I’ll go about breaking this dark veil of deception,” replied Alethea.</p>

Alethea went to a square in the middle of the city. She began to cast a spell. As she was muttering the incantation, some of the king's soldiers approached her, but they fell back as soon as they saw she was an elf. They could sense that she was a powerful elf, even from far away, and they dared not confront her.

First, she broke the old deception spell. Then, she slowly cast a new powerful spell over the city, standing in the middle of the square, for hours, muttering, without even a sip of water.

This new spell she cast would create a blueish light over someone’s mouth when they lied, and a violet light when a lie was repeated.

In less than twenty-four hours, the people of Zior caught on. They figured out that they could now tell when anyone was lying, or even just repeating a lie they had heard but believed.

People began experimenting in front of a mirror by saying the things they’d heard, and seeing if a violet glow appeared in front of their mouths. Many began to realize how much they’d been lied to.

Rohan had magically transported himself to the king’s courtroom. The king wasn’t there. But Rohan found an old genteel-looking man, chained against the side wall, looking quite bruised and with dry clotted wounds. He squinted at him. “Aren’t you Olin..?” “Yes...,” he replied, sounding weak. “The king’s warlocks kidnapped me and tortured me because I lost his precious wand... His wand was stolen from me...”

“Where is the king now?” Rohan asked while casting a spell that healed Olin. He then magically broke his chains. “I don’t know,” replied Olin.

Rohan cast a locating spell, and followed the path it lit up. It led to a door on the second floor of the palace.

He flicked his hand, and the door burst into pieces; and he walked in. The old king Philoteras was lying in bed, half naked and drooling.

The king of Zior was fat, old, decrepit, and borderline senile. Years of lying with no shame had corrupted his mind, to the point that he believed some of his own fabrications, and he could no longer distinguish what was true and what was false himself.

“Your vile and evil actions have cast a stench upon this part of the Endor and great suffering to many,” Rohan said. “What did that red dragon offer you, for the evils you’ve inflicted on the people of this city?”

“Who are you... I don’t know what you’re talking about...,” the king murmured from his bed, as though he was drunk or high on something.

I’ll deal with him later, Rohan thought. He magicked himself back to the square, where Alethea was resting by an old fountain. The old fountain was covered in black grime, because the city government hadn’t cleaned it in years. The king had cut funding to and fired all the people responsible for cleaning public places many years ago, and pocketed the tax money for his own pleasures.

{# todo (more above)

Rohan stood patiently by as Alethea's spirit joined back together

#}

People saw the two elves in the square, and began connecting the dots as to what had just happened. Many people came to them to say thanks. “Thank you for helping us...”

“We should've done this sooner...,” muttered Alethea quietly to Rohan.

The evil king was very angry now.

### Part 2

_[not yet written; to be continued...]_

### References

#### Places
{% for place_name, place_desc in places.items() %}
0. **{{place_name}}**: {{place_desc}}
{% endfor %}

#### Characters
{% for chr_name, chr_desc in chrs.items() %}
0. **{{chr_name}}**: {{chr_desc}}
{% endfor %}
