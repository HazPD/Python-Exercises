import re 

names = ['Christian Panen',
         'Cade Eryx',
         'Eliz',
         'IanBuknooy',
         'Jaymar laseros muntanga',
         'PatrickBatalla',
         'Reilly Javier',]

#Find people with first name and last name only
#Ignore people with 1 or 3 names

#This syntax will find a name within the list of people that starts with one set of characters + another one set of characters
regex = '^\w+ \w+$'

for name in names:
    result  = re.search(regex, name)
    if(result):
        print(name)

#This syntax will search for a names that starts with Capital Letter C and ends with lowercase letter n
capital = 'C\w* \w+n$'

for name in names:
    result  = re.search(capital, name)
    if(result):
        print(name)
        print(result.start())
        print(result.end())