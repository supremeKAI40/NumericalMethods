# Function to calculate f(x) 
def func( x ): 
    return x**2

#Question part
lower_limit = 0   
upper_limit = 2 
h=0.1  

def simpsons( l, u, h ): 
  
    # no. of terms n to be used
    n = ( u - l )/h 
    x = list() 
    fx = list() 
      

    i = 0
    while i<= n: 
        x.append(l + i * h) 
        fx.append(func(x[i])) 
        i += 1
  
    #loop to fit in the simpson's formula 
    res = 0
    i = 0
    while i<= n: 
        if i == 0 or i == n: #if first and last term
            res+= fx[i] 
        elif i % 2 != 0: #if even
            res+= 4 * fx[i] 
        else:           #if odd
            res+= 2 * fx[i] 
        i+= 1
    res = res * (h / 3) 
    return res 
      


print("The value of integration is : %.3f"% simpsons(lower_limit, upper_limit, h)) 
