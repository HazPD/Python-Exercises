#Write a Python program to find the XOR of two given strings interpreted as binary numbers.
def Strings(b_String):
    for i in range(len(b_String)-1):
        x = int(b_String[i],2) #converts binary string to integer. 2 serves as byte for conversion which means binary
        y = int(b_String[i+1],2)
        result = x ^ y 
        xor = bin(result)
    return xor


b_String = ['100011101100001', '100101100101110']

#TEST CASES
#['100011101100001', '100101100101110'] =  0b110001001111
#['0001', '1011'] =0b1010

print(Strings(b_String))
