  #calculator
from logo import logo
#ADD
def add(num1,num2):
    return num1 + num2

#Subtract
def sub(num1,num2):
    return num1 - num2

#Multiply
def mul(num1,num2):
    return num1 * num2

#divide
def div(num1,num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))
    for symble in operations:
        print(symble)
    should_comtinue = True

    while should_comtinue:
        operation_symble = input("Pick an operation:")
        num2 = float(input("What is the next number? "))
        #Dr Angela yu:
        calculate_Function = operations[operation_symble]
        answer = calculate_Function(num1,num2)

        # #My way:
        # if operation_symble == "+":
        #     answer = add(num1,num2)
        # elif operation_symble == "-":
        #     answer = sub(num1,num2)
        # elif operation_symble == "*":
        #     answer = mul(num1,num2)
        # elif operation_symble == "/":
        #     answer = div(num1,num2)

        print(f"{num1} {operation_symble} {num2} = {answer}")

        if input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_comtinue = False
            calculator()

calculator()