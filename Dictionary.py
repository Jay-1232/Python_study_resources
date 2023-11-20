# WAP to use the dictionary and it's Methods

d1 = {"k1":"Jay", "k2":"Adesh","k3":"Nadir"}
print(d1)
print(d1["k1"])
print(d1["k2"])

x = d1.keys() #Returns the keys of the dictionary
print(x)
print(type(d1))

d1.update({"k1":"Priyanka"}) # Use to update the present value of dictionary
print(d1)

# pop() : It removes the specified element 
d1.pop("k1")
print(d1)

d2 = d1.copy()
print(d2)

# Printing dictionary using for loop
print("The keys and values of dictionary d1 is:", end="\n")
for element in d1:
    print(element,d1[element])

# Nested Dictionary
d3 = {"k1":{"k'1":212,"k'2":213},"k2":{"k'3":214,"k'4":215}}
print(d3)
print(d3["k1"]["k'1"])
print(d3["k1"]["k'2"])
print(d3["k2"]["k'3"])
print(d3["k2"]["k'4"])

# clear(): Use to clear dictionary
d1.clear()
print(d1)

# del() : Use to delete the whole dictionary
del(d1)
print(d1)

