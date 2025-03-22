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


print("Welcome to the Calculator ")

first = int(input("Enter a number: "))

operation = input("Select an operation: ")

second = int(input("Enter another number:" ))



if operation == "+": #add operation
    print("Answer: ",add(first, second)) #calls add function

elif operation == "-": #subtract operation
    print("Answer: ",subtract(first, second)) #calls subtract function

elif operation == "/": #divide operation
    print("Answer: ",divide(first, second)) #calls divide function

elif operation == "*": #multiplication operation
    print("Answer: ",multiply(first, second)) #calls multiply function
else:
    print("Invalid Entry")


