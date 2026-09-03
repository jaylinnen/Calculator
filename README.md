# Basic Python Calculator

## About the Project

This is a beginner Python calculator that performs basic arithmetic operations using two numbers entered by the user.

The user selects an operator, enters two numbers, and receives a result rounded to three decimal places. The program also detects unsupported operators and nonnumeric inputs.

## Features

* Performs addition
* Performs subtraction
* Performs multiplication
* Performs division
* Accepts whole numbers and decimals
* Rejects unsupported operators
* Handles nonnumeric input without crashing
* Rounds results to three decimal places

## Python Concepts Used

* Variables
* User input
* Strings
* Floating-point numbers
* `if`, `elif`, and `else` statements
* Comparison operators
* Membership operators
* Tuples
* `try` and `except`
* The `round()` function
* Basic arithmetic operators

## Supported Operations

| Operator | Operation      |
| :------: | -------------- |
|    `+`   | Addition       |
|    `-`   | Subtraction    |
|    `*`   | Multiplication |
|    `/`   | Division       |

## How to Run the Program

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run the calculator:

```bash
python3 calculator.py
```

5. Select an operator and enter two numbers when prompted.

## Example

```text
Enter an Operator (+,-,*,/): +
Enter 1st Number: 10
Enter 2nd Number: 5
15.0
```

## Input Validation

The program checks whether the user selected one of the four supported operators. It also uses error handling to prevent nonnumeric entries from crashing the program.

## Future Improvements

* Prevent division by zero
* Allow the user to perform multiple calculations
* Display the complete calculation with the result
* Add exponent and remainder operations
* Organize the calculator using functions
* Create a graphical user interface

## Author

Jason Linnen
Computer Science student interested in cybersecurity
