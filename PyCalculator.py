def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Can't be divided by 0."

def calc():
    print("""
█████████████████████████████████████████████████████████████████████████
█▄─▄▄─█▄─█─▄█─▄▄▄─██▀▄─██▄─▄███─▄▄▄─█▄─██─▄█▄─▄████▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀█
██─▄▄▄██▄─▄██─███▀██─▀─███─██▀█─███▀██─██─███─██▀██─▀─████─███─██─██─▄─▄█
▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀""", "Choose a Mathematical Operation", "(+)(-)(*)(/)", sep="\n")

    insertNumber = input("Choose an option: ").lower()

    if insertNumber not in ['+', '-', '*', '/']:
        print("Operation not valid.")
        return

    n1 = int(input("Insert the first Number: "))
    n2 = int(input("Insert the second Number: "))

    if insertNumber == '+':
        print(f"{n1} + {n2} = ", sum(n1, n2))
    elif insertNumber == '-':
        print(f"{n1} - {n2} = ", subtract(n1, n2))
    elif insertNumber == '*':
        print(f"{n1} * {n2} = ", multiply(n1, n2))
    elif insertNumber == '/':
        print(f"{n1} / {n2} = ", divide(n1, n2))

def main():
    while True:
        calc()
        ask = input("Continue Calculating?(Y/N): ")
        if ask.lower() != "Y":
            break

if __name__ == "__main__":
    main()
