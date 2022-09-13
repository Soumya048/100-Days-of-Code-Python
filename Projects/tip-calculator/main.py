#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

Total_bill = input("What was the total bill?\n")
Tip = input("How much tip would you like to give? 10, 12, or 15?\n")
Total_person = input("How many people to split the bill?\n")


Bill_with_Tip = float(Total_bill) + (float(Total_bill) * float(Tip) / 100)
Bill_per_person = float(Bill_with_Tip) / int(Total_person)

# return 2 decimal even if it have zero
Bill_per_person = "{:.2f}".format(Bill_per_person)

print(f"Each person should pay: ${Bill_per_person}")