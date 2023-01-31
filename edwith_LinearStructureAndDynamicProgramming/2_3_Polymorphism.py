'''
method overriding: change the behavior of existing methods

method overloading: more than one method of the same class shares the same method name having different signatures
'''
class Building:
    strAddress = "Daejeon"
    def openDoor(self):
        print("Door Opened")

class Hotel(Building):
    def openDoor(self): #overriding of the method 'openDoor' from the super class 'Building'
        print("Bellboy opens a door")
    def checkIn(self, days = 1): #overloading by putting default value of the parameter
        print("Someone checks in for", days, "days")

lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkIn() #default value of 'days' is 1. So in here, the method 'checkIn' looks like doesn't have any parameter.
lotteHotel.checkIn(2) #the method 'checkIn' gets parameter but still works with overloading.