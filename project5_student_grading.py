#Project 5: Student Grading System

print("Welcome to the Student Grading System!")

students = {}

for i in range(3):
    print(f"Student {i+1}:")
    student_name = input("Enter student's name: ")
    grades = []

    for j in range(3):
        while True:
            try:
                grade = int(input(f"Enter grade {j+1} for {student_name}: "))
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100. Please enter a valid grade.")
                    continue
                grades.append(grade)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    students[student_name] = grades

averages = {}
for student, student_grades  in students.items():
        average_grade = sum(student_grades ) / len(student_grades )
        averages[student] = average_grade
        print(f"{student}'s average grade: {average_grade:.2f}")

highest_average = max(averages, key=averages.get)
print(f"\nStudent  with highest average: {highest_average} ({averages[highest_average]:.2f})")