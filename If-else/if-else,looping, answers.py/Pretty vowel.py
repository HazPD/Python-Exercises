#a for loop;
#the concept of conditional execution (if-elif-else)
#the continue statement.

word_without_vowels = ""

user_word = input("Enter a word: ")

vowel = ['A','E','I','O','U','a','e','i','o','u']

for letter in user_word: #skims letters in input
    if letter in vowel: #if letter is in vowel
        continue #it will run another interation to the next letter in the string
    else:
        letter is not vowel #if the next iteration letter is not a vowel
        word_without_vowels += letter #it will add the letter to the list
complete = ' '.join(word_without_vowels)
print(complete.upper())

