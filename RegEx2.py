import re

names = ['Reilly Panens', 
        'Cade Eryx',
        'Eliz Javier', 
        'Kriselace Javier', 
        'N!sha', 
        'C4de 3ryx']

values = ['https://www.facebook.com',
          'https://www.twitter.com',
          'http://www.google.com',
          'www.linkedin.com',]

#Syntax for getting names with first and last names
#parenthesis created groups with our search function
#?P <> is syntax for naming groups within our search pattern
regex = '^(?P<fn>\w+)\s+(?P<ln>\w+)$'
for name in names:
    result = re.search(regex, name)
    if(result):
        print(name)                         #this will display f&l name
        print(result.group('fn'))           #this will display the first group of characters
        print(result.group('ln'))           #this will display the last group of characters
                                            #with group names, we can now use the group name instead of index number.

#Syntax for getting a series of characters 
#a-z for lowercase 
#A-Z for uppercase
#! for exclamation mark
r1 = '^[a-zA-Z!]+$'
for name in names:
    result = re.search(r1, name)
    if(result):
        print(name)
                  

#Scans for blocks of lowercase characters
r2 = '[a-z]+'
for name in names:
    result = re.findall(r2, name)
    if(result):
        print(result)


#Test if strings starts with http or https
r3 = 'http'
for value in values:
    result = re.match(r3, value)
    if(result):
        print(value)
  