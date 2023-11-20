
# Nesting of List Data type
nest = [1,2,3,[4,5],6,['Airplane']]

print(nest[3])
print(nest[3][1])
print(nest[5])
print(nest[5][0])

#***********************************************

##Dictionary

d = {'Key':'value','Key2':123}

print(d['Key'])
print(d['Key2'])
#nesting dictionary

d1 = {'k1':{'innerkey':[1,2,3]}}
print(d1['k1'])
print(d1['k1']['innerkey'])
print(d1['k1']['innerkey'][2])

# Tuples

t= (1,2,3)
print(t)

# Difference b/w list and tuples is that list are mutable but tuples are immutable
# Mutable means changing the value we can change the value of at index present in the list.

# Set : These are collection of unique elements

#print({1,2,1,2,3,3})
#print(set([1,1,1,2,2,2,3,3,3,4,4,4,5]))

s = {1,2,4}
s.add(5)
print(s)

l1=[12,32,45,[1,2,3,4],23,54,[5,6,7,8]]

print(l1[3])
print(l1[6])
print(l1[3]+l1[6])

l2=[12,23,34,[1,2,3,['Target']]]
print(l2[3][3][0])

#append is function used to copy elements from one list and insert it into another list
l3=[1,2,3,4,5]
out=[]
for num in l3:
    out.append(num)
print(out)

#List Comprehension:
# It is a method used to break down a code into a much smaller and easier way

l4=[num**2 for num in l3] # Give me the num square for the num in list l3
print(l4)