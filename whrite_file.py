def check_symbol():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha = alpha + alpha.upper()

    def inner():
        print(alpha)
    return inner


q = check_symbol()
print(q())
