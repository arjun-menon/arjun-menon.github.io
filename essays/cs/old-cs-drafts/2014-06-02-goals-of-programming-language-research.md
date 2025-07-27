

Before I explain my ideas, I think it would be helpful if I shared my thoughts 
and opinions on what the *goals of programming language research* are. In many 
ways they are foundational to my ideas, and my ideas are motivated by these 
goals. I believe the three *broad* goals of programming language research are:

- **Reduction of Human Effort:** The whole purpose of programming is to 
  communicate our intent to a computer in a clear and unambiguous manner. It is 
  essentially, a medium of communication. (Not only to the computer, but also 
  to other programmers who might be reading your code.) Our goal with regard to 
  *effort*, must be to **reduce** the amount of effort a human has to exert in 
  order to communicate his intent to a machine. The effort required, must 
  be *minimized*.

- **Clarity:** Our programs are not for the computer alone to read. Almost 
  every single significant human endevour has been a result of joint-effort and 
  required collaboration. Our programs therefore, are for other humans to read 
  as well. As such, *clarity* becomes a major goal.

  The importance of clarity cannot be understated. Code that is understandable 
  to others will be understandable to us also. We ourselves are the greatest 
  readers of our code. Clarity is also possibly the best panacea for bugs. 
  Clear code, being more understandable, naturally makes bugs more visible. 

  A fuzzy measure of clarity would be: how quickly can others grasp the 
  *intent* of our program, by looking at it? Furthermore, how clearly are the 
  *miniscule* details of our program, that often get buried and become 
  a source of pain, presented? 

  Clarity and *success* in our software design can be achieved at two levels. 
  The first level is architectural design – how the components of a system 
  are organized, and how they interact with each other. Tightly coupled 
  spaghetti code can lead to completely unmaintainable and buggy systems.
  Good architecture is paramount. In their hierarchy of software development, 
  everything else fades into obscurity in comparison to it. 

  *Code clarity* however pertains to how each of the individual components of 
  our system are specified (i.e. programmed), and how clear *their 
  specification is*. Code clarity can, in and of itself, be a tool that 
  allows for better architectural design. Code clarity and architectural 
  design are not as separated from each other as one might be lead to believe. 
  In particular, programming paradigms can enable us *architect our code 
  better*. (Object-oriented programming is one, rather controversial 
  example of this.) 

  (To reword: The focus here will be to develop methods of expressing programs 
  while keeping the big picture in mind – i.e. to do programming language 
  research while always thinking of how this can 
  lead to better-architected code.)

- **Efficiency:** The final goal of programming language design is 
  maximizing efficiency with least programmer *effort*, while 
  maintaining maximal *clarity*.

  Efficiency seems to have an *inverse relationship* with clarity and effort. 
  Less effort (for example, a naive easy-to-write algorithm) generally results 
  in an *inefficient program*. In a similar vein, today, heavily optimized 
  code is usually hard-to-understand and *not clear*.

### The Dream

The ultimate goal is to have a system where we can specify programs at 
a *very high-level*, with maximal clarity, and minimal programmer 
effort – while at the same time generate highly efficient code.

