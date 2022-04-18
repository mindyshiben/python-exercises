# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend


day = input("what is the day today?")
if day.casefold()== "monday":
    print("It's Monday. Have a great week!")
if day.casefold() != "monday":
    print("Just fyi, it's not Monday")

# create variables and make up values for the number of hours worked in one week, the hourly rate, how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = 55
hourly_rate = 50
weekly_pay = hours_worked * hourly_rate

if hours_worked > 40:
    print(hours_worked * (hourly_rate * 1.5))
if hours_worked <= 40:
    print(hours_worked * hourly_rate)

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
        i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
# Alter your loop to count backwards by 5's from 100 to -10.
# Create a while loop that starts at 2, and displays the number squared on each line while the number 


i = 0
while i <=100:
    print(i)
    i += 2

i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i < 1000000:
    print(i)
    i **= 2

# Write a loop that uses print to create the output shown below

i = 100
while i >=5:
    print(i)
    i -= 5

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = int(input("Type a number:"))
for num in range(1, 11):
    print(f"{num} * {number} = {num * number}")

#Create a for loop that uses print to create the output shown below.

print() 
for num in range(1, 10):
    print(f"{num}" * num)

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)


# Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.


value = int(input("Enter an integer:"))
print(int(value), int(value **2) , int(value ** 3))
cont = input("Would you like to continue? yes or no?")
if cont == "yes":
    up_to = input("what number would you like to go up to?")
    for value in range(1, int(up_to) +1):
        print (int(value), int(value **2) , int(value ** 3))