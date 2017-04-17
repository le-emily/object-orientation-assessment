"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction: Hiding data we don't need. You use the class without having to know
   what the technical nitty gritty inside is. For example, when you use .lower(),
   you know that it lower-cases a string but you don't have to know how it does this.

   Encapsulation: Everything is kept "together". This also helps prevent data
   from being modified. There are no accidental access/modification.

   Polymorphism: Interchangeability of components. You can over ride methods, use it and have your own copy of the method.
   You can take what you want from the parent class and modify it, and you decide exactly what to use.
   

2. What is a class?
    A construct that Python lets you create to structure your .

3. What is an instance attribute?
    Its created after the instance was instantiated.

4. What is a method?
    A method is like a function but it is a class' 'function'. 

5. What is an instance in object orientation?
    It is what you create from a class--a 'copy' of the class if you will. I like to 
    say that an intance is a thing created from a particular class (with all its blueprints).

6. How is a class attribute different than an instance attribute?
   Class attributes are attributes that all objects that are created from the class share.
   An instance attribute is specific to a particular instance so it could be different for two instances.
   Two instances can have the same class attribute is they don't have specific instance attributes.

"""


"""
Part 2
"""
class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name,
        self.last_name = last_name,
        self.address = address

    def __repr__(self):
        return "First Name: {}, Last Name: {}, Address: {}".format(self.first_name, self.last_name, self.address)


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question,
        self.correct_answer = correct_answer

    def __repr__(self):
        return "Question: {} Answer: {}".format(self.question, self.correct_answer)

    def ask_and_evaluate(self):
        print "{} ".format(self.question)
        answer = raw_input("> ")
        if answer == self.correct_answer:
            return True 
        else:
            return False

"""
Part 3 
"""

class Exam(object):

    def __init__(self, name):
        self.name = name,
        self.questions = []

    def add_question(self, question, correct_answer):
        my_question = Question(question, correct_answer)
        self.questions.append(my_question)

    def administor(self):
        correct = 0.0
        for question in self.questions:
            if question.ask_and_evaluate():
                correct += 1 

        return correct/len(self.questions)*100


"""
Part 4 
"""

class StudentExam(object):

    def __init__(self, student, exam):
        self.student = student 
        self.exam = exam 
        self.score = None

    def take_test(self):
        print self.exam.administor()

    # def __repr__(self):
    #     return "{} -- {}".format(self.student, self.exam)


# def example():
#     exam = Exam('Midterm')

#     exam.add_question('What is the method for adding an element to a set?', '.add()')
#     exam.add_question('What function randomizes the items of a list in place?', 'shuffle(lst)')
#     exam.add_question('What is the output of print list[0] if list = [ "abcd", 786 , 2.23, "john", 70.2 ]?', 'abcd')
#     exam.add_question('What function checks in a string that all characters are in lowercase?', '.islower()')

#     student = Student('Emily', 'Le', '1234 Unicorn Way')

#     student_exam = StudentExam(student, exam)
#     student_exam.take_test()


"""
Part 5
"""

class StudentQuiz(StudentExam):

    def __init__(self, student, quiz):
        super(StudentQuiz, self).__init__(student, quiz)

    def take_test(self):
        super(StudentQuiz, self).take_test()

    # def __repr__(self):
    #     def __repr__(self):
    #     return "{} -- {}".format(self.student, self.quiz)

class Quiz(Exam):

    def __init__(self, name):
        super(Quiz, self).__init__(name)

    def add_question(self, question, correct_answer):
        return super(Quiz, self).add_question(question, correct_answer)

    def administor(self):
        correct = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                correct += 1 

        if correct >= len(self.questions)/2.0:
            return 1
        else:
            return 0


def example():
    quiz = Quiz('First_Quiz')

    quiz.add_question('What is the method for adding an element to a set?', '.add()')
    quiz.add_question('What function randomizes the items of a list in place?', 'shuffle(lst)')
    quiz.add_question('What is the output of print list[0] if list = [ "abcd", 786 , 2.23, "john", 70.2 ]?', 'abcd')
    quiz.add_question('What function checks in a string that all characters are in lowercase?', '.islower()')

    student = Student('Emily', 'Le', '1234 Unicorn Way')

    student_quiz = StudentQuiz(student, quiz)
    student_quiz.take_test()
 


