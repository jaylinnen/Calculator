
operator = input("Enter an Operator (+,-,*,/): ")
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

if operator == '+':
    result = num1 + num2
    print(round(result,  3))
elif operator == '-':
    result = num1 - num2
    print(round(result,  3))
elif operator == '*':
    result = num1 * num2
    print(round(result,  3))
elif operator == '/':
    result = num1 / num2
    print(round(result,  3))
else:
    print(f"{operator} is not a valid operator.")