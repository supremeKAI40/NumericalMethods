# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (-4+2*y-z)/5
f2 = lambda x,y,z: (-1-x+2*z)/6
f3 = lambda x,y,z: (13-3*x+y)/5

# Initial setup
x0 = 0.0
y0 = 0.0
z0 = 0.0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Jacobi Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('%d\t%0.6f\t%0.6f\t%0.6f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x=%0.4f, y=%0.4f and z = %0.4f\n'% (x1,y1,z1))