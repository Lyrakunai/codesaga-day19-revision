# Q1 Positive/Negative + Even/Odd
num = int(input("Enter number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")




# Q2 Marks Checker
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid input")
elif marks >= 90:
    print("Excellent")
elif marks >= 70:
    print("Good")
elif marks >= 50:
    print("Average")
else:
    print("Fail")




# Q3 Largest of 3 Numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 > n2 and n1 > n3:
    print("Largest:", n1)
elif n2 > n1 and n2 > n3:
    print("Largest:", n2)
else:
    print("Largest:", n3)




# Q4 FizzBuzz
num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)




# Q5 Age Category
age = int(input("Enter age: "))

if age < 0 or age > 120:
    print("Invalid age")
elif age < 18:
    print("Minor")
elif age <= 60:
    print("Adult")
else:
    print("Senior")




# Leap Year Checker
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")




# Last Digit Finder
num = int(input("Enter number: "))
print("Last digit is:", num % 10)