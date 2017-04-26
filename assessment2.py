# Parts 2 through 5:
# Create your classes and class methods
class Student(object):

    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

    def __repr__(self):
        return "Name: {} {} Address: {}".format(self.firstname, self.lastname, self.address)


class Question(object):

    def __init__(self, question, anwwer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):

        print self.question
        user_answer = raw_input("> ")
        if user_answer == self.answer:
            return True

class Exam(object):

    def __init__(self, correct_answer):
        self.question = []
        self.name = name

    def add_question(self):

        question = Question(self.question, self.answer)
        self.question.append(question)

    def administer(self):
        correct = 0
        for question in self.question:
            if question.ask_and_evaluate():
                correct += 1 

        return float((count/len(self.question))) * 100 



        def __repr__(self):
            return "{}".format(score)


    def __repr__(self):

        return "{}, {}".format(self.question, self.answer)


class StudentExam(object):

    def take_test(self):
        print self.administer()
        


def example():
    exam = Exam()
    exam.add_question("hi", "hi")
    exam.add_question("bye", "bye")
    exam.add_question("hello", "hello")

    student = Student()

    studentExam = StudentExam(student, exam)
    studentExam.take_test

