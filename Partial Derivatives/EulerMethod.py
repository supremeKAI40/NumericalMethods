# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def fn(x,y):
    return y-x

#Initial Values
x0= 0
y0=2
#final
b=0.1
#Step Size
h= 0.02

iter= (b-a)/h

def eulerMethod(x0,y0,fn):
    for i in range (0,6):
        print("Iteration: {} \t X: {} \t Y: {:.5f} \t f(x,y): {:.5f}".format(i,x0,y0,fn(x0,y0)))
        y= y0+fn(x0,y0)*h
        y0=y
        x0+=h
        f= fn(x0,y0)
eulerMethod(x0,y0,fn)      