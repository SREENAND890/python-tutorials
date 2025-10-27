class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        total = sum(self.marks.values())
        subjects = len(self.marks)
        average = total / subjects
        return average

    def display_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print(f"{self.name}'s Average: {avg:.1f} | Grade: {grade}")


student1 = Student("Alice", {"Math": 85, "Science": 80})
student2 = Student("John", {"Math": 95, "Science": 87})

student1.display_grade()
student2.display_grade()
