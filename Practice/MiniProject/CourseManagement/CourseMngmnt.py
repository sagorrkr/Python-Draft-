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
            print(f"\n{self.name}'s enrolled courses:")   
            for course in self.enrolled_courses:
                print(course)    
        else:
            print(f"{self.name} is not enrolled in any course")

if __name__ == "__main__":
    course1 = Course(course_name = "Maths", course_code = 1234)
    course2 = Course(course_name = "Physics", course_code = 2345)
    course3 = Course(course_name = "Science", course_code = 3456)
    course4 = Course(course_name = "Java", course_code = 4567)

student1 = Student(student_id = 20240513001, name = "Mishu")
student2 = Student(student_id = 20240513003, name = "Vane")
student3 = Student(student_id = 20240513001, name = "Ridoy")

student1.enroll(course1)
student1.enroll(course2)

student1.display_enrolled_courses() 

    