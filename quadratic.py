# Replace the "ANSWER HERE" for your answer
def roots(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        r1 = (-b + d ** 0.5) / (2 * a)
        r2 = (-b - d ** 0.5) / (2 * a)
        return f"({r1}, {r2})"

    elif d == 0:
        r = -b / (2 * a)
        return f"({r})"

    else:
        return "( )"




def value_y(a, b, c, x):
    y = (a * (x ** 2)) + (b * x) + c
    return y



def to_string(a, b, c):
    if a != 0 and b != 0 and c!= 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b != 0 and c != 0:
        return f"f(x) = {b} * X + {c}"
    elif a == 0 and b == 0 and c != 0:
        return f"f(x) = {c}"
    elif a != 0 and b == 0 and c != 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return ""


def derivation(a, b, c):

    if a > 0 and b < 0 and c > 0:
        return f"f'(x) = 4 * X + {b}"
    elif a == 0 and b > 0 and c < 0:
        return f"f'(x) = {b}"
    elif a == 0 and b == 0 and c > 0:
        return f"f'(x) = 0"
    elif a > 0 and b == 0 and c > 0:
        return f"f'(x) = 4 * X"
    else:
        return ""

def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

    print(roots(num1, num2, num3))
    print(value_y(num1, num2, num3, num4))
    print(to_string(num1, num2, num3))
    print(derivation(num1, num2, num3))

#main()