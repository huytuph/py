print("\n\n:::: Tu's Calculator ::::\n")

x = float(input("\nEnter a number: "))
while True:
    operator = input(">> Select an operation [* / + - =]: ")
    if operator == "=":
        print(x)
        restart = input("Start again? [y/n]: ")
        if restart == "y":
            x = float(input("\nEnter a number: "))
            continue
        elif restart == "n":
            print("\n\n\n>> Tu is the Best !! <<\n\n\n")
            break
    y = float(input("\nEnter a number: "))
    if operator == "*":
        x *= y
    elif operator == "/":
        x /= y
    elif operator == "+":
        x += y
    elif operator == "-":
        x -= y