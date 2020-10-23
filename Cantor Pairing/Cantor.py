'''
Author: Luke Schwaller
Purpose: This code is used to calculate if Cantor pairing is a valid method to store complex sequences of numeric data
using a key and the paired integer. It was designed for MEE 484 use. Result is that Cantor pairing created far too long
of integers for our use with modern computer limitations.

'''


import numpy as np
import time

tic = time.perf_counter()
test_array = [1,2,1,3,1,1]

# Array Creation for Validation
length_array = np.random.randint(1,26)
newArray = np.random.randint(0, 5, size=( length_array))
print('Now testing array: ',newArray)
print('Array is of Length: ',length_array)
def encoder(test_array):
    x = np.zeros(len(test_array))
    i = 0
    for i in range(0,len(test_array)):
        x[i] = int(test_array[i] * 5**i)
    z = np.sum(x, dtype=np.int64)
    return(z)

def homebrew(num,lenty):
    i = 0
    array_test = np.zeros(lenty)
    while (num//5) > 0:
        array_test[i] = int(num%5)
        num = num//5
        i+=1
    array_test[i] = int(num%5)
    print(array_test)


z = encoder(newArray)
print( "z is: ",z)
typer_of_z = type(z)
print("z is a: ", typer_of_z)
homebrew(z,length_array)

toc = time.perf_counter()
print(f"Runtime is:  {toc - tic:0.4f} seconds")