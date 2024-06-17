Username = ["John","Alenere","David"]
Password = ["abc123","123abc","Hahatdog"]

User = (input("Enter your username: "))
Pass = (input("Enter your password: "))
for x in range(len(Username)):
    
    if User == Username[x] and Pass == Password[x]:
        print("welcome " + Username[x])
        break
else:
    print("Account not found")
        