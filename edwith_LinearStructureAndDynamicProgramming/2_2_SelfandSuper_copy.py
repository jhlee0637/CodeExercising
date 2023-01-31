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
    def __init__(self, paramName, paramHome): #when the instance is created, two variables coming after the class name will be the parameters
        super(Child, self).__init__(paramHome) #bring the 'paramHome' from the superclass 'Father'
        self.strName = paramName
        print("Child is created")
    def doRunning(self):
        print("Fast")

me = Child("Sun", "Universe") #instance created
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHomeTown)
print(me.strName)