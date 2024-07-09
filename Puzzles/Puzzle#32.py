#Write a Python program to rescale and shift numbers in a given list, so that they cover the range [0, 1].

def rescale(int_list):
    x = min(int_list)
    y = max(int_list)
    Range = y-x

    #RescaledList = []
    RescaledValues = [(j - x) / Range for j in int_list]
    #RescaledList.append(RescaledValues)

    return RescaledValues

int_list = [13.0, 17.0, 17.0, 15.5, 2.94]

#test cases 
#[13.0, 17.0, 17.0, 15.5, 2.94] = [0.7155049786628734, 1.0, 1.0, 0.8933143669985776, 0.0]
#[18.5, 17.0, 18.0, 19.0, 18.0] = [0.75, 0.0, 0.5, 1.0, 0.5]
print(rescale(int_list))

    

