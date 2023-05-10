#JEREMY 
          
def main():
    try:
        file= open('D:\\Documents\COP1000C.txt', 'r')
        print(file.read())

    except Exception as e:
        print(e)

    
    count, passed , failed , total = 0,0,0,0
    file = open('C:/Documents/Python/COP1000C.txt', 'r')
    print('-------------------------------------------------------------')
    print('                   Broward College Grades Summary')
    print('-------------------------------------------------------------')
    title = infile.readline().strip()
    professor = infile.readline().strip()
    term = infile.readline().strip()
    print(title)
    print(f'Professor: {professor:<30} Term:{term}')
    print('{:<20}{:>5}'.format('Student Name','Grade'))
    print('-'*30)
    name = infile.readline().strip()

    while name:
        grade = int(infile.readline().strip())
        print('{:<20}{:>5}'.format(name,grade))
        name = infile.readline().strip()
        count += 1
        total += grade
        if grade>=60: passed+=1
        else: failed+=1
    print('Students\' Performance')
    print('-'*30)
    print('Passed: {:<15}Failed:{:>2}'.format(passed,failed))
    print('Passing Percent: {}'.format(round(passed*100/count)))
    print('Average Grade: {}'.format(round(total/count)))
    infile.close()


def main():
    print('Course Grades Summary Report ...')
    repeat = 'y'
    while repeat == 'y':
        file = 'C:/Documents/COP1000C.txt'
        try:
            file = input('Enter name of course file: ')
            generate_report(file)
        except:
            print(f'Error: {file} not found.')
        repeat = input('\nWould you like to process another file (y/n)? ').lower()


main()
