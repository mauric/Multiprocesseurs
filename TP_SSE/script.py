# -*- coding: utf-8 -*-
def my_function(x, y=0):
	a= 5*y + x**2
	return a

def my_function(x, y=0):
	a= 5*y + x**2
	return a

w= my_function(3)
z= my_function(3,1)
y= my_function(y=2, x=3)

print "(w,z,y)=",(w,z,y)

a = 8;
b = 3;
 
print "a = ",a
print "b = ",b
print "a + b =", a+b
 
 
if a > 2 :
	c = 1
	print "a is bigger that 2"
else:
	print "a is smaller or equal to 2"
	c = 2;
print "c = ",c
 
print "a is smaller or equal to 2" ,my_function(2,2)

# Testing Numpy bro

num_tab = numpy.empty(1000,numpy.float32)
num_empty = numpy.zeros(1000,numpy.float32)
num_ones =  numpy.ones(1000,numpy.float32)
num_arrange= numpy.arange(1000, dtype=numpy.float32)






 
