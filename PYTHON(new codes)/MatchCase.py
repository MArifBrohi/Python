age = int(input("Enter your age: "))

match age:
    case 18:
        print("You are young:")
    case _:
        print("Invalid output")

