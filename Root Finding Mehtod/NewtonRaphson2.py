import math
def fn(x):
	return x*math.sin(x)+math.cos(x)

def derivfn(x):
	return x*math.cos(x)


x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))


def Newton(x0, e):
    print('\n\n***Implementing Newton Raphson Method***')
    step = 1
    condition = True
    while condition:
        h=fn(x0)/derivfn(x0)
        x0=x0-h
        print('Iteration-%d, x = %0.6f, fn(x0) = %0.6f & derivative fn(x0)= %0.6f, h= %0.6f' % (step, x0, fn(x0),derivfn(x0),h))
        step=step + 1
        
        condition = abs(fn(x0)) > e

    print('\n The Root of the above equation is %0.6f'% x0)

Newton(x0,e)


		