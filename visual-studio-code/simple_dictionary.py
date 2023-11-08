student = {}

print(student)
print(type(student))

student = dict()

print(student)
print(type(student))

student = {
    "name":"Kemoy",
    "year":3,
    "GPA":4.9,
    }

print(student)

student = dict(name="Kemoy", year=3, GPA=4.9)
print(student)

print(student["name"])
print(student["GPA"])

print("name" in student)
print(student.keys())
print(student.values())

for key in student:
    print(f"{key}")

for key in student:
    print(f"{key}-->{student[key]}")

for key,value in student.items():
    print(f"{key}-->{value}")

student =  {}
student["id"] = 12345687
student["id"] = 1234568999999
student["name"] = "Alvin"
student["card"] = ("Ace", "Spade", "Black")
student["list"] = ["1","2","3"]
student["dictionary"] = {"name":"Yes!!"}
print(student)

students = {
    "1234567":
    {
        "name":"Kemoy",
        "year":3,
        "GPA":4.9,
    },
    "12345674444444":
    {
        "name":"Shawn",
        "year":3,
        "GPA":2.2,
    }
}

print(students)
