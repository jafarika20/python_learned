"""خواندن دو دستور بریک و کانتنیو
break:برای شکستن
continue:
"""
#دستور break
n=int(input("Enter the number :"))
for i in range(12):
    print(n%10,end="")
    n=n//10
    if n==0:
        break #به معنای قطع کردن دستور میباشد
print()

#عدد ارم استرانگ 
"""توضیح کلی درباره عدد ارم استرانگ:
عددی میباشد که  اگر تک تک ارقام ان را به توان سایز عدد برسانید
وان را جمع کنید خود عدد دوباره بدست میاید"""
n=input("Enter the number :")
lenth=len(n)
count=0
for i in n:#
    count+=int(i)**(lenth)
if count==int(n):
        print("Arm strang")
else:
        print("not Armstrang")
#استفاده از یک روش بهینه تر برای تشخیص عدد ارم استرانگ
"""این روش خیلی سریع تر و کم جا گیرتر است زیرا مستقیما با اعداد
سرو کار دارد و نکته ان یک فرمول ریاضی است که مود در واقع همان
رقم یکان عدد را به ما میدهد وهمچنین جزع صحیح ان عدد را دوباره بدون باقیمانده قبلی میدهد
"""
n=int(input("Enter the n for armstrang :"))
t=n
s=0
while n!=0:
    s=s+(n%10)**3
    n=n//10
if s==t:
    print("Arm strang")
else:
    print("not Armstrang")     
#قطعه کدی که مشخص کند  که تعداد رشته هایی که عضو اخر و اول ان ماننده هم هستند
list_1=['abc','xyz','aba','1221']
c=0
for i in list_1:
     if i[0]==i[-1]:#با ای ما به عناصر لیست و با اسلایس ای میتوان به داخل رشته های ان نفوذ کرد
        c+=1
print(c)
#پیدا کردن مشترکات بین دو لیست
count=0
karol1=['abc','efg','ali',"ahmad"]
karol2=[123,'karo','ali',18,93,'ajib']
for i in karol1:
    for j in karol2:
        if i==j:
            count+=1
print(count)
"""continue"""
numbers=[]
for i in range(10):
    n=int(input("enter numbers"))
    if n<0:
        continue
    numbers.append(n)
    print('add')
print(numbers)

"""_________________________________________"""

numberss=[]
for i in range(10):
    if c==3:
        print('pleas try again later')
        break
    if n>0:
        c+=1
        continue
    numberss.append(n)
    print("add")
print(numberss)

"""یک تمرین برای گرفتن حداکثر پنج شماره از کاربر"""

number=[]
names=[]
a=['+','!','@','#','$','%','^','*',')','=','+','(']
def number_you():
    while True:
        a=input("for Enter name(y or n)")
        if ('n' or 'N')in a:
            break
        while True:
            nam=input("what's your name ?")
            if any(c in nam for c in a):
                print("please enter your name True :")
            else:
                names.append(nam)
                print("add name",nam,"in the list .")
                break
    while True:
        a=input("for Enter number(y or n)")
        if ('n' or 'N')in a:
            break
        numb=input("Please enter your number :  ")
        l=len(numb)
        if l!=11:
            print("number len != 11 :   maby not zero phone")
            continue
        else:
            print("number for you is",numb)
            number.append(numb)
    print(list(zip(number,names)))
number_you()