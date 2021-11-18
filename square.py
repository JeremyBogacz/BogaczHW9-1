# Created by Jeremy Bogacz on 11/17/2021

# This program computes the square of all 
# numbers from 0 to 19 and prints them out.
# The squaring is done by the function sq().

def sq(x):
    y = x*x
    return y

for i in range(20):
    z = sq(i)
    print z
