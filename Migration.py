
Student1Attr = {
    "height" : 120,
    "weight" : 200,
    "skin" : "dark"
}



Student1 = {
    "name": "Reilly",
    "course" : "BSCP",
    "age" : 24,
    "physical" : Student1Attr
}



print(Student1.get("physical").get("height"))