a, b, x = map(int, input().split())


def f(a, x):
    if a == -1:
        return 0
    return int(a // x) + 1


print(f(b, x) - f(a - 1, x))
