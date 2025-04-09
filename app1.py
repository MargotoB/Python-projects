#import math
#Ex.1
#name = 'John Smith'
#age = 20
#is_new = True

#Ex.2
#name = input("What is your name? ")
#print("Hi, " + name)

#Ex.3
#name = input("What is your name? ")
#color = input("What is your favorite color? ")
#print(name + " likes " + color)

#Ex.4
#birth_year = int(input("Enter birth year: "))
#age = 2024 - birth_year
#print(type(age))
#print(f"Your age is {age}.")

#Ex.5
#weight_lbs = float(input("What is your weight in L(bs)? "))
#weight_kg = weight_lbs * 0.45
#print(weight_kg)

#Ex.6
#course = '''
#Hi John,

#Here is our first email to you.

#Thank you
#The support team
#'''
#print(course)

#Ex.7
#course = 'Python for Begginers'
#print(len(course))
#print(course.upper())
#print(course.find('o'))
#print(course.replace('Begginers', 'Absolute Begginers'))
#print('Python' in course)
#another = course[:]
#print(another)
#name = 'Jennifer'
#print(name[1:-1])
#print(course[0])
#print(course[-1])
#print(course[0:3])
#print(course[1:])
#print(course[:5])

#Ex.8
#x = 2.9
#print(round(x))
#print(abs(-2.9))
#print(math.ceil(2.9))
#print(math.floor(2.9))

#Ex.9
#price = 1000000
#good_credit = True
#if good_credit:
#    down_payment =0.1*price
#else:
#    down_payment = 0.2*price
#print(down_payment)

#Ex.10
#has_high_income = False
#has_good_credit = True
#if has_high_income and not has_good_credit:
#if has_high_income and has_good_credit:
#if has_high_income or has_good_credit: 
#    print("Eligable for loan")

#Ex.11
#name = input("Enter name: ")
#if len(name)<3:
#    print("Name must be at least 3 characters")
#elif len(name)>50:
#    print("Name can be maximum of 50 characters")
#else:
#    print("Name looks good")

#Ex.12
#i =1
#while i<=5:
#    print('*' * i)
#    i=i+1
#print("Done")

#Ex.13
#secret = 9 
#guess_count=0
#guess_limit=3
#while guess_count < guess_limit:
#    guess = int(input("Guess: "))
#    guess_count +=1
#    if guess == secret:
#        print("You win")
#        break
#else:
#    print("Sorry, you failed")

#Ex.14
#command = ""
#started = False
#while True:
#    command = input(">").lower()
#    if command == "start":
#        if started:
#            print("Car is already started")
#        else:
#            started=True
#            print("Car started..ready to go")
#    elif command == "stop":
#        if not  started:
#            print("Car is already stopped")
#        else:
#            started=False
#            print("Car stopped")
#    elif command=="help":
#        print("""
#start - to start the car
#stop - to stop the car
#quit - to exit""")
#    elif command == "quit":
#        break
#    else:
#        print("Ï don't understand that...")

#Ex.15
#prices = [ 10, 20, 30 ]
#total = 0
#for price in prices:
#    total  +=  price
#print(f"Total: {total}")

#Ex.16
#for x in range(4):
#    for y in range(3):
#        print(f"({x},{y})")

#Ex.17
#numbers = [5, 2, 5, 2, 2]
#for x_count in numbers:
    #print('x'*x)
#    output =''
#    for count in range(x_count):
#        output += 'x'
#    print(output)

#Ex.18
#numbers = [2, 4, 32, 45, 1]
#max = numbers[0]
#for number in numbers:
#    if number>max:
#        max=number
#print(max)

#Ex.19
#matrix =[
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
#]
#matrix[0][1]=20
#print(matrix[0][1])
#for row in matrix:
#    for item in row:
#        print(item)

#Ex.20
#numbers = [2, 5, 39, 13, 5]
#numbers.append(20) #добавяме число в края на списъка
#numbers.insert(0, 22) #добавяме число на позиция, която искаме
#numbers.remove(5) #премахваме числото, което искаме
#numbers.clear() #изчистваме целия списък
#numbers.pop() #премахваме последното число от списъка
#numbers.index(5) #проверява дали това число го има в списъка и показва неговия индекс
#numbers.count(5) #проверява колко пъти зададеното число го има в списъка
#numbers.sort() #сортира списъка по възходящ ред
#numbers.reverse() #обръщаме списъка, тоест сега е подреден в низходящ ред
#nums = numbers.copy() #копираме списъка
#print(numbers)

#Ex.21
#numbers = [1,2,3,4,10,3,3,1]
#uniques = []
#for number in numbers:
#    if number not in uniques:
#        uniques.append(number)
#print(uniques)

#Ex.22
#tuples(кортеж) - не може да променяме стойностите в тях, те са непроменящи се
#numbers = (1,2,3)
#print(numbers[0])

#Ex.23
#coord = (1,2,3)
#x = coord[0]
#y = coord[1]
#z = coord[2]
#x,y,z =coord #съкратен вариант на горните 3 реда

#Ex.24
#customer={
#    "name":  "John Smith",
#    "age": 30,
#    "is_verified": True
#}
#customer["name"]="Jack Smith"
#customer["birthdate"]="Dec 3 2004"
#print(customer["name"])
#print(customer.get("name"))
#print(customer.get("bithdate", "Jan 9 2005"))

#Ex.25
#phone = input("Phone: ") 
#digit_mapping={
#    "0": "Zero",
#    "1": "One",
#    "2": "Two",
#    "3": "Three",
#    "4": "Four",
#    "5": "Five",
#    "6": "Six",
#    "7": "Seven",
#    "8": "Eight",
#    "9": "Nine"
#}
#output=""
#for ch in phone:
#    output+=digit_mapping.get(ch, "!") + " "
#print(output)

#Ex.26
#def greet_user(name, last_name):
#    print(f'Hi {name} {last_name} there!')
#    print('Welcome abroad!')


#print("Start")
#greet_user(last_name= "Smith, name = "John"")
#greet_user("Mary", "Tammer")
#print("Finish")

#Ex.27
#def square(number):
#    return number*number


#print(square(3))

#Ex.28
#try:
#    age = int(input("Age: "))
#    income = 20000
#    risk = income/age
#    print(risk)
#except ZeroDivisionError:
#    print("Age can not be zero")
#except ValueError:
#    print("Invalid value")

#Ex.29
#class Point:
#    def move(self):
#        print("move")
#
#    def draw(self):
#        print("draw")


#point1 = Point()
#point1.x = 10
#point1.y=20
#print(point1.x)
#point1.draw()

#point2 = Point()
#point2.x=1
#print(point2.x)

#Ex.30
#class Point:
#    def __init__(self,x,y):
#        self.x=x
#        self.y=y

#point = Point(10,20)
#point.x=12 
#print(point.x)

#Ex.31
#class Person:
#    def __init__(self, name):
#        self.name=name
    
#    def talk(self):
#        print(f"Hi, I am {self.name}")


#John =Person("John Smith")
#John.talk()

#Bob = Person("Bob Smith")
#Bob.talk()

#Ex.32
#class Mammal:
#    def walk(self):
#        print("walk")


#class Dog(Mammal):
#    def bark(self):
#        print("bark")

#class Cat(Mammal):
#    def be_annoying(self):
#        print("annoying")


#dog1= Dog()
#dog1.walk()
#dog1.bark()
#cat1 = Cat()
#cat1.walk()
#cat1.be_annoying()

#Ex.33
#правим нов файл и тези 2 функции ги слагаме в него
#def lbs_to_kg(weight):
#    return weight*0.45


#def kg_to_lbs(weight):
#    return weight/0.45

#след това в този файл пишем следния код
#import converters #името на файла, в който сме вкарали функциите
#from converters import kg-to_lbs
#kg_to_lbs(100)
#print(converters.kg_to_lbs(70))

#Ex.34
import random
#for i in range(3):
#    print(random.random())
#    print(random.randint(10,20))

#Ex.35
#members = ["John" , "Mary", "Bob", "Mosh"]
#leader = random.choice(members)
#print(leader)

#Ex.36
#class Dice:
#    def roll(self):
#        first = random.randint(1,6)
#        second = random.randint(1,6)
#        return first,second
    

#dice = Dice()
#print(dice.roll())

#Ex.37