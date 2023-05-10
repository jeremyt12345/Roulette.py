def main():    
    # Printing header    
    print("\nQuiz Grading App ...")
    print("\nQuiz Grading App ...")
    # Getting correct answers
    correctAns = getCorrectAnswers()
     # Looping till user want to quit
    while True:
        # Reading name of student
        print("\n\nEnter name of student:   ", end="")
        stuName = input()
        # Reading answers file
        print("  \"   quiz answers file: ", end="")
        ansFile = input()
        # Reading student answers
        studentAns = getUserAnswers(ansFile,ansFile)
        # Counts
        correctAnsCnt, inCorrectAnswers = process(correctAns, studentAns)
        # Results
        printResults(stuName, correctAnsCnt, inCorrectAnswers)
        # Prompting for another student
        print("\nDo you have another student (y/n)? ", end="")
        ans = input()
        if ans.lower() == 'n':
            break
def getCorrectAnswers():
    # Storing correct answers
    correctAns = ['A','C','A','B','B','D','D','A','C','A','B','C','D','D','B']
    return correctAns

def getUserAnswers(ansFile,fileName):
    # Reading answers from file
    studentAns=[]
    try:
        # Opening and reading data from file
        fp = open(ansFile, 'r')
        # Reading answers
        for line in fp:
            studentAns.append(line.strip())
    except:
        print('Error!! Processing input file')
    return studentAns
def process(correctAns, studentAns):
    """ Process the answers """
    # Counts
    correctAnsCnt=[0]
    inCorrectAnswers=[0]
    # Comparing lists
    for i in range(0,15):
        if studentAns[0]== correctAns[0]:
            # Incrementing counts
            correctAnsCnt += 1

        else:
            # Adding to list
            inCorrectAnswers.append(i+1)
    return correctAnsCnt, inCorrectAnswers
main()

