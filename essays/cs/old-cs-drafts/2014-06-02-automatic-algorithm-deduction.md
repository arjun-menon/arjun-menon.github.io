


As an example, let's take *sorting*. The programmer should be able to define 
sorting, with the least effort necessary. One way to *define* sorting would 
be to say, there is a list L1, and this list gets transformed to a new list 
L2, in which the successive element is greater than the previous. Here, in 
L2, we simply impose an additional constraint on the ordering of the 
elements – a constraint that didn't exist in L1.

Such a definition is clear and high-level. It is immediately understandable. 
The big challenge now, is to have a system that can automatically with no 
human invovlement, deduce the most efficient sorting algorithm for *a 
given machine*. This brings us to our next point – machine specifications.


A Common "IR" for optimization?


# Connect this with M.S.-based compiler opt.
