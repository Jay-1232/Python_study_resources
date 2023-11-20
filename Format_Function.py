#format function
# age=int(input("Enter the age:"))
# name=str(input("Enter the name:"))
# print("My name is {} and my age is {}.".format(name,age))

# Method 2

def Personal_Detail(name,place,course,branch):
    print('''Hello Everyone! My name is {one} and I am from {two}.I'm currently pursuing my {three} in {four}.The {two} is also known as 'The City of Lakes', is famous for it's beautiful lakes, ponds and the natural beauty.'''.format(one=name,two=place,three=course,four=branch))

Personal_Detail("Jay Sahu","Bhopal","Bachelors of Technology degree","Computer Science Engineering specialization in Data Science")