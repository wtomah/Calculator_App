result = 0
def add(left: float, right: float) -> int: #add function
    result = left + right
    return result

def subtract(left: float, right: float) -> int: #subtract function
    result = left - right
    return result

def multiply(left: float, right: float)-> int: #multiply function
    result = left * right
    return result

def divide(left: float, right: float)-> int: #divide function
    if right == 0:
        return "Undefined"
    else:
        result = left // right
        return result
    
def power(left: float, right: float) -> int:
    result = left ** right
    return result


print("Welcome to the Calculator ")

while True:
    try:
        first = float(input("Enter a number: "))
        second = float(input("Enter another number:" ))
    except ValueError:
        print("Invalid Input. Please enter a number.")
        continue

    operation = input("Select an operation: ")
    if operation == "+": #add operation
        print("Answer: ",add(first, second)) #calls add function

    elif operation == "-": #subtract operation
        print("Answer: ",subtract(first, second)) #calls subtract function

    elif operation == "/": #divide operation
        print("Answer: ",divide(first, second)) #calls divide function

    elif operation == "*": #multiplication operation
        print("Answer: ",multiply(first, second)) #calls multiply function
    elif operation == "^": #power operation
        print("Answer: ",power(first, second)) #calls power function


    else:
        print("Invalid Entry")

