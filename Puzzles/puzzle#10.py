#Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
def check_p(input_string1):
    current_group = []  
    parenthesis = []
    counter = 0             
    for char in input_string1:  #iteration for every character in input_string1
        if char == "(":                         
            current_group.append(char)           
            counter += 1                        
        if char == ")":
            current_group.append(char)
            counter -= 1
        if counter == 0:                        #+=(  -=), meaning if it went back to 0, we have a complete set of parenthesis
            cg_replica = current_group[:]       #creates a current_group copy everytime the counter becomes 0
            cg_replica = "".join(cg_replica)    #joins all element into one index or basically removes "," from current_group
            parenthesis.append(cg_replica)      #moves the joined element as an element to parenthesis list
            current_group.clear()               #clears the original temp list as well as cg_replica for the next iteration.
    return parenthesis
            
input_string = "() (( ( )() ( )) ) ( ())"
input_string1 = input_string.replace(" ","")

print(check_p(input_string1))

#TEST CASES 
#input: "( ()) ((()()())) (()) ()" ////// output: ['(())', '((()()()))', '(())', '()']
#input: "() (( ( )() ( )) ) ( ())" ////// output: ['()', '((()()()))', '(())']





