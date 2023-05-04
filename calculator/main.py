import art
print(art.logo)


def calculator(firstNumber, secondNumber, pickOperator):

    if pickOperator == "+":
        return firstNumber + secondNumber
    elif pickOperator == "-":
        return firstNumber - secondNumber
    elif pickOperator == "*":
        return firstNumber * secondNumber
    elif pickOperator == "/":
        return firstNumber / secondNumber


shouldContinue = True
continueWithResult = True
while shouldContinue:
    firstNumber = float(input("What's the first number?: "))
    print("+")
    print("-")
    print("*")
    print("/")
    pickOperator = input("Pick an operator: ")
    secondNumber = float(input("What's the next number?: "))
    result = calculator(firstNumber, secondNumber, pickOperator)
    print(f"{firstNumber} {pickOperator} {secondNumber} = {result}")
    while continueWithResult:
        check = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
        if check == 'y':
            pickOperator = input("Pick an operator: ")
            secondNumber = float(input("What's the next number?: "))
            newResult = calculator(result, secondNumber, pickOperator)
            print(f"{result} {pickOperator} {secondNumber} = {newResult}")
        else:
            continueWithResult = False
            shouldContinue = False
