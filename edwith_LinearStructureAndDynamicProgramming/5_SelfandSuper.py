class Father(object):
    strHometown = "Jeju"
    def __init__(self, paramHome): #constructor
        self.strHometown = paramHome
        print("Father is created")
    def doFatherThing(self): #method
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother(object):
    strHometown = "Seoul"
    def __init__(self): #constructor
        print("Mother is created")
    def doMotherThing(self): #method
        print("Mother's action")

class Child(Father, Mother): #two super classes
    strName = "Moon"
    def __init__(self, paramName, paramHome):
        super(Child, self).__init__(paramHome) #call the super class: Father
        self.strName = paramName
        print("Child is created")
    def doRunning(self): #method override
        print("Fast")

me = Child("Sun", "Universe")
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHometown)
print(me.strName)