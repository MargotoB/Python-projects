import random

#дефинираме функция, която ще проверява дали въведената стойност ще е в зададения интервал
def myinput(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
            if number <= low or number >= high:
                raise ValueError("Invalid number...")
            else:
                return number
        except ValueError as e:
            print(e)


#създаваме променлива, която ще бъде в зададения в условието интервал, за да показва от колко елемента ще се съдържа списъкът
if __name__ == "__main__":
    n = myinput("n=", 15, 35)
#създаваме празен списък
    mylist1 = []
#в този празен списък ще генерираме случайни числа(спрямо променливата) в определен интервал
    for i in range(n):
        # mylist1.append(random.randint(30, 300))
        mylist1.append(myinput(f"{i+1}=", 30, 300))
    print(mylist1)
#намираме броят на елементите от списъка, чиято цифра на десетиците е кратна на 3
    mylist11 = [x for x in mylist1 if x//10 % 10 % 3 == 0]
    print(len(mylist11))

#намираме индекса на елемента с минимална стойност в този списък, който има остатък 4 при целочислено деление на 6
    mylist12 = [x for x in mylist1 if x % 6 == 4]
    min1 = min(mylist12)
    index = mylist1.index(min1)
    print(min1, index)

#създаваме нов списък, който да включва елементите на първия, които са двуцифрени и кратни на 2 и 3
    mylist2 = [x for x in mylist1 if 9 < x <
               100 and (x % 2 == 0 or x % 3 == 0)]
    print(mylist2)
#намираме средноаритметично на елементите на списъка, чиито индекси са нечетни
    mylist22 = [mylist2[i] for i in range(1, len(mylist2), 2)]
    try:
        print(sum(mylist22)/len(mylist22))
    except ZeroDivisionError as e:
        print(e)

#изтриваме минималното четно число от mylist22
    mylist23 = [x for x in mylist2 if x % 2 == 0]
    try:
        min_even = min(mylist23)
        print(min_even)
        mylist2.remove(min_even)
        print(mylist2)
    except ValueError:
        print("No such data...")



# //10 премахва цифрата на единиците 
# %10 премахва цифрата на стотиците 
        