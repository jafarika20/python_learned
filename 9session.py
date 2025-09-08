"""اموزش تابع یا همان فانکشن
def
"""
#دستور هایی که پرانتز باز و بسته دارند تابع نام دارد خود دستور پرینت هم یک از توابع داخلی پایتون میباشد
#حالا خودمان یک تابع میسازیم
"""درست کردن تابع 
len
البته نمیتوان نام  را ان گذاشت بدین وسیله نامش را 
lengh
میگذاریم
"""
print("*"*30)
def lenth(a):
    c=0
    for i in a:
        c+=1
    print(": طول جمله شما برابر است با",c) 
lenth("karo jafari az sanandaj be tehran meravad.") 
a="karo jafari az sanandaj be tehran meravad."   
print(len(a))
print("*"*30)

#----------------------------------------------->اگر از خروجی استفاده کنیم از ریترن استفاده میکنیم
"""یک مثال خوب همان فرمول جایگشت است 
 که به جای انجام دادن یکباره همه فاکتوریل ها
   از یک تابع فاکتوریل استفاده میکنیم
   و نهایتا فرمول را مینویسیم
"""
def fact(a):
    c=1
    for i in range(2,a+1):
        c=i*c
    return c
#اکنون فرمول را با استفاده از استفاده از تابع بالا باز نویسی میکنیم
def jaigasht(n,r):
    return fact(n)/(fact(n-r)*fact(r))
print(jaigasht(10,5))
#یا برای این که کاربر ممکن  ایت جابه جا بنویسد میتوان اینگونه عمل کرد
print(jaigasht(n=10,r=5))
print("*"*30)

"""
دو اصطلاح مهم و نکته دار در بحث تابع :          یک
ارگومان:هنگامی که تابع میسازید ورودی هایی که از کاربر میخواهید بگیرید ارگومان نام دارد
دو
پارامتر: هنگامی که شما تابع ساخته شده را فرا میخوانید ورودی ها پارامتر نام دارد
"""
#-----------------------------------------------
#تابع جمع کردن دو عدد
def add(a,b):
    return a+b
print(add(5,7))
print("*"*30)
#همان کار منتها با تعداد نامحدود
def adder(*numbers):#------------>این نشان دهنده لیست دادن است
    count=0
    for i in numbers:
        count+=i
    return count
print(adder(5,7))
print("*"*30)
"""این تک ستاره به معنای دادن یک لیست است
 که تعداد نامشخص میباشد
 """
#نکته بعدی دو تا ستاره
def display(**info):
    print(info["name"],info["city"])
display(name="karo",age=19,avg=19.5,city="sanandaj")#-->نمیتوان دو کلید هم نام داشت
print("*"*30)

#تابع بازگشتی فاکتوریل
def factor(a):
    if a==1:
        return 1
    else:
        return a*factor(a-1)
print(factor(6))
print("*"*30)

#تابع بازگشتی فیبوناچی
def fibo(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)
#نمایش مجموعه به دلخواه تا رنج        
def list_fibo(n):
    for i in range(0,n+1):
        print(f"fibonacci({i}) =",fibo(i),sep="")
input_list_fibo=int(input("Enter your step for see fibonacci :  "))
list_fibo(input_list_fibo)

#--------------------------------------