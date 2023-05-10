import os
path = 'C:\\Users\\thoma\\OneDrive\\Documents\\COP1000C.txt'

os.path.isfile(path)
def main():
    try:
        

    
    
        file = open(COP1000C.txt,'r')
        print('-------------------------------------------------------------')
        print('                    College Grades Summary')
        print('-------------------------------------------------------------')
    
        print(title)
        print(f'Professor: {professor:<30} Term:{term}')
        print('{:<20}{:>5}'.format('Student Name','Grade'))
        print('-'*30)
        name = infile.readline().strip()

    except:
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


                print('Course Grades Summary Report ...')
                repeat = 'y'
                while repeat == 'y':
                    file = ''
    try:
            file = input('Enter name of course file: ')
            generate_report(file)
            
            print(f'Error: {file} not found.')
            repeat = input('\nWould you like to process another file (y/n)? ').lower()

    finally:
        print("this is it")

main()
    

