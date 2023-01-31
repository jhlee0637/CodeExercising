'''
inheritance: Giving my attribute(member variables, methods) to my descendants

superclass: my ancestors, specifically my father
            Python let the class has more than two one parent class(<-> Java)

subclass: my descendatns, specifically my son
'''

class Father(object): #the superest class is inherited from 'object' class
    strHomeTown = "Jeju"
    def __init__(self): #constructor
        print("Father is created")
    def doFatherThing(self): #method
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother(object):
    strHomeTown = "Seoul"
    def __init__(self):
        print("Mother is created")
    def doMotherThing(self):
        print("Mother's action")

class Child(Father, Mother): #the class 'Child' has two super classes
    strName = "Moon"
    def __init__(self):
        super(Child, self).__init__() #call the super class 'Father'
        print("Child is created")
    def doRunning(self): #method override
        print("Fast")

me = Child() #instance created
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHomeTown)
print(me.strName)