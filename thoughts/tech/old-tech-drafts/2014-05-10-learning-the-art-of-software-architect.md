---
title: Getting to be better at software architecture
published: false
---


My suggestion for learning software architecture is to practice. Obviously you can't practice it by doing hundreds of projects, because each one of them takes too long, but you can easily design a hundred architectures for problems which only exist on paper, and where you strive to just get the solution to work on paper. Start by modifying the requirements of a problem you're working on. What if the amount of bandwidth or CPU was a hundredth what it currently is? What if it were a thousand times? A million? What if you had a thousand times as much data? A million? A billion? What if the users were untrusted and you had to either prevent them from damaging the system or have a means of fixing things when they did? It doesn't matter if these scenarios are totally unrealistic, what matters is that they're different and that when you try to find architectures for handling them you take the inputs just as seriously as if you were about to start writing a system with those requirements for work. Try to find as many different approaches as you can, and come up with scenarios in which the stranger ones would be better.

Learning these skills takes time, but is definitely worth it. I couldn't have come up with Codeville's architecture without first having spent a lot of time working on voting algorithms. Not that voting algorithms have anything to do with version control, but the process of coming up with example scenarios and defining the behavior which should happen in each of them carries over very well.

https://bramcohen.livejournal.com/4563.html

---

The idea of designing systems on paper is rather interesting...

http://aosabook.org/en/index.html

