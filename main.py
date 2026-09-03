#Ask the operator what operation they want.
operator = input("Enter an Operator (+,-,*,/): ")

if operator not in ('+','-','*','/'):
     print("Invalid Operator")
     exit()

try:
    num1 = float(input("Enter 1st Number: "))
    num2 = float(input("Enter 2nd Number: "))
except ValueError:
     print("Invalid input. Please enter a number.")
     exit()

if operator == "+":
        result = num1 + num2
        print(round(result, 3))

elif operator == "-":
    result = num1 - num2
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

elif operator == "/":
    result = num1/num2
    print(round(result, 3))