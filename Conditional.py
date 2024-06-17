# == equal
# != not equal 
# > greater
# < less 
# >= greater than or equal
# <= less than or equal 

Grade1 = int(input("Enter grade for first grading: "))
Grade2 = int(input("Enter grade for second grading: "))
Grade3 = int(input("Enter grade for third grading: "))

Average = (Grade1 + Grade2 + Grade3)/3


if Average > 100 or Average <= 50:
    print("Invalid grade")
elif Average >= 98:
    print("With Highest Honor")
elif  Average >= 95 and  97:
    print("With High Honors")
elif  Average >= 90 and  94:
    print("With Honors")
elif  Average >= 75 and 89:
    print("Passed")
else:
    print("failed")


   
