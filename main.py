#Ask the operator what operation they want.
operator = input("Enter an Operator (+,-,*,/): ")
#Ask the user for their numbers.
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

#If the operator wants +
if operator == '+':
    #Then add 1st and 2nd number.
    result = num1 + num2
    print(round(result,  3))
#If the operator wants -
elif operator == '-':
    #Then subtract 2nd number from 1st number.
    result = num1 - num2
    print(round(result,  3))
#If the operator wants *
elif operator == '*':
    #Then multiply 1st and 2nd number.
    result = num1 * num2
    print(round(result,  3))
#If the operator wants /
elif operator == '/':
    #Then divide 1st number by 2nd number.
    result = num1 / num2
    print(round(result,  3))
    
else:
    print(f"{operator} is not a valid operator.")