beatles = []

beatles.append("John lennon") #0 
beatles.append("Paul McCartney") #1 
beatles.append("George Harrison") #2

new_members = ["Stu Sutcliffe","Pete Best"]

for i in new_members:
    answer = input(f"Would you like to add {i} to the band?")
    if answer == 'yes':
        beatles.append(answer) 


del beatles[3:5] # will delete names in index 3-4. 
beatles.insert(0, "Ringo Starr") 

print(beatles)