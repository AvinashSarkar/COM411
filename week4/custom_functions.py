def game():
    print("Welcome to the Adventure Game!")

    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to our Adventure!")

    title = input("What is your heroic title? ")
    print(f"You shall be known as {title}!")

    print(f"Farewall, {title} {name}. Your journey awaits!")

if __name__ == "__main__":
    game()