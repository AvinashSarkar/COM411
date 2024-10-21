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
