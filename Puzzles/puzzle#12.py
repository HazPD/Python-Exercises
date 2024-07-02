#Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
def isPalindrome(char_list):
    answer = []
    for i in range(len(char_list)): 
        if char_list[i] == char_list[i][::-1]:
            t = "True"
            answer.append(t)
        else:
            f = "False"
            answer.append(f)
            
    return answer

char_list = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
print(isPalindrome(char_list))