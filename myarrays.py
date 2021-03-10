#import numpy as np
#type REPL in command pallete to make interactive mode
#cannot save it in file
#numpy faster way to create arrays than with lists

import numpy as np
integers = np.array([1,2,3])

print(type(integers))
print(integers)

#ndarray of numpy, it's a numpy array!
#a one diminesional array

#list comprehension
#create one dimensional array that makes even integers from 2 through 20
integers = np.array(x for x in range (2,21,2))
print(integers)

integers = np.array([[1,2,3],[4,5,6]])
#if a two dimensional array, there is an outer list with two lists within, aka two sets of square brackets
#two rows, with the columns each --> two dimensional array
print (integers)

floats = np.array([0.0,0.1,0.2,0.3,0.4])
#1 dimensional array with five elements, floating points
print(floats)

#how to know type 
a=integers.dtype
b=integers.ndim #tells us number of dimensions aka rows
c=integers.shape #returns 2 rows, 3 columns
d=integers.size #total number elements in entire arrow 2x3 = 6 elements

print()
#red dot tells debugger to stop at print statement

for row in integers:
    print(type(row))  #returns numpy.ndarray, a 1 dimensional array
    print(row)
    for column in row:
        print (column, end=' ') #changed default newline character to print out in row
        #print(column)

#for i in integers.flat: #iterates though all values diregarding columns and rows, goes through every single value in array
   # print(i)


#exercise -> create 2D list array of 5 integer elements each using the random module
#and list comprehension print out its dimension, shape, and size
import random

a = np.array([[random.randint(1,10) for x in range (5)],     #first row
                [random.randint(1,10) for x in range(5)]])  #second row
print(a)

#or do this because easier
b = np.array(np.random.randint(1,10, size = (2,5))) #size saying 2 rows, 5 elements in each row
print(b)

c = np.zeros(5) #create an array of 5 elements of zeros (by default float type
print(c)

d = np.ones(5) #create an array of 5 elements of 1s (by default float type)
print(d)

e = (np.ones((2,4), dtype = int)) #create array of 2 by 4 of ones of type int
print(e)

f = np.full((3,5),13) #create an array of 3 row of 5 columns of the number 13
print(f)

g = np.arange(10,1,-2) #goes from 10 to 1 descending by -2 each time
print(g)

h = np.linspace(0.0, 1.0, num=5) #evenly spaced float range by number specified AKA five equally spaced numbers between 0.0 and 1.0
print(h)

array1 = np.arange(1,21) #reshape method can change the dimension --> right now only 1 dimensional array

array2= array1.reshape(4,5) #has to have the same number of elements. makes 4 rows with 5 columns

print(array1)
print(array2)

array3=np.arange(1,100001).reshape(4,25000)
print(array3) #see first 3 columns and last 3 columns, ... in between

array4=np.arange(1,100001).reshape(100,1000) #reshape into 100 rows and 1000 columns
print(array4)

numbers = np.arange(1,6)
numbers += 10 #adds 10 to each value in our array AKA 11,12,13,14,15
print(numbers)


#broadcasting in numpy!!
#can typically only do operations if same size and shape or else get error
print(numbers * 2) #multiple each element by 2, just assumes dimensions are same as original
#numbers * [2, 2, 2, 2, 2]

print(numbers ** 3)
#numbers * [^3, ^3, ^3, ^3, ^3]
print(numbers) #numbers is unchanged by arithmetic operators

numbers2 = np.linspace(1.1,5.5, 5)
a = (numbers * numbers2)
print(a)

#comparing arrays
print(numbers >= 13)
#returns true or false saying which element passes and doesnt pass

print(numbers2 < numbers)
#returns true or false saying which element passes and doesnt pass

print(numbers==numbers2)
#returns true or false saying which element passes and doesnt pass
