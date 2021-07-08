#Object-oriented Programming in Python

class Dog:
    #This functions always runs as soon as the class is called/assigned to a variable. The __init__ defines what arguments the class initially requires.
    def __init__(self, name, age, breed):
        self.name = name #This will assign the argument 'name' values to 'self' a.k.a whatever variable you assigned this class to.
        self.age = age #This will assign the argument 'age' values to 'self' a.k.a whatever variable you assigned this class to.
        self.breed = breed #This will assign the argument 'breed' values to 'self' a.k.a whatever variable you assigned this class to.
        
    def get_name(self): #Defining a function/method that the user can call so it can see what values were assigned to the argument 'name' to a certain object with the class 'Dog' assigned to it.
        return self.name
    
    def get_age(self): #Defining a function/method that the user can call so it can see what values were assigned to the argument 'age' to a certain object with the class 'Dog' assigned to it.
        return self.age
    
    def get_breed(self): #Defining a function/method that the user can call so it can see what values were assigned to the argument 'breed' to a certain object with the class 'Dog' assigned to it.
        return self.breed
    
    def bark(self): #Defining a function/method that just prints 'Bark!'
        print('Bark!')
        
    def add_one(self, x): #Defining a function/method that takes 1 argument 'x' and returns x + 1
        return x + 1
    
    def set_age(self, age): #Defining a function that allows users to change the 'age' value assigned to a certain 'Dog' class.
        self.age = age
        
#Creating an instance of 'Dog' class, assigning it to variable 'd' and passing its name, age and breed values as it requires arguments because of 'def __init__'
d = Dog('Khartie', 10, 'Lhasa Apso')
print(d.get_name()) #Printing the method 'get_name' which will return the 'name' value of 'd'.
print(d.get_age()) #Printing the method 'get_age' which will return the 'age' value of 'd'.
print(d.get_breed()) #Printing the method 'get_breed' which will return the 'age' value of 'd'.

d.set_age(12) #Using the method 'set_age' to reassign a new value to the age argument of the 'Dog' class assigned to variable 'd'.
print(d.get_age()) #Reprinting age of dog to make sure above method is working.

#Creating a second instance of 'Dog' class and assigning it to variable 'd2'. Again, requires an argument values for, 'name', 'age' and 'breed'.
d2 = Dog('Oscar', 14, 'Maltese')
print(d2.get_name()) #Printing the method 'get_name' which will return the 'name' value of 'd2'.
print(d2.get_age()) #Printing the method 'get_age' which will return the 'age' value of 'd2'.
print(d2.get_breed()) #Printing the method 'get_breed' which will return the 'age' value of 'd2'.

#Showing type of object. Returns class __main__.Dog, shows '__main__' because it shows which module the class was loaded out of. Which if you only have 1 file in your program, will always be '__main__'.
print(type(d))

#Showing attribute 'bark' which just prints 'Bark!' to the console. Has no arguments.
d.bark()

#Showing attribute 'add_one' which takes an argument for 'x' and returns 'x + 1'. Hence the print() function.
print(d.add_one(47))
#-------------------------------------------------------------------------------------------------------------------

# Real life example (creating course and student classes/objects)
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_name(self):
        return self.name
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def get_name(self):
        return self.name
        
    def add_student(self, student): #Function to add student to the course
        if len(self.students) < self.max_students: #Only adds if length of 'students' list is less that 'max_students'
            self.students.append(student)
            print(student.get_name(), 'added to class roster Successfully')
        else:
            print(student.get_name(), 'could not be added to class roster, Roster is Full!')
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
            
#Creating Students
student_1 = Student('Nate Cowley', 20, 63)
student_2 = Student('Satoshi Nakamoto', 63, 97)
student_3 = Student('Elon Musk', 45, 89)

#Creating Courses
course_1 = Course('Computing & IT', 2)

course_1.add_student(student_1)
course_1.add_student(student_2)
course_1.add_student(student_3)

for student in course_1.students:
    print(student.name)
    
print(course_1.get_name(), 'Average Grade:', course_1.get_average_grade())
#---------------------------------------------------------------------------------

#Example of 'inheritence' a.k.a having a 'parent' class and 'sub' classes.

class Pet: #This 'Pet' Class acts as the parent class.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')
        
class Cat(Pet): #'Cat' is a sub-class and is assigned a parent by typing it in the parentheses. So now it contains all the methods in 'Pet' class and its own class 'Cat'
    def speak(self):
        print('Meow')
        
class Dog(Pet): #'Dog' is a sub-class and is assigned a parent by typing it in the parentheses. So now it contains all the methods in 'Pet' class and its own class 'Dog'
    def speak(self):
        print('Bark!')
        
cat_1 = Cat('Mittens', 7)
dog_1 = Dog('Max', 6)
cat_2 = Pet('Ruffles', 3)

cat_1.show()
cat_1.speak() #This will speak 'Meow'
dog_1.show()
dog_1.speak() #While this one will speak 'Bark'

cat_2.show()
#cat_2.speak() #This one wont work as it is an instance of the 'Pet' class which has no 'speak' method. Only 'Cat' & 'Dog' have a speak method.