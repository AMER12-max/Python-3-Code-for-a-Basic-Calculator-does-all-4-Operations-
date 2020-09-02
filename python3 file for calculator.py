# Python 3 Code for Basic Calculator (Does all 4 Operations)

num1 = float(input("Type in your first number: "))
num2 = float(input("Type in your second number: "))
operator = input("Type in your Operator: ")

if operator == "+" or operator == "addition" or operator == "Addition":
    numb1 = num1 + num2
    print("Here is your answer added: " + str(numb1))
elif operator == "-" or operator == "subtraction" or operator == "Subtraction":
    numb2 = num1 - num2
    print("Here is your answer subtracted: " + str(numb2))
elif operator == "/" or operator == "division" or operator == "Division":
    numb3 = num1 / num2
    print("Here is your answer divided: " + str(numb3))
elif operator == "*" or operator == "multiplication" or operator == "Multiplication":
    numb4 = num1 * num2
    print("Here is your answer multiplied: " + str(numb4))
else:
    print("Invalid Operation")
