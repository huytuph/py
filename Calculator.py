print("\n\n:::: Tu's Calculator ::::\n")

x = float(input("\nEnter a number: "))
while True:
    operator = input("""
>> Select an operation: 
(a) Multiply
(b) Divide
(c) Add 
(d) Subtract
(e) Calculate
>> """)
    if operator == "e":
        print(x)
        restart = input("Start again? [y/n]: ")
        if restart == "y":
            x = float(input("\nEnter a number: "))
            continue
        elif restart == "n":
            print("\n\n\n>> Tu is the Best !! <<\n\n\n")
            break

    y = float(input("\nEnter a number: "))

    if operator == "a":
        x *= y
    elif operator == "b":
        x /= y
    elif operator == "c":
        x += y
    elif operator == "d":
        x -= y