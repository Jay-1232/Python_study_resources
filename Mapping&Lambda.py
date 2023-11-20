# Map function in Python
# The map() function executes a specified function for each item in an iterable. 
# The item is sent to the function as a parameter.

def times3(var):
    return var*3

output=times3(4)
print(output)

list1=[1,2,3,4,5]
list2=list(map(times3,list1))
print(list2)

def Greeting(name):
    print("Hello",name)

Greeting("Jay")

s1={"Raj","Sanjay","Ishita"}

print(set(map(Greeting,s1)))

# for x in range(0,4):
#     print(x)

#Lambda Expression
l = lambda x: x**2
print(l(2),l(3),l(4))

l4=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x**2,l4)))

#Filter
l1=list(filter(lambda y: y%3==0,l4))
l2=list(filter(lambda y: y%3!=0,l4))
print(l1)