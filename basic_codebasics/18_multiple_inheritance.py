class Teacher:
    def teacher_action(self):
        print("I am a teacher")

class student:
    def student_action(self):
        print("I am a student")

class youTuber:
    def youTuber_action(self):
        print("I am a youtuber.")

class Person(Teacher, student, youTuber):
    pass

a = Person()
a.teacher_action()
a.student_action()
a.youTuber_action()