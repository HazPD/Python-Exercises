user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()

# Initialize an empty string for the word without vowels
word_without_vowels = ""

# Loop through each letter in the user_word
for letter in user_word:
    # If the letter is a vowel, continue to the next iteration
    if letter in 'AEIOU':
        continue
    # If the letter is not a vowel, concatenate it to word_without_vowels
    word_without_vowels += letter

# Print the word without vowels
print("Word without vowels:", word_without_vowels)