# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

# Display a box
print("Please enter a character for the eye:")
eye_char = input()
print("##########")
print(f"#  {eye_char}  {eye_char}  #")
print("#  ----  #")
print("##########")

# Prompt the user for their name, age, height, and weight
name = input("What is your name?")
age = int(input("How old are you?"))
height = float(input("How tall are you?"))
weight = float(input("How much do you weigh?"))

# Calculate the BMI
bmi = weight / (height ** 2)

# Display the results
print(f"{name}, you are {age} years old and your BMI is {bmi:.2f}.")


