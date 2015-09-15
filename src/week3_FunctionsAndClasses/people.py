'''
Created on Sep 14, 2015

@author: Philip Schulz
'''

# This is our first class definition. The argument of a class definition is the parent class of the
# class that we are currently creating
class Human(object):
    '''
    This class models fundamental traits of humans.
    '''
    
    # The variables that are owned by a class are known as fields. Every instance of that class will have those fields.
    age = None
    haircolour = None
    height = None

    # __init__ is the constructor and needs to be present in every class. It can take arguments.
    # Like any method, its first argument needs to be "self".
    def __init__(self, age, haircolour = 'blond', height = 175):
        '''
        Constructor
        '''
        self.age = age
        self.haircolour = haircolour
        self.height = height
        
    # Methods within classes are defined the same way as normal functions. The only difference is that they take "self" as first
    # argument.
    def change_haircolour(self, new_haircolour):
        '''
        Set the haircolour to a new value.
        
        @param new_haircolour: The new haircolour
        '''
        self.haircolour = new_haircolour
        
    def tell_age(self):
        '''
        Retrieve the age of the Human.
        
        @return: The age
        '''
        return self.age
        
    def have_birthday(self):
        '''
        Increase the age of the Human by 1.
        '''
        self.age += 1
        

# We are now building a sub-class of Human, called Student. It is also a sub-class of object, Human's parent.
class Student(Human):
    '''
    A class to model the traits of students.
    '''

    def __init__(self, name, age, gpa, haircolour = 'blond', height = 175):
        '''
        Constructor
        '''
        # We can use the super function to refer to functions from the parent. The syntax is 
        # super(this_class, self) and it returns the parent class. Thus, we are now calling
        # the constructor of the parent (Human).
        super(Student, self).__init__(age, haircolour, height)
        self.name = name
        self.gpa = gpa
        
    # Finally, we can also override methods that we have inherited from the superclass(es)
    def tell_age(self):
        return "No, I won't tell you my age."