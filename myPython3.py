#Welcome to the tip calculator!
#Data Types

"""

print(11+2)
print(100-1)
print(5*11)
print(99/9)


#int  = 100
#float = 100.20
#string  = "Hi!"
#boolean = True


print("Welcome to the tip Calculator! :)")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)



print("Welcome to the tip Calculator! :)")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount  = round(bill_per_person, 2)
final_amount  = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

"""


print(len("Salom"))
#In programming, the count starts from 0
print("Hello" [0])
print("Hello" [1])
print("Hello" [2])
print("Hello" [3])
print("Hello" [4])
# print("Hello" [5]) ---> this is error because the counter starts from 0 in data

#String
print("123" + "456")
"Hello"[3]

#Integer
print(123 + 456)

#Float
3.14159

#Boolean
True
False

num_char = str(len(input("What is your name? ")))
print("Your name has " + num_char + " characters.")


"""

num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

"""

a = str(123)
print(type(a))

a = (70 + float("100.5"))
print(a)
print(type(a))


two_digit_number = input("Enter a 2-digit number... :) ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print(first_digit)
print(second_digit)

a = float(123)
print(type(a))

print(str(70) + str(100))

3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

"""
PEMDASLR
()
*
**
/
+
-
"""
print(type(3 * 3 + 3 / 3 - 3))

height = input("...enter your height in m: ")
weight = input("...enter your weight in kg: ")
bmi = float(weight) / float(height) ** 2
print(bmi)


print(int(7.4 / 2))
print(int(8 / 3))
print(8 / 3)
print(round(8 / 3))
print(round(8 / 3, 2))
print(round(8 / 3, 3))

print(8 // 3)


score = 0 
#User scores a point
score += 1
print(score)


score = 23
#User scores a point
score -= 1
print(score)


score = 23
#User scores a point
score *= 2
print(score)


score = 0
print("Your score is: " + str(score))

#This is error ---> print("Your score is:" + score)

score = 0
height = 1.85
isWinning = True

#f-String
print(f"your score is: {score} and Your height is: {height} and you are winning: {isWinning}")


age = input("What is your current age? ")
age = int(age)
years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_reamining  = years_remaining * 52
months_remaining  = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_reamining} weeks, and {months_remaining} months left."

print(message)








