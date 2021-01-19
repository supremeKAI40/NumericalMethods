x0 = 0
y0 = 0
h = 0.1
x = 1

def y1(x,y):
    return x**2 + y**2

def y2(x,y):
    return 2*x + 2*y*y1(x,y)

def y3(x,y):
    return 2+2*((y1(x,y)**2) + y*y2(x,y))


def y(x0,y0,h):
    return y0 + y1(x0,y0)*h+ y2(x0,y0)*h*h/2 + y3(x0,y0)*h*h*h/6

print("y(0.1) & y(0.2) are:")
print(y(x0,y0,0.1))
print(y(x0,y0,0.2))

#calculate y(x) in steps of 'h'
def calc(x,h):
   xi = x0
   yi = y0
   while(xi<x):
     yi = y(xi,yi,h)   #new initial conditions
     xi = xi + h
   return yi


print("y(1) taking h = 0.1 is:")
print(calc(1,0.1))
print("y(1) taking h = 0.01 is:")
print(calc(1,0.01))
    
    
    




    
