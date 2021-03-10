## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
a = np.full((4,3),2)
print(a)

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
b = np.arange(0,111,10).reshape(3,4)
print(b) 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
c = b.reshape(4,3)
print(c)

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
d = c * 3
print(d)
"""
## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")
e = (a * b)
## This errored out... why? because first array is 4 row 3 column and second is 3 row 4 columns. Sizes of arrays dont match. Number of rows don't matter, but difference in number of columns does
print(e)
"""
## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")
f = a * c
## this worked! why? Both same rows and columns
print(f)



