students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

students.sort(reverse=True)
sorted_students = sorted(students, reverse=True)

for i in students:
    print(i)

print()

for i in sorted_students:
    print(i)

print()

students = [
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr. Krabs", "C", 78)
]

students.sort(key=lambda grades: grades[1], reverse=True)
sorted_students = sorted(students, key=lambda grades: grades[1])

for i in students:
    print(i)

print()

for i in sorted_students:
    print(i)