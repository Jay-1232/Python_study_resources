import time
timestramp = time.strftime("%H:%M:%S")
print(timestramp)
hours = int(time.strftime("%H"))
print(hours)
minute = int(time.strftime("%M"))
print(minute)
timestramp = int(time.strftime("%M"))
print(timestramp)

# hours=int(input("Enter the Hour:"))
# minute=int(input("Enter the Minutes:"))

if(hours<=11 and minute<=59):
    print("Good Morning")

elif(hours>11 and hours<16):
    print("Good AfterNoon")

elif(hours>=16 and hours<=23 and minute<=59):
    print("Good Evening")