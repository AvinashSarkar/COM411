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