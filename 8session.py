"""دنباله set مجموعه,
                    خواص ان:الف
            تغیر ناپذیر
                    ب
            غیر قابل تکرار
                    ج
            انجام عملیات های ریاضی
                    د
            از نوع داده ها هشینگ
                    ه
            نه اندیس و نه ترتیب مهم نیست-------------------->not ordered
"""
#تا حدودی میتوان گفت ما در اینجا همان عملیات های ریاضی روی یک مجموعه را انجام میدهیم
#دو عنصری نبودن نشان دهنده دیکشنری بودن میباشد
a={1,1,1,1,2,2,3,1,46,7,9}
print(a)
b={1,5,4,9,4}
print(b)

#در مثال پایین متوجه میشیم که ایندکس اصلاا مهم نیست
print("*"*30)
for i in a:
    print(i)#هربار چیزی میاورد

#add
print("*"*30)
a.add(87)#--------------------->در اینجا باید توجه داشت که گذاشتن یک مجموعه تکرار پذیر با ارور مواجه میشود اما تاپل یا فروزینت اینگونه نیست
print(a)

#copy
print("*"*30)
c=set()
c=a.copy()
print(c)

#differance
print("*"*30)
print(a.difference(b))
print(b.difference(a))
#or
print(a-b)#شکل کوتاه تر شده همین تابع

#diffreance_update
print("*"*30)
a.difference_update(b)
b.difference_update(a)#تفاوت در این است که تفاضل را دو مجموعه را دوباره در خود میریزد اپدیت ها همین کار را میکند
print(a,"-----------",b)

#remove and discard
print("*"*30)
a.remove(2)
print(a)
a.discard(999999999999999999)#تفاوت در این است که در دیسکارد اگر عنصر نباشد ارور نمیدهد
print(a)

#intersiction------------>اشتراک گیری  د
print("*"*30)
v=a.intersection(b)#دستور اپدیت ان متغیر نمینویسیم و اشتراک در خود ای جاگذاری میشود
print(v)
#or
print(a&b)#شکل کوتاه تر شده همین تابع

"""کلا ان متد هایی که ایز دارند 
ترو و فالس جواب میدهند"""
#isdisjoin
print("*"*30)
print(a.isdisjoint(b))#اگر اشتراک باشد غلط و نباشد ترو میدهد

#issubset-------------->زیر مجموعه
print("*"*30)
print(a.issubset(b))
#or
print(a<=b)#شکل کوتاه تر شده همین تابع

#issuperset---------------->مجموعه مادر بودن
print("*"*30)
print(a.issuperset)
#or
print(a>=b)#شکل کوتاه تر شده همین تابع

#pop
print("*"*30)
a.pop()#رندم حذف میکند
print(a)#pop هیچ ورودی ندارد

#union
print("*"*30)
print(a.union(b,v))#هر تعداد مجموعه میخواهید با هم اجتماع کنید با کاما مینویسید
print(a|b|v)#خلاصه تر 

#update
print("*"*30)
print(a.update(b))
#or
a |= b#----------------->توجه شود که این عبارت aرا بروزرسانی میکند بنابر این مستقیما نمیتوان در دستور پرینت استفاده کرد
print(a)

#symitric_differance-------------------->xor------>همان حالت هایی که در هیچکدام مشترک نیست
print("*"*30)
print(a)
print(b)
c=a.symmetric_difference(b)#این دستور نیز اپدیت دارد که مثل مثال های ثبلی میباشد
print(c)

"""چند نگته مهم برای دانستن
{"True",0} or{"False",0}
در یک مجموعه باشد یکی در مجموعه در نظر گرفته میشود
"""

#مثال های کاربردی از مبحث مجموعه سیت

"""برنامه ای که عناصر تکراری درون لیست را حذف کند"""
print("*"*30)
number=[1,5,4,9,1,4,5,6,9,8]
number_set=set(number)
print(number_set)

#ایا دو مجموعه با هم اشتراک دارند
print("*"*30)
set_1={1,2,3,4,5,45,89}
set_2={1,5,8,7,6}
a=set_1.isdisjoint(set_2)
if a==False:
        print("yes")
else:
        print("No")

#عناصر منحصر به فرد در مجموعه
set_1={1,2,3,4,5,45,89}
set_2={1,5,8,7,6}
c={}
c=set_1.difference(set_2)
print(c)

#اتحاد دو مجموعه با هم
set_1={1,2,3,4,5,45,89}
set_2={1,5,8,7,6}
print(set_2.union(set_1))

#تک تک برسی کردن یک استرینگ
str_3="karo jafari"
print(set(str_3))

#برسی وجود داشتن یک عنصر در مجموعه
fruits={"apple","banana","kiwi","orange"}
print("banana" in fruits)#بسیار سریعتر از لیست عمل میکند ولی خیلی باید به بود و نبود فاصله دقت بشود

#اجتماع چند مجموعه
set_1={1,2,3,4,5,45,89}
set_2={1,5,8,7,6}
set_3={"ali",54,19}
#از روش سرعتی استفاده گردیده
print(set_1|set_2|set_3)

#مقایسه دو مجموعه
a={1,2,3}
b={3,2,1}
print(a==b)#توجه چون جای ان مهم نیست و فقط اعضا را برسیی میکند که عینا باشد فقط

#پیدا کردن ایمیل تکراری
import random as rand
import string
def email_random():
        user_name=''.join(rand.choices(string.ascii_lowercase+string.digits,k=8))
        domains='@gmail.com'
        email=user_name + domains
        return email
list_email=[]
for i in range(10):
        list_email.append(email_random())

        
print(list_email)
print("*"*30)
#for del again
print(set(list_email))
