"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages of object orientation include abstraction, 
   polymorphism, and encapsulation. 

   Abstraction affords programmers the ability to hide certain pieces of their
   code from the interface that other programmers or users interact with. A 
   programmer using a class you created does not need to understand each detail
   of the class in order to use it, thus reducing the complexity. 

   Polymorphism allows for a group to share interchangeable functionality so that
   components that do the same kind of things can be used interchangeable.

    Encampsulation means that methods pertaining to certain parts of a program
    stays associated, or "belong to", that part of the program. For example, all
    of the functionality of an exam can travel in an Exam class - import that,
    and you get all of the parts.     



2. What is a class?

    A class is a blueprint to make an object (aka instances). Note, a class is
    not something in it of itself, but rather a map to build a particular data
    structure (e.g. linked lists, trees, stacks, etc. 


3. What is an instance attribute?
    At a high level, an instance attribute is a variable inside a class. It is
    a piece of data (which can be any type, such as a list, integer, etc) that 
    is assinged to each individual instance. 

    For example, for a Human class, we could have instance attributes for those 
    things that are different person to person, like eye color, name, etc.


4. What is a method?
    A method isa a function inside a class. A method is like a behavior that a 
    class can execute. 


5. What is an instance in object orientation?
    An instance is an individual occurrence of an object, the idea made manifest.
    For an Exam class, each individual exam (e.g. Unit Test 1) would be an instance.


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    A class attribute exists on a class, whereas instance attributes exist on 
    the individual instances, and therefore their values may vary by instance.

    Example: Class attribute 
    In a Cat class, it would make sense to have a class attribute 
    of species (which would have the value Felis catus for all Cat instances).
    
    Example: Instance attribute
    In a Cat class, and instance attribute of name (which would be different for
    each Cat instance) would be better suited than a class attribute. 

"""


# Parts 2 through 5:
# Create your classes and class methods

################################################################################
"""
PART 2 
Directions: Make Python classes that could store each of the following three 
pieces of data. Use the tables below as examples to guide you in creating class
definitions for the following objects (see PDF in the w2_object_orientation
folder called PDF instructions). 

Define an __init__ method to allow callers of this class to provide initial values
for each attribute. Note: these classes should all be subclasses object, none is
a subclass of any other. 
"""

class Student(object):
    """ This is a Student object. """

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """ Question class, as in a question in an exam. """

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return "< Question question:%s correct_answer:%s>" % (self.question, self.correct_answer)

    def ask_and_evaluate(self):
        """ Pose a question to user, records user answer, and returns
        True if answer is correct and False otherwise."""

        answer = raw_input(self.question + " >")
        return self.correct_answer == answer 


class Exam(object):
    """ Exam object. Exams comprise zero or more question. """

    def __init__(self, name):
        self.name = name
        # We initialize the questions attribute as an empty list
        self.questions = []

    def add_question(self, question, correct_answer):
        """ Add question to exam."""

        question_object = Question(question, correct_answer)
        self.questions.append(question_object)

    """
    # Write method, administers all of the exam's question (how do you access
    each question in turn? Once you have a question, how do you administer it?

    Returns the user's tally of correct (as a decimal percentage)
    """ 

    def administer(self):
        """ Administer a test, returning the score."""

        score = 0

        #loop through exam list 
        for question in self.questions:
            if question.ask_and_evaluate():
                score = score + 1

        return float(score/len(self.questions))

        






























