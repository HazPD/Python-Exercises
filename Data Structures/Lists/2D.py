temps = [[0.0 for h in range(24)] for d in range(31)]

total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Average temperature at noon:", average)