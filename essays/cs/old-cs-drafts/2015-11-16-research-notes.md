Research Notes


for the essays on your mutli-level language idea, see:
  [LANGSEC: Language-theoretic Security](http://langsec.org/)


"OS Ideas" (or "Beyond Unix") could be a blog -- you could publish chapters/posts over time, slowly.


Modularity & Reusability
------------------------
Everyone knows that **modularity** (cojointly with **reusability**) is the 
essence to the success of large software projects. However, not everyone knows 
quite how this modularity should be implemented. A few examples:

    * The Unix Approach

      In the (AT&T video on the UNIX Operating System)[link_to_YouTube], it is 
      mentioned that the key killer feature of Unix that made it a success was 
      _pipelining_. I.e., programmers could now accomplish complex tasks easily 
      by composing programs from a vast existing set of light-weight 
      single-function _small_ Unix utilities.

      Observations on this Approach

        * Input and output is just a stream of bytes. It has no type. It is not 
        required to have any structure, or to be bound to any particular syntax. 
        It is usually plain text, but does not have to be so.

        Finally, pipelining operates on input and output _streams_. For `A | B`, 
        B can start processing the A's input before A has completely produced 
        all of its output. This is slightly reminiscent of superscalar pipelining 
        in modern microprocessors. It allows for some parallelism, especially when 
        large datasets are involved.
      
      - Another kind of stdin (besides string streams) would be JSON, or perhaps, 
      a JSON stream. Would have figure out how that works though. Again, a 
      drawback/issue with this is that JSON doesn't support functions/callbacks/hooks/etc.

    * Function calls in traditional programming languages

    Unlike Unix, which operates on _streams_ and where parallel processing is 
    possible, when functions in traditional programming languages are _composed_ 
    they expect a complete data unit for input before beginning processing. For 
    example, in `f(g(x))`, `f` does not start executing until `g` has finished.


    * C libraries
    * Java 


Haskell Video

    "Compositionality is the way control complexity."


See:
    http://xuanji.appspot.com/isicp/4-0-metalinguistic-abstraction.html


from pypage's readme:
    One more thing about secure templating languages like Liquid_: These languages are usually provide 
    a limited set of domain-speific functions, and the language constructs are limited in such a manner 
    that the template can be processed in an approximately linear amount of time. They are 
    non-Turing-complete languages with an implicit time complexity bound and guaranteed termination. 
    What I'd like to point out is that there's a whole area of research on this topic, called *Implicit 
    Computational Complexity*. While this field hasn't recieved much attention in recent years, I 
    believe there is a lot of value in looking into it and researching it more. 

    Perhaps eventually we'll be able to statically specify that a function must fall within an implicit 
    computational bound, and the compiler will be able to guarantee that. We'd be able to extract a lot 
    more assertions about our code *statically*, if were able to accomplish this (perhaps).



Thoughts on certain Blog Posts
------------------------------

 * On [We need less powerful languages](http://lukeplant.me.uk/blog/posts/less-powerful-languages/)
     Saw this via [HN](https://news.ycombinator.com/item?id=10567408)

     I think this guy is confusing complexity with expressives.
     Scala is complex (and expressive).
     But a language doesn't have to be complex in order to be expressive.
     ... explain why/how ...


