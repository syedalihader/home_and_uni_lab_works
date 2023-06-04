class Student:
    def __init__(self, roll_number, name, grade):
        self.roll_number = roll_number
        self.name = name
        self.grade = grade


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_number, name, grade):
        student = Student(roll_number, name, grade)
        self.students.append(student)
        print(f"Student {name} with roll number {roll_number} added successfully.")

    def remove_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student with roll number {roll_number} removed successfully.")
                return
        print(f"Student with roll number {roll_number} not found.")

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Student found with roll number {roll_number}:")
                print(f"Name: {student.name}")
                print(f"Grade: {student.grade}")
                return
        print(f"Student with roll number {roll_number} not found.")

    def display_all_students(self):
        if len(self.students) == 0:
            print("No students found.")
        else:
            print("List of all students:")
            for student in self.students:
                print(f"Roll Number: {student.roll_number}, Name: {student.name}, Grade: {student.grade}")


# Example usage:
sms = StudentManagementSystem()

sms.add_student(1, "John Doe", "Grade 10")
sms.add_student(2, "Jane Smith", "Grade 9")
sms.add_student(3, "Mark Johnson", "Grade 11")

sms.display_all_students()

sms.search_student(2)

sms.remove_student(1)

sms.display_all_students()