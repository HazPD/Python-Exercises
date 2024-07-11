#Write a Python program to find strings that, when case is flipped, give a target where vowels are replaced by characters two later.
def flip(strings):
    x = {'a': 'C', 
         'b': 'D', 
         'c': 'E', 
         'd': 'F', 
         'e': 'G', 
         'f':'H',
         'g':'I',
         'h':'j',
         'i':'K',
         'j':'L',
         'k':'M',
         'l':'N',
         'm':'O',
         'n':'P',
         'o':'Q',
         'p':'R',
         'q':'S',
         'r':'T',
         's':'U',
         't':'V',
         'u':'W',
         'v':'X',
         'w':'Y',
         'x':'Z',
         'y':'A',
         'z':'B',
         'A':'c',
         'B':'d',
         'C':'e',
         'D':'f',
         'E':'g',
         'F':'h',
         'G':'i',
         'H':'j',
         'I':'k',
         'J':'l',
         'K':'m',
         'L':'n',
         'M':'o',
         'N':'p',
         'O':'q',
         'P':'r',
         'Q':'s',
         'R':'t',
         'S':'u',
         'T':'v',
         'U':'w',
         'V':'x',
         'W':'y',
         'X':'z',
         'Y':'a',
         'Z':'b'
         }

    vowels =['A','E','I','O','U','a','e','i','o','u']
    result = []
    for i in strings:
        if i.islower() and i in vowels and i in x:
            result.append(x[i])
        elif i.isupper() and i in vowels and i in x:
            result.append(x[i])
        elif i.islower():
            result.append(i.upper())
        elif i.isupper():
            result.append(i.lower())
        else:
            result.append(i)
    result1 ="".join(result)
    return result1

strings = "AEIOU"
print(flip(strings))
#TEST CASES
# Python = pYTHQN
# aeiou = CGKQW 
# Hello, world! = hGLLQ, WQRLD!
# AEIOU = cgkqw


        