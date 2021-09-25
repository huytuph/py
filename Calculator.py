print("\n\n:::: Tu's Calculator ::::\n")

x = float(input("Enter a number: "))
while True:
    operator = str(input("""
>> Select an operation: 
(a) Multiply
(b) Divide
(c) Add 
(d) Subtract
(e) Calculate
>> """))
    if operator == "e":
        print(x)
        break

    y = float(input("Enter a number: "))

    if operator == "a":
        x *= y
    elif operator == "b":
        x /= y
    elif operator == "c":
        x += y
    elif operator == "d":
        x -= y