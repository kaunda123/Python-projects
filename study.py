import flask as flask

"""x,y=3,5
b1,b2,b3,b4=True,False,x==3,y<3
print(b3)
print(b4)
print(not b1)
print(not b2)
print(not b3)
print(not b4)
print(b1 and b2)
print(b1 or b2)
print(b1 and b3)
print(b1 or b3)
print(b1 and b4)
print(b1 or b4)"""

#q12.
"""user=input("Enter a value between 1 and 100: ")
user1=int(user)
if user1>=1 and user1<=100:
    print("OK")
else:
    print("")"""

#q13.
#i,j,k=3,5,7
"""i,j,k=3,7,5
if i<j:
    if j<k:
        i=j
        #print("i=", i, "j=", j, "k=", k)
    else:
        j=k
        #print("i=", i, "j=", j, "k=", k)
else:
    if j>k:
        j=i
        #print("i=", i, "j=", j, "k=", k)
    else:
        i=k
        #print("i=", i, "j=", j, "k=", k)
print("Comparison:","i=",i,"j=",j,"k=",k)"""

#16.
#a 3=wow
#b 21=whoa
#c 5=6
#d 17=27
#e -5=wow

#17.
#a. first app:0=****,second app:0=*
#b. first app:1=***,second app:1=*
#c. first app:5=***,second app:5=*
#d. first app:50=**,second app:50=*
#e. first app:500=*,second app:500=*
#f. first app:5000=,second app:5000=

#18.
"""import random

num1=int(input("Enter 1st number :"))
#num1=random.randint(0,100)
num2=int(input("Enter 2nd number :"))
#num2=random.randint(0,100)
#num3=int(input("Enter 3rd number :"))
num3=random.randint(0,100)
#num4=int(input("Enter 4th number :"))
num4=random.randint(0,100)
#num5=int(input("Enter 5th number :"))
num5=random.randint(0,100)
numlist=[]
uniquelist=[]
duplicatelist=[]
numlist.append(num1)
numlist.append(num2)
numlist.append(num3)
numlist.append(num4)
numlist.append(num5)
print("My list is :",numlist)
for number in numlist:
    for number2 in numlist[numlist.index(number)+1:]:
        if number==number2:
            duplicatelist.append("Duplicate")
            uniquelist.append("")
        else:
            uniquelist.append("Unique")
            duplicatelist.append("")
print(duplicatelist[0],uniquelist[0],sep="")
maxnum=max(numlist)
minum=min(numlist)
print("Maximum number is :"+str(maxnum),"Minimum number is :"+str(minum),sep="\n")"""

#Chapter 5 exercise
#4.
"""a=0
while a<100:
    print(str(a)+" ",end='')
    a+=1"""
#26.
"""a=0
while a<100:
    print(a,end=" ")
    a+=1
print()
#27.
for i in range(100):
    print(i,end=" ")

#28.
a=0
while a>100:
    print(a,end=" ")
    a+=1
print()

#29.
done=False
n,m=0,100"""
"""while not done and n!=m:
    n=int(input())
    if n<0:
        done=True
    print("n=",n)"""

"""while not done and n!=m:
    n=int(input())
    if n<0:
        break
    print("n=",n)"""
"""from flask import Flask


app=flask.Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello world!</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' %name

if __name__=='__main__':
    app.run(debug=True)"""

#30.
"""x=5
while x>0:
    y=int(input())
    if y==25:
        continue
    x-=1
    print('x=',x)


x=5
while x>0:
    y=int(input())
    x-=1"""

#32.
"""n=int(input("enter number here :"))
if n<1:
    print()
else:
    #box=n*n
    for box in range(n):
        print(n*"{}  ".format("*"))"""

#33.
"""import random
float_list=[]
cnt=0
while len(float_list)<20:
    user=random.randint(0,100)
    #user=int(input("Enter {} numbers :".format(cnt)))
    print(float_list.append(user)
    cnt+=1
print("The sum is :"+str(sum(float_list)),"The average is :"+str(sum(float_list)/len(float_list)),"The minimum is :"+str(min(float_list)),"The maximum is :"+str(max(float_list)),sep="\n")"""

#34.

#Guessing game
"""import random
compInp=random.randint(1,100)
try:
    user1=int(input("Enter number 0<No.<100 to guess: "))
    while user1!=compInp:
        if compInp >=0 and compInp< 25:
            inq = "Is 0<num<25"
            if compInp % 2 == 0:
                muulti=random.choice([2,3,5,6,7,9,10])
                print(muulti)
                if compInp%muulti==0 :
                    multiple="is a multiple of "+str(muulti)
                    even = "number is even"
                    lvar = [inq, even, multiple]
                    ran = random.choice(lvar)
                    print(ran)
                else:
                    even = "number is even"
                    lvar = [inq, even]
                    ran = random.choice(lvar)
                    print(ran)
            else:
                muulti = random.choice([2, 3, 5, 6, 7, 9, 10])
                print(muulti)
                if compInp % muulti == 0:
                    multiple = "is a multiple of " + str(muulti)
                    odd = "number is odd"
                    lvar = [inq, odd, multiple]
                    ran = random.choice(lvar)
                    print(ran)
                else:
                    odd = "number is odd"
                    lvar = [inq, odd]
                    ran = random.choice(lvar)
                    print(ran)

        elif compInp>=25 and compInp<50:
            inq = "Is 25<num<50"
            if compInp % 2 == 0:
                muulti = random.choice([2, 3, 5, 6, 7, 9, 10])
                print(muulti)
                if compInp % muulti == 0:
                    multiple = "is a multiple of " + str(muulti)
                    even = "number is even"
                    lvar = [inq, even, multiple]
                    ran = random.choice(lvar)
                    print(ran)
                else:
                    even = "number is even"
                    lvar = [inq, even]
                    ran = random.choice(lvar)
                    print(ran)
            else:
                muulti = random.choice([2, 3, 5, 6, 7, 9, 10])
                print(muulti)
                if compInp % muulti == 0:
                    multiple = "is a multiple of " + str(muulti)
                    odd = "number is odd"
                    lvar = [inq, odd, multiple]
                    ran=random.choice(lvar)
                    print(ran)
                else:
                    odd = "number is odd"
                    lvar = [inq, odd]
                    ran = random.choice(lvar)
                    print(ran)

        elif compInp>=50 and compInp<75:
            inq="Is 50<num<75"
            if compInp % 2 == 0:
                muulti = random.choice([2, 3, 5, 6, 7, 9, 10])
                print(muulti)
                if compInp % muulti == 0:
                    multiple = "is a multiple of " + str(muulti)
                    even = "number is even"
                    lvar=[inq,even, multiple]
                    ran = random.choice(lvar)
                    print(ran)
                else:
                    even = "number is even"
                    lvar = [inq, even]
                    ran = random.choice(lvar)
                    print(ran)
            else:
                muulti = random.choice([2, 3, 5, 6, 7, 9, 10])
                print(muulti)
                if compInp % muulti == 0:
                    multiple = "is a multiple of " + str(muulti)
                    odd = "number is odd"
                    lvar=[inq,odd, multiple]
                    ran = random.choice(lvar)
                    print(ran)
                else:
                    odd = "number is odd"
                    lvar = [inq, odd]
                    ran = random.choice(lvar)
                    print(ran)

        elif compInp>=75 and compInp<100:
            inq = "Is 75<num<100"
            if compInp % 2 == 0:
                muulti = random.choice([2, 3, 5, 6, 7, 9, 10])
                print(muulti)
                if compInp % muulti == 0:
                    multiple = "is a multiple of " + str(muulti)
                    even = "number is even"
                    lvar = [inq, even, multiple]
                    ran = random.choice(lvar)
                    print(ran)
                else:
                    even = "number is even"
                    lvar = [inq, even]
                    ran = random.choice(lvar)
                    print(ran)
            else:
                muulti = random.choice([2, 3, 5, 6, 7, 9, 10])
                print(muulti)
                if compInp % muulti == 0:
                    multiple = "is a multiple of " + str(muulti)
                    odd = "number is odd"
                    lvar = [inq, odd, multiple]
                    ran = random.choice(lvar)
                    print(ran)
                else:
                    odd = "number is odd"
                    lvar = [inq, odd]
                    ran = random.choice(lvar)
                    print(ran)

        else:
            print("Invalid")
        try:
            user1=int(input("Enter number again 0<No.<100:"))
        except ValueError:
            print("Integers only(0-100) and NO other characters!")


    print("You won !!,number is:" + str(user1))
except ValueError:
    print("Integers only(0-100) and NO other characters!")"""
#Dice roll game
import  random

"""def dice_roll():
    try:
        dice=int(input("Enter 1 to roll dice OR 0 to end game: "))
    except ValueError:
        print("Choose between 0 and 1 ONLY!!, NO other characters")
        dice_roll()
    else:
        if dice==1:
            roll=random.randint(1,6)
            print("You rolled:", roll)
            dice_roll()
        elif dice>1 or dice<0:
            print("Choose between 0 and 1 ONLY!!, NO other characters")
            dice_roll()
        else:
            print("Game Over!!!")


dice_roll()"""
#Email slicer
def email_slicer():
    email=input("Enter your email address: ")
    for sym in email:
         if sym=="@":
             print(str.find(z))

email_slicer()



