#functions 
def Greater_Number():
    a=int(input("Enter no.1: "))
    b=int(input("Enter no.2: "))
    c=int(input("Enter no.3: "))

    if(a>b and a>c):
      print(a,",is greater")

    elif(b>a and b>c):
       print(b,",is greater")

    elif(c>a and c>b):
       print(c,",is greater")
    
Greater_Number()