def summa(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        raise TypeError("Type error raised!!!")


def jako(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        raise ZeroDivisionError("You can't divide by zero!!!")
    except TypeError:
        raise TypeError("Type error raised!!!")


def kerto(num1, num2):
    try:
        return num1 * num2
    except TypeError:
        raise TypeError("Type error raised!!!")


def miinus(num1, num2):
    try:
        return num1 - num2
    except TypeError:
        raise TypeError("Type error raised!!!")


