#look at powerpoint, anything covered so far is on midterm for multiple choice
#25 multiple choice questions
#can use notes for interview
import numpy as np
grades = np.array([[87,96,70], [100,87,90], [94,77,90], [100,81, 82]])
"""
#rows - grades for each student
#columns - grades for each test

a=grades.sum() #adds up each value of the array together, output one value

b=grades.min()

c=grades.max()

d=grades.mean()

e=grades.std()

f=grades.var()

g=grades.mean(axis=0) #by specifying axis, determine how we want them to be calculated. 
#gives us the mean by test (87, 100, 94, 100), averages by column
#axis 0 --> doing it by column for every row
print('Average of each test', g)

h = grades.mean(axis=1)
#axis 1 --> doing it by row (student)
print('Average of each student', h)

numbers = np.array([1,4,9,16,25,36])
sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1,7)*10
#output - 10, 20, 30, 40, 60
print(numbers)

add = np.add(numbers, numbers2) #same dimensions so works
print(add)

multiply = np.multiply(numbers2, 5)
print(multiply) #multipling each value of array by 5

numbers3 = numbers2.reshape(2,3)#2 dimension
print(numbers3)

numbers4 = np.array([2,4,6])#1 dimension
print(numbers4)

multiply2 = np.multiply(numbers3, numbers4) #this still works even though they're not the same shape
#works because length of each row has same number of columns --> just need columns, if columns don't match then won't work
print(multiply2)


#works because numbers4 has same length as each row of numbers3, so Numpy can apply the multiply operation by treating numbers 4 as if it were the following:
#array(pp2, 4, 6], [2, 4, 6])
"""
#indexing and sliving
grades = np.array([[87,96,70], [100,87,90],
                     [94,77,90], [100,81, 82]])

a = grades[0,1] #number 96
print(a)

b = grades[1]
#output --> array --> ([100, 87, 90])
print(b)

#to select multiple sequential rows
firsttwo = grades[0:2] #does not include upper limit
#first two rows in array
#output --> 
# [[ 87  96  70]
#   [100  87  90]]
print(firsttwo)

grades[[1,3]]
#selects non sequential rows, use list of row indices
#array ([[100,87, 90],
#   [100, 81, 82]])

grades = np.array([[87,96,70], [100,87,90],
                     [94,77,90], [100,81, 82]])

#all rows and only first column
#colon means everything from first element to last element, which we use here for rows because we want all rows
#0 because only want first column
c = grades[:, 0]
#output --> [ 87 100  94 100]
print(c)

#select consecutive columns using a slice:
d = grades[:,1:3] #all rows, columns 1 thrugh 2
print(d)
#[[96 70]
 #[87 90]
 #[77 90]
 #[81 82]]


#or specific columns using a list of column indices:
e = grades[:,[0,2]] #first and third columns,indexes
print(e)
"""
[[ 87  70]
 [100  90]
 [ 94  90]
 [100  82]]
 """

#use numpy random-number generation to create an array of twelve random grades in the range 60 through 100, then reshape the result into a 3-by-4 array
#calculate average of all the grades, the averages of the grades for each test, and the averages of grades for each student

grades = np.random.randint(60,101,12).reshape(3,4) #grades 60 through 100, 12 numbers

print(grades.mean())
 

print(grades.mean(axis = 0)) #by test
 

print(grades.mean(axis=1)) #by student




#shallow copies (view) --> returning view array object that is a view of the original array
#whatever yo do to original is affected to view, and whatever you do to the view affects the original array
#the array method view returns a new array object with a view of the original array

numbers = np.arange(1,6)
#array([1, 2, 3, 4, 5])

numbers2 = numbers.view()
#array ([1, 2, 3, 4, 5])

numbers[1] *= 10

print(numbers2) #change to original array, but affects view as well
#array([1, 20, 3, 4, 5])

numbers2[1] /= 10 #change to view, affects original array numbers, divide by 10
print(numbers)
#array([1, 2, 3, 4, 5])

#slice views
#slices also create views. Let's make numbers2 a slice that views only the first three elements of numbers:

numbers2 = numbers[0:3]
print(numbers2)

#to verify it is a view, lets modify an element in the original array and see the view array
numbers[1] *= 20
print(numbers2)
#array ([1, 40, 3])




#DEEP copies AKA hard copies, an actual copy independent of original
#the array method copy returns a new array object with a deep copy of the original array
numbers = np.arange(1,6)
numbers2 = numbers.copy() #creates new independent array

#to prove that numbers2 has a sepearate copy of the data in numbers, let's modify an element in numbers, then display both arrays
numbers[1] *= 10
print(numbers)
#array([1, 20, 3, 4, 5])

print(numbers2)
#array([1, 2, 3, 4, 5])



#the array methods reshape and resize both enable you to change an array's dimensions
#method reshape returns a view (shallow copy) of the orgiinal array with the new dimensions. It does not modify the original array

grades = np.array([[87, 96, 70], [100, 87, 90]])

a=grades.reshape(1,6) #a is a view of grades
print(a)
#array([[ 87, 96, 70, 100, 87, 90]])
print(grades)

#resize makes permanent change to original array
b = grades.resize (1,6)
print(grades)



grades = np.array([[87, 96, 70], [100, 87, 90]])
#method flatten deep copies into 1 dimensional array the original array's data:
flattened = grades.flatten()

#method ravel produces a veiw (shallow copy) 1 dimension of the original array, which shares the grades of array's data
raveled = grades.ravel()

raveled[0] = 100

raveled[5] = 99

#since its is a view and they share same data, we can look at grades to see that the 6th element has been updated 
print(grades)


grades = np.array([[87, 96, 70], [100, 87, 90]])
#you can quickly transpose an array's rows and columns - that is "flip" the array so the rows become columns, and columns become rows
#the T attribute returns a transposed view (shallow copy) of the array

transposed = grades.T
print(transposed)
#does not permanently change the array

#adding columns, more test scores
#adding rows, more students

#you can combiena rrays by ading more columns or more rows
#known as horizontal stacking and vertical stacking

#HSTACK

grades = np.array([[87, 96, 70], [100, 87, 90]])

grades2 = np.array([[94, 77, 90], [100, 81, 82]])

#can combine grades and grades 2 with Numpys hstack
h_grades = np.hstack((grades, grades2))

print(h_grades)
#old array not affected
print(grades)

#VSTACK
v_grades = np.vstack((grades, grades2))
print(v_grades)

