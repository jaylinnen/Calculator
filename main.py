#Ask the operator what operation they want.
from num2words import num2words

operator = input("Enter an Operator (+,-,*,/): ").strip()

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
    result = round(num1+num2, 2)
    print(f"Result: {result:,.2f}")
    print(f"In words: {num2words(result)}")

elif operator == "-":
    result = round(num1-num2, 2)
    print(f"Result: {result:,.2f}")
    print(f"In words: {num2words(result)}")

elif operator == "*":
    result = round(num1*num2, 2)
    print(f"Result: {result:,.2f}")
    print(f"In words: {num2words(result)}")

elif operator == "/":
    result = round(num1/num2, 2)
    print(f"Result: {result:,.2f}")
    print(f"In words: {num2words(result)}")