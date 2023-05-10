def main():    # while loop which break when user enter n or N
    while True:
    
        print('\nCourse Grades Summary Report ...\n')
    
            # asking file name
        fileName = input('Enter name of course file: ')

            # try and except blocks to catch errors
        try:
                # opening file
                file = open(fileName)
                print('-'*60)
                print('%40s' % "College Grade Summary")
                print('-'*60)

            
                # reading file
                data = file.read().splitlines()
                # printing header
        
                print('\n' + data[0])
                print("Professor: %s %28s" % (data[1], "Term: "+data[2]))
                print("\n%-25s   %13s" % ("Student Name", "Grade"))
                print('-'*45)
                passed = 0
                failed = 0
                totalGrade = 0
                numStudent = 0

                   # loop through the data with increment 2
                # because each student data contains 2 lines
                # line 1 is name , line 2 is grade
                for i in range(3, len(data[0]), 2):
                    # reading name and grade
                    name = data[i]
                    grade = int(data[i+1])

                    # if grade greater than 60 adding to passed
                    if grade >= 60:
                        passed += 1
                    # else failed
                    else:
                        failed += 1

                    # adding grade to total grades and increasing student count
                    totalGrade += grade
                    numStudent += 1
                    print("%-25s %13s" % (name, grade))

                     # printing summery
                print("Students' Performance")
                print('-'*45)
                passingPercent = (passed/numStudent)*100
                avgGrade = totalGrade/numStudent
                print("Passed: %d \t\t\t\t\t Failed: %d" % (passed, failed))
                print("Passing Percent: %.0f%%" % passingPercent)
                print("Average Grade: %.0f" % avgGrade)

                # asking to continue or exit
                choice = input("\nWould you like to process another file (y/n)? ")
                if choice == "N" or choice == 'n':
                    break
            
        except FileNotFoundError:
                print('\nFile Not Found')
        except IOError:
                print('\nIO Error occurred')
main()
