# squares numbers from 1 to 10
squares = [i * i for i in range(1, 11)]
print(squares)

# filters all students that passed the test
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

passed_students = [i for i in students if i >= 60]

failed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)
print(failed_students)