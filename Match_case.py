# Match is nothing but just like what we use in c and c++ (switch case)
x=int(input("Enter the Number"))
match x:
    case 1:
        print("No! it's False.")
    case 4:
        print("Yes! it's True.")
    case _:
        print(x)


