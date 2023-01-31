'''
All of Python classes are the descendants of Object.

Object class has many hidden methods: __init__  constructor
                                      __del__
                                      __eq__    T/F examination
                                      __cmp__   compare
                                      __add__   

We actually override to those hidden methods.
'''
class Room:
    numWidth = 100
    numHeight = 100
    numDepth = 100

    def __init__(self, parWidth, parHeight, parDepth): #actually overriding from the object class
        self.numDepth = parDepth
        self.numWidth = parWidth
        self.numHeight = parHeight
    
    def getVolume(self):
        return self.numDepth*self.numHeight*self.numWidth

    def __eq__(self, other):
        if isinstance(other, Room):
            if self.getVolume() == other.getVolume(): #Duck Typing: the variable is not defined yet
                return True
        return False