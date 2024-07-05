def last(words):
    result = []
    
    for i in words:
        if i[-2] == " " in i:
            x = "True"
            result.append(x)
        else:
            y = "False"
            result.append(y)
    return result

words = ['ca t', 'car', 'fea r', 'cente r']
print(last(words))
#TEST CASES
#['ca t', 'car', 'fea r', 'cente r']

    