print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your Love interest name? \n")

low1 = name1.lower()
low2 = name2.lower()

a = low1 + low2

t = a.count("t")
r = a.count("r")
u = a.count("u")
e = a.count("e")

l = a.count("l")
o = a.count("o")
v = a.count("v")
e = a.count("e")

num1 = t + r + u + e
num2 = l + o + v + e

final_value = str(num1) + str(num2)

x = int(final_value)

if x < 10 or x > 90:
    print(f"Your score is {x} %, you go together like coke and mentos.")
elif x >= 40 and x <= 50:
    print(f"Your score is {x} %, you are alright together.")
else:
    print(f"Your score is {x} %. Sad life")