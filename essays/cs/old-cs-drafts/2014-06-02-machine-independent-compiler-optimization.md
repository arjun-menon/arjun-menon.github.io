



### Machine Specification

Before we can think about generating efficient implementations, it is 
necessary to know what kind of machine we are generating an implementation 
for; or in other words, to know what sorts of constraints we are operating 
under with regard to the final auto-generated program.

A *machine specification* is a description of a machine. It describes 


Cache-locality





the need for an intermediate represenation, from which this *compiler* can 
produced MS-based optimized code.

this repr will have to be highly abstract in order for MS-based optimization 
to be easier.




On a lower level, data representation
