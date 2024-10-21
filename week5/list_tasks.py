def directions():
    steps = ["Move Forward", "Move backward", "Turn Left", "Turn Right"]
    return steps

def run_task1():
    steps = directions()
    print(steps)

if __name__ == '__main__':
    run_task1()


def movements():
    path = [("Move Forward", 10), ("Move Backwards", 5), ("Move Left", 3), ("Move Right", 1)]
    return path

def run_task2():
    print("Moving...")
    path = movements()

    for direction, steps in path:
        print(f"{direction} for {steps} steps")

if __name__ == '__main__':
    run_task2()


def menu():
    print("Please select a direction: ")
    steps = directions()

    for index, steps in enumerate(steps):
        print(f"{index}: {steps}")

def run_task3():
    menu()

if __name__ == '__main__':
    run_task3()


def menu_and_input():
    steps = directions()

    print("Please select a direction: ")
    for index, steps in enumerate(steps):
        print(f"{index}: {steps}")

    while True:
        try:
            choice = int(input("Please select the index: "))
            if 0 <= choice < len(steps):
                return steps[choice]
            else:
                print("Please select a valid index.")
        except ValueError:
            print("Please select a valid number.")

def main_task():
    route = []
    print("Working out escape route...")

    for i in range(5):
        direction = menu_and_input()
        route.append(direction)

    print(f"\nEscape route: {route}")

if __name__ == '__main__':
    main_task()
