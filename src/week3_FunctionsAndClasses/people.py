'''
Created on Sep 14, 2015

@author: Philip Schulz
'''

class Human(object):
    '''
    This class models fundamental traits of humans.
    '''

    age = None
    haircolour = None
    height = None

    def __init__(self, age, haircolour = 'blond', height = 175):
        '''
        Constructor
        '''
        self.age = age
        self.haircolour = haircolour
        self.height = height
        
    def change_haircolour(self, new_haircolour):
        self.haircolour = new_haircolour
        
    def tell_age(self):
        return self.age
        
    def have_birthday(self):
        self.age += 1
        

class Student(Human):
    '''
    classdocs
    '''


    def __init__(self, name, age, gpa, haircolour = 'blond', height = 175):
        '''
        Constructor
        '''
        pass
        super(Student, self).__init__(age, haircolour, height)
        self.name = name
        self.gpa = gpa
        
    def tell_age(self):
        return "No, I won't tell you my age."