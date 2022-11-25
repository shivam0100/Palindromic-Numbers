def calculate():
    number = []
    for i in range(100, 1000):
        if str(i) == str(i)[::-1]:
            number.append(i)
    return len(number)
print(calculate())

