import random

def myinput(prompt,low,high):
    while True:
        try:
            number = int(input(prompt))
            if number<=low or number>=high:
                raise ValueError("Wrond input")
            else: 
                return number
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    n=myinput("n=", 10,20)
    mylist1=[]

    for i in range(n):
        a = random.randint(100,500)
        while a in mylist1:
            a = random.randint(100,500)
        mylist1.append(a)
    print(mylist1)

    try:
        print(sum(mylist1)/len(mylist1))
    except ZeroDivisionError as e:
        print(e)
    
    mylist11 = [x for x in mylist1 if x%2==0 ]
    print(len(mylist11))

    mylist12 = [ x for x in mylist1 if x%2==1]
    max1 = max(mylist12)
    index1 = mylist1.index(max1)
    print(max1, index1)

    mylist2 = [x for x in mylist1 if x%2==0]
    print(mylist2)
    min1 = min(mylist2)
    index2 = mylist2.index(min1)
    print(min1, index2)
