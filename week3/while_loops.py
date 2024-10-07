print("How many apples should I remove?")
apples_to_remove = int(input())

apples_removed = 0

print()

while apples_removed < apples_to_remove:
    print("Removed apple.")
    apples_removed = apples_removed + 1


print("How many obstacles should I avoid?")
obstacles_to_avoid = int(input())

obstacles_avoided = 0

print()

while obstacles_avoided < obstacles_to_avoid:
    print("Avoiding...", end="")
    obstacles_avoided = obstacles_avoided + 1
    print(f"Done! {obstacles_avoided} obstacles avoided.")


print("How many bars should be charged?")
bars_to_charge = int(input())

bars_charged = 0

print()

while bars_charged < bars_to_charge:
    bars_charged = bars_charged + 1
    print(f"Charging: {'█' * bars_to_charge}.")
print("This battery is fully charged.")


print("Please enter a phrase.")
phrase = input()

i = 0

print()

while i < len(phrase):
    print("Hi ", end="")
    i = i + 1


print("Calculating the sum of the first 100 numbers...")

number = 1
total = 0

while number <= 100:
    total = total + number
    number = number + 1

print(f"...Done! The answer is {total}")


print("How many numbers should I sum up?")
numbers_to_sum = int(input())

summed = 0
total = 0

print()

while summed < numbers_to_sum:
    print(f"Please enter number: {summed} of {numbers_to_sum}:")
    number = int(input())
    total = total + number
    summed = summed + 1

print(f"The number is {total}")


print("How many mountains should I display?")
mountains = int(input())

print("Displaying...")

for mountains in range(mountains):
    print(""" 
    __
     / \_
     /^ \
     / ^ \_
     _/ ^ ^ ^\
     / ^ ^ \ 

    """)


print("How far are we from the target?")
distance = int(input())

print()

for count in range(distance, 0, -1):
    print(f"{count} steps remaining")

print("Target achieved!")


print("What level of brightness is required?")
brightness_lvl = int(input())

print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_lvl + 1, 2):
    print(f"Brightness level: {'*' * brightness}")

print("Complete!")