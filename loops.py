# i=0

# while(i<=34):
#     i=int(input("Enter the number"))
#     print(i)

# print("done")

for i in range(0,4):
    for j in range(0,4):
        if(i==j or i<=j):
            print("*", end=" ")
    print("")


for i in range(0,4):
    for j in range(0,4):
        if(i==j or i>=j):
            print("*", end=" ")
    print("")

# output for above code: 
# * * * *
# * * *
# * *
# *
# *
# * *
# * * *
# * * * *

# Implementation of while loop
i=1
while(i<9):
    print(i, end=" ")
    i=i+1
else:
    print("I'm out of the loop.")

# output: 
# 1 2 3 4 5 6 7 8 I'm out of the loop.