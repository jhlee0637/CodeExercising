class HelloWorld:
    def __init__(self):
        print ("Hello, world")

    def __del__(self):
        print ("Good Bye!")

    def performAverage(self, val1, val2):
        average = (val1 + val2) / 2.0
        print("The average of the scores is: ", average)

def main():
    world = HelloWorld()
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    world.performAverage(int(score1), int(score2))
    print ("out?")


main()
print ("out")