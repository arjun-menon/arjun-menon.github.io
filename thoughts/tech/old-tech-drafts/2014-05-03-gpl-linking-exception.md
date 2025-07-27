---
published: false
---

The GPL in addition to requiring that derivative works (modified programs) be 
released under the same license, also stipulates that any program that links 
with a GPL-licensed program or segment of code, be subject to this same 
constraint.

Let's analyze this bit.

Linking, eh? That's a very C/Unix-based concept.

First of all, "linking" is not necessarily the *only* way to _link_ 
two pieces of code together. Yes, it's the standard way things are 
done on most OSes.

But.


Let's say you wanna use a particular library that you really like, but do 
not want to license your program under the GPL (perhaps you prefer Apache).

Now, whad'ya do?

The GPL can be easily, oh-so-easily circumvented by packagin the turning your 
library into a "service process" -- i.e. a program that runs on it own, not 
linked to any other program; but one that provides a "service", very much 
like any other library.

A good example would libgit2. libgit2 is licensed under "GPLv2 with Linking 
Exception", but let's say it wasn't licensed with the "Linking Exception".
What would we do then? Simply spawn a _git_ process whenever we want a 
git operation done.


We could apply this principle and take all or favorite GPL libraries, package 
them in processes that have _complete_ Unix pipe-based command-line UI, or 
that can be controlled and utilized via some form of 
inter-process communication (IPC).

Now, the big problem with IPC is that it's not *as* efficient as having a 
statically or dynamically linked-togther library. There's a performance 
penalty that comes with it.

But.

#### The Fallacy of IPC inefficiency

Does anybody realize that this "inefficiency" is solely operating system 
dependent 



### The Idea of Linking is OS-specific

Linking, as define in Unix and Windows, does **not** need to exist in 
other operating systems.

Other OSes could could have completely different (or similar) ways of 
accomplishing the same goals -- that might not _necessarily_ be implemented 
technically in the same manner as static/dynamic links (i.e. with a 
shared address space).

To begin with, I *personally* believe sharing your address address space  
with a whole bunch of random libraries is a very Bad Idea(TM).

I don't like shared address spaces, in general. ..more rigour needed!!

### Linking, or "relatedness" is very difficult to cleary _define_

There's really no way to define what constitues a *linked*-togther, 
or related program. It's just plain impossible.

