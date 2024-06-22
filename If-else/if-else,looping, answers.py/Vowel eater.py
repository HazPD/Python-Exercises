#ask the user to enter a word;
#use user_word = user_word.upper() to convert the word entered by the user to upper case;
# 
# we'll talk about string methods and the upper() method very soon – don't worry;
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#print the uneaten letters to the screen, each one of them on a separate line.

#Your task here is very special: you must design a vowel eater! Write a program that uses:
# a for loop;
#the concept of conditional execution (if-elif-else)
#the continue statement.

user_word = str(input("Enter a word: "))
user_word = user_word.upper()
vowel = ['A','E','I','O','U']


for letter in user_word: #skims letters in input
    if letter in vowel: #if letter is in vowel
        continue #it will run another interation to the next letter in the string
    else:
        letter is not vowel #if the next iteration letter is not a vowel
        print(letter)       #it will print letter
    
   