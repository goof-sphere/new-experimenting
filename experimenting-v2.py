import random
r = random.randint(1,2)
x = "Daniel"
age = 15
print("My name is " + str(x) + " and my age is " + str(age))
name = input("What is your name?")
if r == 2:
    print(str(name) + " is my name too!")
else:
    print(str(name) + " is such a stupid name like IMAGINE LMAO")
age = input("What is your age?")
r = random.randint(1,2)
if r == 2:
    print(age + " is my age too!")
else:
    print("Well I'm " + str(int(age) + 10) + ", so HAH!")