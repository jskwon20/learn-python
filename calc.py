import sys

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        try:
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What is the next number?: "))
            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

            if choice == "y":
                num1 = answer
            else:
                should_accumulate = False
                print("\n" * 20)
                calculator()
                
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            sys.exit()
        except ValueError:
            print("올바른 숫자를 입력하세요.")
            continue
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")
            continue

calculator()
