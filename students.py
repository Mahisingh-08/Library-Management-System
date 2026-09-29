from data import students

# Add a new student
def add_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    course = input("Enter course: ")

    new_student = {
        "id": student_id,
        "name": name,
        "course": course
    }

    students.append(new_student)

    print("Student added successfully!")

# Display all students
def view_students():
    print("\n----- STUDENT LIST -----")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("------------------------")

