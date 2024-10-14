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


def main():
    print("Program Started!")

    while True:
        try:
            user = int(input("Enter an ASCII code (0-255): "))

            if 0 <= user <= 255:
                character = chr(user)
                print(f"The character represented by the ASCII code {user} is '{character}' ")
                break
            else:

                print("Invalid input. Please enter a number between 0 and 255.")
        except ValueError:

            print("Invalid input. Please enter a valid integer.")

    print("Program Ended.")

if __name__ == "__main__":
    main()