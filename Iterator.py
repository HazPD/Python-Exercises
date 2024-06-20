#Make a function that iterates odd numbers
def odd_generator():
    n1 = 1
    n2 = 3
    while True:
        yield n1
        n1, n2 = n2, n1 + 2

odd= odd_generator()
print(next(odd))
print(next(odd))
print(next(odd))
