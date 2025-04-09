import random 

#дефинираме функция, която ще проверява дали въведената стойност ще е в зададения интервал
def myinput(prompt,low,high):
    while True:
        try:
            number = int(input(prompt))
            if number<=low or number >=high:
                raise ValueError("Invalid number")
            else:
                return number
        except ValueError as e:
            print(e)

#създаваме променлива, която ще бъде в зададения в условието интервал, за да показва от колко елемента ще се съдържа списъкът
if __name__ == "__main__":
    n = myinput("n=", 20, 30)
#създаваме празен списък
    mylist1=[]
#в този празен списък ще генерираме случайни числа(спрямо променливата) в определен интервал
    for i in range(n):
        mylist1.append(random.randint(-100,100))
    print(mylist1)

#намираме сумата на елементите на списъка, чиито индекси са нечетни
    mylist11 = [mylist1[i] for i in range(1, len(mylist1), 2)]
    print(sum(mylist11))

#намираме броят на елементите от списъка, чиято цифра на единиците е кратна на 2
    mylist12 = [x for x in mylist1 if x % 10 % 2==0]
    print(mylist12)
    print(len(mylist12))

#намираме произведението на числата, които са отрицателни и четни като принтираме тяхното произведение
    mylist13 = [x for x in mylist1 if x<0 and x % 2==0]
    product = 1
    for element in mylist13:
        product *= element
    print(product)

#създаваме втори списък, който да включва тези елементи от първия списък, които са по-големи от n
    mylist2 = [x for x in mylist1 if x > n]
    print(mylist2)

#да се намери разликата между елемента с максимална стойност и елемента с минимална стойност в списъка
    print(max(mylist2) - min(mylist2))

#да се принтират нечетните числа от този списък и техния брой
    mylist21 = [x for x in mylist2 if x %2 != 0]
    print(mylist21)
    print(len(mylist21))

#да се изтрие елемента с минимална стойност от списъка 
    min_even = min(mylist2)
    mylist2.remove(min_even)
    print(mylist2)



