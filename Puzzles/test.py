
def get_odd(test):
    output = []
    for i, value in enumerate(test):
        if i % 2 == 1:
            output.append(value)
    return output
           




test = ['a','b','c','d']

print(get_odd(test))