class Student:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f'course: {course} added for student {self.name}')

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"Course '{course}' removed for student {self.name}.")
        else:
            print(f"Student: {self.name} is not rolled in course '{course}'.")

    def display_info(self):
        print(f'Student: name {self.name} ')
        print(f'Student: ID {self.student_id} ')
        print('rolled courses:')
        for course in self.courses:
            print(course)


student1 = Student('kote', 12442, 'Physics')
student2 = Student('luka', 12443, 'Political science')

student1.add_course('Biology')
student2.add_course('Chemical engineering')
student1.remove_course("Physics")
student2.remove_course("Biology")
student1.display_info()
student2.display_info()
