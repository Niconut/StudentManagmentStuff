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

class Student:
    def __init__(self, name, ID, grade): #Initializing Class
        self.name = name
        self.ID = ID
        self.grade = grade
    
    def printDetails(self): #Printing Details
        print(f'Name: {self.name}') 
        print(f'StudentID: {self.ID}')
        print(f'Grade: {self.grade}\n')



class StudentManager:
    def __init__(self, studentList):
        self.studentList = studentList

    def addStudent(self):
        print('Add student')
        name = input('Student name: ')
        studentID = numResponse('Student ID: ')
        grade = numResponse('Grade: ')
        self.studentList.append(Student(name, studentID, grade))
        print('Student added')
    
    def displayStudent(self):
        for Student in self.studentList:
            Student.printDetails()
    
    def findStudentByID(self):
        idSearch = numResponse(f'Student ID:')
        for Student in self.studentList:
            if Student.ID == idSearch:
                Student.printDetails()
    '''print()
        
        idMatch = [lambda x:x == idSearch]
        idMatchList = list(filter(lambda Student: idMatch(Student), self.studentList))
        if len(idMatch) == 0:
            print('No person with the given ID is found')'''
    def removeStudentByPreference(self):
        print('''Remove Student by
        1. ID 
        2. Grade
        3. Name''')
        preferredRemoval = numResponse('Choose an option: ',1,3)-1
        preference = [ 'ID', 'grade', 'name'][preferredRemoval]
        if preferredRemoval == 2:
            search = input("Name:")
        else:
            search = numResponse(f'Student {preference}:')
        
        if preference == 'name':
            for Student in self.studentList:
                if Student.name == search:
                    print('Removed Student')
                    Student.printDetails()
                    self.studentList.remove(Student)
                    return
        elif preference == 'grade':
            for Student in self.studentList:
                if Student.grade == search:
                    print('Removed Student')
                    Student.printDetails()
                    self.studentList.remove(Student) 
                    return
        elif preference == 'ID':
            for Student in self.studentList:
                if Student.ID == search:
                    print('Removed Student')
                    Student.printDetails()
                    self.studentList.remove(Student) 
                    return
        else:
            print (f'No Student with that {preference}')
    
    def UpdateStudentAttributes(self):
        print('''Update Student
              1. ID
              2. Grade
              3. Name''')
        preferredChange=numResponse('Choose an option:',1,3)-1
        change = ['ID','grade', 'name'][preferredChange]
        if preferredChange == 2:
            search = input("Student Current Name:")
        else:
            search = numResponse(f'Student Current {change}:')
        if change == 'name':
            for Student in self.studentList:
                if Student.name == search:
                    Student.printDetails()
                    Student.name = numResponse('Student Changed Name:') 
                    print('Changed Name')
                    return
    
        elif change == 'grade':
            for Student in self.studentList:
                if Student.grade == search:
                    Student.printDetails()
                    Student.grade = numResponse('Student Changed Grade:') 
                    print('Changed Grade')
                    return
    
        elif change == 'ID':
            for Student in self.studentList:
                if Student.ID == search:
                    Student.printDetails()
                    Student.ID = numResponse('Student Changed ID:') 
                    print('Changed ID')
                    return
        
        else:
            print (f'No Student with that {change}')
    def UpdateStudentAttributesImproved(self):
        print('''Pick Student to Update by inputting ID, Name, And Grade''')
        studentID = numResponse('Student ID:')
        studentName = input('Student Name:')
        studentGrade = numResponse('Grade:')
        for Student in self.studentList:
            if Student.ID == studentID:
                if Student.name == studentName:
                    if Student.grade == studentGrade:
                        print('''Choose Student Attribute You Want To Update
                            1. ID
                            2. Grade
                            3. Name''')
                        preferredChange=numResponse('Choose an option:',1,3)-1
                        change = ['ID','grade', 'name'][preferredChange]
                        if change == 'name':
                                    Student.name = input('Student Changed Name:') 
                                    print('Changed Name')
                                    Student.printDetails()
                                    return
                    
                        elif change == 'grade':
                                    Student.grade = numResponse('Student Changed Grade:') 
                                    print('Changed Grade')
                                    Student.printDetails()
                                    return
                    
                        elif change == 'ID':
                                    Student.ID = numResponse('Student Changed ID:') 
                                    print('Changed ID')
                                    Student.printDetails()
                                    return
                        
        else:
            print (f'No Student with that description')
            return
    def removeStudentImproved(self):
        print('''Remove Student by inputting ID, Name, And Grade''')
        studentID = numResponse('Student ID:')
        studentName = input('Student Name:')
        studentGrade = numResponse('Grade:')
        for Student in self.studentList:
            if Student.ID == studentID:
                if Student.name == studentName:
                    if Student.grade == studentGrade:
                        Student.printDetails()
                        self.studentList.remove(Student)
                        print('Student Removed')
                        return
        else: 
            print("No Student matches that description")
            return
                    

School =  StudentManager([Student('Kevin', 1, 9), #Student list ordered: String name, int studentID, float grade
            Student('Kanu', 2, 10),
            Student('Johann', 3, 11),
            Student('Aedan', 4, 12)])

funcs = [School.addStudent,
         School.displayStudent, School.findStudentByID, School.removeStudentImproved, School.UpdateStudentAttributesImproved]
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
    

        


'''
#1. Add Student

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 1
Enter student name: John Doe
Enter student ID: 101
Enter student grade: 85.5


#2. Display All Students/

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 2
ID: 101, Name: John Doe, Grade: 85.5


#3. Find Student by ID

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 3
Enter student ID to find: 101
ID: 101, Name: John Doe, Grade: 85.5


#4. Remove Student by ID

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 4
Enter student ID to remove: 101


#5. Update Student Grade

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 5
Enter student ID to update grade: 101
Student not found.


#6. Exit

Student Management System
Choose one of the following: 
1. Add Student
2. Display All Students
3. Find Student by ID
4. Remove Student by ID
5. Update Student Grade
6. Exit

Choose an option: 6'''
