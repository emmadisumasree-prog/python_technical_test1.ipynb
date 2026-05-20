
print("Intern Student Management")
students = []

for i in range(2):
    print(f"\nEnter Student {i+1} Details")

    student = {}


    student["name"] = input("Enter name: ")
    student["role"] = input("Enter target role: ")
    student["cgpa"] = float(input("Enter CGPA: "))

    projects = []

    p1 = input("Enter Project 1: ")
    p2 = input("Enter Project 2: ")

    projects.append(p1)
    projects.append(p2)

    student["projects"] = projects

    # Set for unique skills
    skills = set(input("Enter skills separated by space: ").split())

    student["skills"] = skills

    student["student_id"] = (i+1, "ALG2026")

    students.append(student)

for student in students:

    print(f"Student ID : {student['student_id']}")
    print(f"Name : {student['name']}")
    print(f"Role : {student['role']}")
    print(f"CGPA : {student['cgpa']}")

    print("Projects :")

    for project in student["projects"]:
        print("-", project)

    print("Skills :", student["skills"])


    if student["cgpa"] >= 7:
        print("Status : Eligible")
    else:
        print("Status : Need Improvement")

    print("=" * 40)