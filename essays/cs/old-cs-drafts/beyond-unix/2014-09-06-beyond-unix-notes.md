Notes on Beyond Unix
====================

A book called "Beyond Unix" -- that explore alternatives to the *Unix UI*.

Beginning by mentioning that I'm talking about the Unix UI, not about operating system internals. I.e. the Unix UI, and the POSIX standard behind it.

I'm exploring alternatives to this UI model

With first describing the Unix user interface at a high-level...
* The file system structure
* The C programming language (cc, cstdlib)
* Process, pipes, IPC
* The Shell
* etc.

Then exploring how all of this could be improved... with both
- (1) looking into existing ideas
- (2) describing *my own ideas*



Study and analyze the good and bad of Unix.

Book & resources:
* [The Art of Unix Programming](http://www.catb.org/~esr/writings/taoup/html/)
* [The Unix-Haters Handbook](http://web.mit.edu/~simsong/www/ugh.pdf)
	*[Comments by ESR](http://esr.ibiblio.org/?p=538)
*[ESR's thoughts on C++](http://esr.ibiblio.org/?p=532)


From http://www.joelonsoftware.com/articles/Biculturalism.html

> "There is one significant group of Windows programmers who are primarily coding for other programmers: the Windows team itself, inside Microsoft. The way they tend to do things is to create an API, callable from the C language, which implements the functionality, and then create GUI applications which call that API. Anything you can do from the Windows user interface can also be accomplished using a programming interface callable from any reasonable programming language. For example, Microsoft Internet Explorer itself is nothing but a tiny 89 KB program which wraps together dozens of very powerful components which are freely available to sophisticated Windows programmers and which are mostly designed to be flexible and powerful. Unfortunately, since programmers do not have access to the source code for those components, they can only be used in ways which were precisely foreseen and allowed for by the component developers at Microsoft, which doesn't always work out. And sometimes there are bugs, usually the fault of the person calling the API, which are difficult or impossible to debug without the source code. The Unix cultural value of visible source code makes it an easier environment to develop for. Any Windows developer will tell you about the time they spent four days tracking down a bug because, say, they thought that the memory size returned by LocalSize would be the same as the memory size they originally requested with LocalAlloc, or some similar bug they could have fixed in ten minutes if they could see the source code of the library. Raymond invents an amusing story to illustrate this which will ring true to anyone who has ever used a library in binary form."

also perhaps refuting Eric S. Raymond's misplaced "silence is golden" 'value' -- which draws a 
wrong picture of unix

