import math

def f(x):
    return x**3 + x**2 -100

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return -1/(x**2+1)

# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    print('initial guess: %0.6f \n' %(x0))
    print('\n Iteration \t\t x1 \t\t f(x1) \t\t g(x1)\n')
    step = 1
    #going on a loop
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, \t\t %0.6f, \t %0.6f, \t %0.6f' % (step, x1, f(x1),g(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > e

#Check for memory overflow
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

x0 = float(x0)
e = float(e)
N = int(N)

fixedPointIteration(x0,e,N)