import math
def fn(x):
	return x*math.exp(x)+math.sin(x)

def derivfn(x):
	return math.exp(x)+x*math.exp(x)+math.cos(x)

def doublederivfn(x):
	return 2*math.exp(x)+x*math.exp(x)-math.sin(x)

x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))


def Newton(x0, e):
    print('\n\n***Chebyshev Method***')
    step = 1
    condition = True
    while condition:
        h=fn(x0)/derivfn(x0)
        m=((fn(x0)**2)*doublederivfn(x0))/2*math.pow(derivfn(x0),3)
        x0=x0-h-m #extension to newton raphson
        print('Iteration-%d, x = %0.6f, fn(x0) = %0.6f & derivative fn(x0)= %0.6f, h= %0.6f, m= %0.6f' % (step, x0, fn(x0),derivfn(x0),h,m))
        step=step + 1
        
        condition = abs(fn(x0)) > e

    print('\n The Root of the above equation is %0.6f'% x0)

Newton(x0,e)
