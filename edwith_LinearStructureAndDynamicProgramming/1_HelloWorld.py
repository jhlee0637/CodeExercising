def main():
    print ("Hello, world")
    print ("This program computes the average of two exam scores.")

    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    average = (int(score1) + int(score2)) / 2.0

    print("The average of the scores is: ", average)

main()