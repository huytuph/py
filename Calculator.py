# Multiplication
def a(num1,num2):
    print(f"\n{num1} * {num2} = {num1 * num2}")
# Division
def b(num1,num2):
    print(f"\n{num1} / {num2} = {num1 / num2}")
# Addition
def c(num1,num2):
    print(f"\n{num1} + {num2} = {num1 + num2}")
# Subtraction
def d(num1,num2):
    print(f"\n{num1} - {num2} = {num1 - num2}")

print("\n\n:::: Tu's Calculator ::::")

restart = 1
while restart == 1:
    num1 = float(input("\n>> Enter a number: "))

    operator = str(input("""
>> Select an operation: 
(a) Multiplication 
(b) Divsion 
(c) Addition 
(d) Subtraction 
: """))

    num2 = float(input("\n>> Enter another number: "))

    if operator == "a":
        a(num1,num2)
    elif operator == "b":
	    b(num1,num2)
    elif operator == "c":
        c(num1,num2)
    elif operator == "d":
        d(num1,num2)
    else:
	    print("\n>> Error: sum ting wong!!\n>> please try again.")

    restart = input("\nStart Again? [y/n]: ")
    if restart == "y":
        restart = 1
    elif restart == "n":
        break