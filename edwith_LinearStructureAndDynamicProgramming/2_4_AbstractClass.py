'''
abstract class: A class with an abstract method

abstract method: A method with signature, but with no implementation.
                 Abstract method is not a complete.
                 You can't make an instance out of it.
                 The concrete class with 'full' implementations and inheriting the abstract class will be a basic for instances.
'''
from abc import ABC, abstractmethod

class Room(ABC):
    @abstractmethod #indicator of abstract base method and class
    def openDoor(self):
        pass
    @abstractmethod
    def openWindow(self):
        pass

class BedRoom(Room):
    def openDoor(self):
        print("Open bedroom door")
    def openWindow(self):
        print("Open bedroom winodw")

class Lobby(Room): #this class has a lack of method, 'openWindow' which is the abstract base method of the super calss.
    def openDoor(self):
        print("Open lobby door")

room1 = BedRoom()
print(issubclass(BedRoom, Room), isinstance(room1, Room))

lobby1 = Lobby()
print(issubclass(Lobby, Room), isinstance(lobby1, Room))