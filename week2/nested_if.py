print("Where should I look?")
place = input()

if place == "in the bedroom":
    sub_place = input("Where in the bedroom should I look?")
    if sub_place == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone")

elif place == "in the bathroom":
    sub_place = input("Where in the bathroom should I look?")
    if sub_place == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone")

elif place == "in the living room":
    sub_place = input("Where in the living room should I look?")
    if sub_place == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone")

else:
    print("I dont know where that is but I will keep looking!")

