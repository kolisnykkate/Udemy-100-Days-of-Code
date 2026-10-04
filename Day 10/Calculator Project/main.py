from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def operation_next_number():
    operation = input("+\n-\n*\n/\nPick an operation: ")
    n2 = int(input("What's the next number: "))
    return operation, n2

def calculate(n1, operation, n2):
    for key in calc_dict:
        if operation == key:
            result = calc_dict[key](n1, n2)
            print(result)
            return result

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


restart = True

while restart:
    result = 0
    n1 = int(input("What's the first number: "))

    continue_calculating = True
    while continue_calculating:

        operation, n2 = operation_next_number()

        result = calculate(n1, operation, n2)

        should_continue = input(f"Type 'y' to continue calculating with {result}, "
                                f"or type 'n' to start a new calculation. To exit type 'exit': "
                                ).lower().strip()

        if should_continue == "y":
            n1 = result
            continue_calculating = True

        if should_continue == "n":
            continue_calculating = False
            restart = True

        if should_continue == "exit":
            continue_calculating = False
            restart = False




