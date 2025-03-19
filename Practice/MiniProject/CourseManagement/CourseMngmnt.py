class Course:
    def __init__(self,course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def __str__(self):
        return f"{self.course_code}: {self.course_name}"

class Student:
    def __init__(self,student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"{self.name} has enrolled in {course.course_name}")
        else:
            print(f"{self.name} has already enrolled in this course.")
    def display_enrolled_courses(self):
        if self.enrolled_courses:
            print(f"\n{self.name} Enrolled courses")   
            for course in self.enrolled_courses:
                print(course)    
        else:
            print(f"{self.name} is not enrolled in any course")
    

    