CourseStudent = [
#index  0       1       2        3
    ["BSIT",["David","Alenere"]],
    ["BSCS",["Jaymar","Emman","Patrick"]],
    ["BLIS",["Cade","Reilly","Eliz"]]
]

for bsit in CourseStudent:
    #Index 0 for Courses which is in first box
    print(bsit[0])
    #index 1 used for the students name since they are in the 2nd index
    for names in bsit[1]:
        print(" -" + str(names))
    print()
   