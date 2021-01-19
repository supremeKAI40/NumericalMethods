import numpy as np 

#Data table defined in code

n = 5; 
     
y = [[0 for i in range(10)] 
		for j in range(10)];  
x = [ 1, 2, 3, 4, 5 ]; 
#table where y[][0] is used for input 
y[0][0] = 1; 
y[1][0] = 4; 
y[2][0] = 9; 
y[3][0] = 16; 
y[4][0] = 25;


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


        
print('\nFORWARD DIFFERENCE TABLE\n');

for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, n-i-1):
        print('\t\t%0.2f' %(y[i][j]), end='')
    print()