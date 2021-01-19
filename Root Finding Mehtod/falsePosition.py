def fn(x):
	return x**3+x**2-100

a = float(input('Enter Guess Value 1: '))
b = float(input('Enter Guess Value 2: '))
e = float(input('Tolerable Error: '))


def falsePosition(a,b,e):
    print('\n\n***Implementing False Position Method***')
    print('\n Iteration \t a \t\t b \t\t c \t\t f(c)\n')
    step = 1
    condition = True
    while condition:
        c = a - (b-a) * fn(a)/( fn(b) - fn(a) )
        print('Iteration-%d, \t%0.6f, \t%0.6f, \t%0.6f, \t%0.6f ' % (step, a, b, c, fn(c)))

        if fn(a) * fn(c) < 0:   #like bisection
            b = c
        else:
            a = c
        
        step=step + 1 
        condition = abs(fn(c)) > e

    print('\n The Root of the above equation is %0.8f'% c)      #c is the solution

if fn(a)*fn(b)>0:
    print("Invalid Guess \n Enter other Guess Value")
else:
    falsePosition(a,b,e)


		