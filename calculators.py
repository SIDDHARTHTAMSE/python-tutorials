def add(num1, num2):
    res = num1 + num2
    print(f"Addition of num1 and num2 is {res}")
    mul(5, 5)
    return res


def sub(num1, num2):
    res = num1 - num2
    print(f"Substraction of num1 and num2 is {res}")
    return res


def mul(num1, num2):
    res = num1 * num2
    print(f"Multiplication of num1 and num2 is {res}")
    sub(20, 10)
    return res


def div(num1, num2):
    res = num1 / num2
    print(f"Division of num1 and num2 is {res}")
    add(10, 20)
    return res


div(10, 5)




