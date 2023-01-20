class Father(object):
    strHometown = "Jeju"
    def __init__(self, paramHome): #constructor
        self.strHometown = paramHome
        print("Father is created")
    def doFatherThing(self): #method
        print("Father's action")
    def doRunning(self):
        print("Slow")

papa=Father("homehomehome")
print(papa.strHometown)