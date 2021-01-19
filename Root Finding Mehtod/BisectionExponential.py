import math

def f(x): 
	return 3*x+math.sin(x)-math.exp(x)

x0= float(input('enter first guess: '))
x1= float(input('enter second guess: '))
question=float(input ('question number: '))

error= 0.0001

def bisection(x0,x1,x2):
	step=1
	print('\n\n solution to question %0.2f \n****Bisection Method Implementing***\n'%(question))
	print('\n Iteration \t a \t\t b \t\t xn \t\tf(a)\t\tf(b)\t\t f(xn)\n')
	condition= True
	while condition :
		x2= (x0+x1)/2
		print('Iteration -%d, \t %0.6f, \t %0.6f, \t %0.6f,\t%0.6f, \t%0.6f, \t %0.6f' % (step,x0,x1,x2,f(x0),f(x1),f(x2)))
		i=f(x0)/f(x2)
		if i<0:
			x1=x2
		else:
			x0=x2	

		step+=1	
		condition = abs(f(x2))>error
	print('\nRequired root is : %0.8f' % x2)

if f(x0)/f(x1)>0:
	print("The guess value don't bracket a root")
else:
	bisection(x0,x1,error)