# Created by Jeremy Bogacz on 11/17/2021

# This program computes the cube of odd 
# numbers from 0 to 19 and prints out the
# even numbers as well as the cube odd
# numbers. The cubing is done by the 
# cb() function.

def cb(x):
    y = x*x*x
    return y

for i in range(20):
    z = i

    if i%2 == 1:
        z = cb(i)

    print z
        
