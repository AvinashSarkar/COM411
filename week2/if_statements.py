print("What type of book do you have?")
book = input()

if book == "adventure":
    print("I like adventure books!")
else:
    print("Finished reading book.")

print("Please enter the activity to be performed")
activity = input()

if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")
print("Activity complete!")

print("Towards which direction should i go (up, down, left or right)?")
direction = input()

if direction == "up":
    print("I am moving in an upwards direction!")
elif direction == "down":
    print("I am moving in an downwards direction!")
elif direction == "left":
    print("I am moving in the left direction!")
elif direction == "right":
    print("I am moving in the right direction!")