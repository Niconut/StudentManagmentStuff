studentList = [['Kevin', 1, 9], #Student list ordered: String name, int studentID, float grade
            ['Kanu', 2, 10],
            ['Johann', 3, 11],
            ['Aedan', 4, 12]]

def numResponse(prompt:str, min=None, max=None, varType=int): #Extra feature: Data validation , NumResponese borrowe from Dustin
    '''Data validation - WIP
    - Add option for inclusive or exclusive 
    - Optimize
    - Change default variable?'''
    while True:
        try:
            x = varType(input(prompt))
            if isinstance(min,(int,float)) and x < min:
                print(f'The minimum is {min}')
                raise Exception('Number is below minimum')
            elif isinstance(max,(int,float)) and x > max:
                print(f'The maximum is {max}')
                raise Exception('Number is above maximum')
        except ValueError:
            print('Enter a number')
        except:
            print('That\'s not a valid input')
        else:
            return x


def printDetails(student):
    print(f'- Name: {student[0]}') 
    print(f'- StudentID: {student[1]}')
    print(f'- Grade: {student[2]}\n')

def addStudent():
    print('Add student')
    name = input('Student name: ')
    studentID = numResponse('Student ID: ')
    grade = numResponse('Grade: ')
    studentList.append([name, studentID, grade])
    print('Student added')

def displayStudents():
    for student in studentList:
        printDetails(student)

def findStudentByID():
    idSearch = numResponse(f'Student ID:')
    for student in studentList:
        if student[1] == idSearch:
            printDetails(student)

def UpdateStudentAttributesImproved():
    print('''Pick Student to Update by inputting ID, Name, And Grade''')
    studentID = numResponse('Student ID:')
    studentName = input('Student Name:')
    studentGrade = numResponse('Grade:')
    for student in studentList:
        if student[1] == studentID:
            if student[0] == studentName:
                if student[2] == studentGrade:
                    print('''Choose Student Attribute You Want To Update
                        1. ID
                        2. Grade
                        3. Name''')
                    preferredChange=numResponse('Choose an option:',1,3)-1
                    change = ['ID','grade', 'name'][preferredChange]
                    if change == 'name':
                                student[0] = input('Student Changed Name:') 
                                print('Changed Name')
                                printDetails(student)
                                return
                
                    elif change == 'grade':
                                student[2] = numResponse('Student Changed Grade:') 
                                print('Changed Grade')
                                printDetails(student)
                                return
                
                    elif change == 'ID':
                                student[1] = numResponse('Student Changed ID:') 
                                print('Changed ID')
                                printDetails(student)
                                return
                    
    else:
        print (f'No Student with that description')
        return
def removeStudentImproved():
    print('''Remove Student by inputting ID, Name, And Grade''')
    studentID = numResponse('Student ID:')
    studentName = input('Student Name:')
    studentGrade = numResponse('Grade:')
    for student in studentList:
        if student[1] == studentID:
            if student[0] == studentName:
                if student[2] == studentGrade:
                    printDetails(student)
                    studentList.remove(student)
                    print('Student Removed')
                    return
    else: 
        print("No Student matches that description")
        return
                    


funcs = [addStudent,
         displayStudents, 
          findStudentByID, 
          removeStudentImproved, 
          UpdateStudentAttributesImproved]
while True:
    print('''Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student
5. Update Student Attributes
6. Exit''')
    chosenManagement = numResponse('Choose an option:', 1,6,int)-1
    print('')
    if chosenManagement == 5:
        break
    funcs[chosenManagement]()
    print('-' * 20 +'\n')
