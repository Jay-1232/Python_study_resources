#Program for set and tuples 
# Set and Tuples are the data types used to store multiple value.
# Set is a type of data type in python which is basically a collection of unique elements . It is represented by {}.
# Tuples on the other hand are the type of data type used to store multiple and is immutable
# which means the values once assigned can not be changed.

print(type({12,23,44}))#output: <class 'set'>
print(type((1,2,3,4))) #output: <class 'tuple'>

s = {12,12,33,43,1,2,1,2,3}
print(s)
s.add(6)
print(s)

t=(1,2,3,34)
print(t)
print(t[0],t[1],t[2],t[3])

s1 = 'Hii'=='Bye'
print(s1)

