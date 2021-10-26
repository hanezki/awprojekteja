import sys
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul
}

operator = str(sys.argv[1])
number1 = int(sys.argv[2])
number2 = int(sys.argv[3])

print(ops[operator](number1, number2))