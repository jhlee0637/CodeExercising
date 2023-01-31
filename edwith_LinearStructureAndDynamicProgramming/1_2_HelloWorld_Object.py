'''
This is 'Object-oriented' Hello World.
Meaning, using class to make an instance later.

'''
class HelloWorld: #class name -> noun, camel casing
    def __init__(self): #constructor
        print ("Hello, world")

    def __del__(self):
        print ("Good Bye!")

    def performAverage(self, val1, val2): #method name -> verb, start with lower case
        average = (val1 + val2) / 2.0 #variable name -> noun, start with lower case
        print("The average of the scores is: ", average)

def main(): 
    world = HelloWorld()
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    world.performAverage(int(score1), int(score2))

main()

'''
Also, check the naming and styling recommendations

For class,
    - Noun for the concept to eb represented by the class
    - Capitalize the first letter of each word

For variable,
    - Noun for the contents to be stored
    - Start with lower case
    - Not recommend to note the type of variable
      (variable's type can be changed easily from Python)

For method,
    - Verb for the method action
    - Start with lower case
'''