'''
self: reference variable pointing the instance itself

super: reference variable pointing the base class instance
       super is used to call the base class methods.
'''
class Father(object):
    strHometown = "Jeju"
    def __init__(self, paramHome):
        self.strHometown = paramHome
        print("Father is created")
    def doFatherThing(self):
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother(object):
    strHomeTown = "Seoul"
    def __init__(self):
        print("Mother is created")
    def doMotherThing(self):
        print("Mother's action")

class Child(Father, Mother):
    strName = "Moon"
    def __init__(self, paramName, paramHome): #when an instance is created, two arguments will be 'pramName', 'paramHome'
        super(Child, self).__init__(paramHome) #bring the 'paramHome' from the superclass 'Father'
        self.strName = paramName
        print("Child is created")
    def doRunning(self):
        print("Fast")

me = Child("Sun", "Universe") #Father is created, Child is created
me.doFatherThing() #Father's action
me.doMotherThing() #Mother's action
me.doRunning() #Fast
print(me.strHomeTown) #Universe
print(me.strName) #Sun