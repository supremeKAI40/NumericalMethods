import math as m
from functools import reduce

X1 = [0.5,0.6,0.7,0.8,0.9,1.0,1.1]
Y1 = [.4804,0.5669,0.6490,0.7262,0.7985,0.8658,0.9281]
a= 0.5      #limits of integration
b= 1.1      #upper limit
n= len(X1)
Z1 = [0 for x in range(n)]
def f(x,y):
    return x*x*y  #Integration Function

def g(x,y):
    return x*y*y
###
###

def trapezoidal (a, b,f, n): 
      
    # Grid spacing 
    h = X1[1]-X1[0]
    Z1= [f(X1[i],Y1[i]) for i in range (n)]
    # Computing sum of first and last terms 
    s = Z1[0]+Z1[n-1]
  
    # Adding middle terms in above formula 
    for i in range (1,n-1):
        s+=2*Z1[i]
          
    # Multiplying h/2 with s. 
    return ((h / 2) * s)
print("Integral of f(x,y) = x^2*y from x=0.5 to x=1.1 for given data evaluates to-")
print ("Value of integral is ", 
     "%.4f"%trapezoidal(a,b,f,n))

print("Integral of f(x,y) = x*y^2 from x=0.5 to x=1.1 for given data evaluates to-")
print(trapezoidal(a,b,g,n))
