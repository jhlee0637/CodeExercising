class Father(object):
    strHomeTown = "Jeju"
    def __init__(self): #constructor
        print("Father is created")
    def doFatherThing(self): #method
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother(object):
    strHomeTown = "Seoul"
    def __init__(self): #constructor
        print("Mother is created")
    def doMotherThing(self): #method
        print("Mother's action")

class Child(Father, Mother): #two super classes
    strName = "Moon"
    def __init__(self):
        super(Child, self).__init__() #call the super class Father
        print("Child is created")
    def doRunning(self): #method override
        print("Fast")

me = Child() #instance created
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHomeTown)
print(me.strName)