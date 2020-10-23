'''
Author: Luke Schwaller
Purpose: This code was created as an attempt to find an alternative method to cantor pairing for storage
of complex sequences of interactions in the basketball simulation for MEE 484

'''


import numpy as np
import time

tic = time.perf_counter()
test_array = [1,2,1,3,1,1]

# Array Creation for Validation
length_array = np.random.randint(0,26)
newArray = np.random.randint(0, 5, size=( length_array))
print('Now testing array: ',newArray)
print('Array is of Length: ',length_array)

def encoder(array_enters):
    output = ""
    for i in range(0,len(array_enters)):
        output = output + str(array_enters[i])
    return(output)

def decoder(z):
    j = 0
    num = np.zeros((len(z)))
    for i in range(0,len(z)):
        num[j] = z[i]
        j+=1
    print(num)
z = encoder(newArray)
print( "z is: ",z)
typer_of_z = type(z)
print("z is a: ", typer_of_z)
decoder(z)

toc = time.perf_counter()
print(f"Runtime is:  {toc - tic:0.4f} seconds")