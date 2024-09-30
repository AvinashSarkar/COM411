print("Please enter a whole number")
num = int(input())

if num % 2 == 0:
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")

print("Please enter the first number")
num1 = int(input())
print("Please enter the second number")
num2 = int(input())

if num1 > num2:
    print("The second number is the smallest")
elif num2 > num1:
    print("The first number is the smallest")
elif num1 == num2:
    print("Both numbers are equal")

print("Please enter the first number")
no1 = int(input())
print("Please enter the second number")
no2 = int(input())
print("Please enter the third number")
no3 = int(input())

even_count = 0
odd_count = 0

if no1 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if no2 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
if no3 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

print(f"There are {even_count} even numbers and {odd_count} odd numbers.")

