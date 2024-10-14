def main():
    print("Program Started!")

while True:
    char = input("Please enter a standard character: ")

    if len(char) == 1 and char.isalpha():
        ascii_value = ord(char)
        print(f"The ASCII value of '{char}' is {ascii_value} ")
        break
    else:
        print("Invalid input. Please enter a standard character.")

print("Program Ended.")

if __name__ == "__main__":
    main()