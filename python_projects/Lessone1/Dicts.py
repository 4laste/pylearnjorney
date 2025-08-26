car = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1999,
}
print(car["Brand"])
car["Color"] = "Black"
print(car)
car["Year"] = 2025
print(car)

for key,value in car.items():
    print(key, ":", value )

student = {
    "name": "Ivan",
    "age": 20,
    "grades": [5, 4, 5, 3, 4]
}
print(student["name"])

avg = sum(student["grades"]) / len(student["grades"])
print("Average grade:", avg)

student["passed"] = avg >= 4
print(student)
for key, value in student.items():
    print(key, ":", value)

book = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2020,
    "rating": [5, 4, 4, 5, 3]
}
print(book["title"])
print(book["author"])

avg = sum(book["rating"]) / len(book["rating"])
print("Average raitin:", avg)
book["popular"] = avg >= 4.5
for key, value in book.items():
    print(key, ":", value)
