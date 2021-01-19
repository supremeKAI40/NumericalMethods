import numpy as np 
import math

#Data table defined in code

n = 7; 
sum=0;
index=0;
y = [[0 for i in range(10)] 
		for j in range(10)];  
x = [0, 1, 2, 3, 4, 5, 6]; 
#table where y[][0] is used for input 
y[0][0] = 0; 
y[1][0] = 1; 
y[2][0] = 4; 
y[3][0] = 9; 
y[4][0] = 16;
y[5][0] = 25;
y[6][0] = 36;

xp= 2;


"""Taking input from the user about the data table"""
"""n = int(input('Enter number of data points: '))
 
# to store x an y values
x = np.zeros((n))
y = np.zeros((n,n))


# Reading them using 2 for loops

print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))"""
    


# Generating table using nested loop
for i in range(1,n):
    for j in range(0,len(x)-1):
        y[j][i] = y[j+1][i-1] - y[j][i-1]		#forward table 

'''for k in range(7):
	if ((xp-x[k])<0.0001):
		index=k
		break'''

print('\nFORWARD DIFFERENCE TABLE\n');

for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, n-i-1):
        print('\t\t%0.2f' %(y[i][j]), end='')
    print()


h = x[1] - x[0]
sign=1
for i in range(1,n-index):
	t=math.pow(-1,i+1)*y[i][index]/i
	sum= sum+ t

deriv= sum/h

print("First derivative at x = %0.2f is %0.2f"%(xp, deriv))