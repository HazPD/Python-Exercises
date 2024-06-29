#Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java
#Output : java

user_filetype = input("Enter a filename: ")

extension = user_filetype.split(".")

print(extension[1])
