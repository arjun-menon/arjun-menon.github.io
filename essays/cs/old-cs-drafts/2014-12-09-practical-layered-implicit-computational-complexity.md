




### A Layered Programming Language with Implicit Computational Complexity


mmm



Potential Applications
-----------------------

Programs like Microsoft Word or other office applications, can allow users to 
embed code whose space & time complexity can be statically guaranteed -- and 
also potentially, provide other security guarantees before running it.

Say for example, a legislative body in any country wants to develop a very 
specific XML Schema for their body of law. XSLT affords an oppurtunity to 
transform this to other formats; but having a system where code can be 
statically guaranteed to be "safe", will permit more flexibility, and they're 
not necessarily bounded by XSLT -- they can write a translator specific to 
their particulat needs, and this translator cab be statically guranteed to 
run in reasonable amount of time, using a reasonable amount of space.

The ability for "untrustworthty", anonymous users to embed code wherever they 
want, offers *immense* oppurtunities. Websites and web services could begin to 
grant users much finer control by permitting them to upload arbitary code in
this language, that, by the very nature of the language, is guaranteed to be 
completely, determinstically, and mathematically provably *secure*, and 
guaranteed to use resources that fall within a pre-execution computable bound. 


With such guarantees, a new era of applicaiton might very well be ushered. 
We'll see code flying everywhere -- and the thus so far "feared code", will 
no longer be feared. Static guarantees on security, and space-time 
complexity guarantees offer amazing oppurtunities.


Compare to the goal of [Liquid](http://liquidmarkup.org/) -- a "library 
for rendering safe templates which cannot affect the security of 
the server they are rendered on".


### Super-intelligent Diffs

Let's say you update the ID3 tags on a an MP3 file -- the tag editor, while 
saving the file, can construct an intelligent (O(n)-limited program) that 
describes the programmatically this diff. A filesystem that stores file 
version history, can store this programmatic diff. The diff will have to 
be a _invertible function_.


