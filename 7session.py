""" بحث دیکشنری dictunary"""
#از دو بخش تشکیل شده که شامل کلید و مقدار میباشد
words={"apple":"سیب","banana":"موز","pen":"خودکار","orange":"پرتقال"}#فاصله بین کلید و مقدار (:) میباشد
print(words.keys())#برای دسترسسی به عناصرکلید مجموعه
print(words.values())#برای دسترسسی به مقدار عناصر
print(words["apple"])#در اینجا اندیس ها همان کلید ها میباشد
words["grap"]="انگور"#برای اضافه کردن یک عنصر از این استفاده میکنیم
print(words)

"""attention for example by dict
b={'karo':18,"karo":20}
print(b)
output={'karo':20}
"""

#با اضافه کردن یک عنصر با تشابه کلید کلید قبلی بروز میشود و هیچ دو کلید همنام در دیکشنری وجود ندارد
words["apple"]="apple"
print(words.items())#میتوان به صورت تاپل هایی ان ها را مشاهده میکند

"""برای برسی عناصر یک مجموعه دیکشنری در حلقه میتوان 
از دو متغیر  استفاده کرد """

for k,v in words.items():#با نوشتن وردس خالی با ارور مواجه میشوید
    print(k,"-"*15,v)

#میخواهیم کدی بنویسیم که کد بالا خط چین های مرتب یا به اصلاح خط چین متغیر داشته باشد
"""lengths=max(len(list(words.keys())))
این کد ارور داره زیرا مستقیما نمیتونی اندازه اون رو محاسبه بکنی در نتیجه
"""
lenghts=max(len(k) for k in words.keys())#پس دیکشنری کمی دسترسی سخت است وباید دقیق تر وغیر مستقیم تر به ان رسید
#یا
"""sep="    " """
lenghts=0
for k in words.keys():
    if len(k) > lenghts:
        lenghts=len(k)
for k,v in words.items():#با نوشتن وردس خالی با ارور مواجه میشوید
    print(k,' '*(lenghts-len(k)),"-"*15,v,sep="")#نکته مهم فهمیدن سپریتور است که در واقع جدا کردن اعضای داخل یک پرینت است که خود پیش  فرض یک اسپیس میباشد
"""ادامه دیکشنری"""
#copy
a=words.copy()
print(a)
print("----------------")

#fromkeys
a=a.keys()
count=100
print(dict.fromkeys(a,count))

#clear
print(words.clear())
print("----------------")

#get
words={"apple":"سیب","banana":"موز","pen":"خودکار","orange":"پرتقال"}
print(words.get('apple'))#or words[apple]کلید گرفته و ولیو تحویل میدهد    .ف
#اما یک تفاوت اصلی با شکل اندیسی دارد که در صورت نبودن کلید ارور نمیدهد     .پ
print("----------------")

#pop
words.pop("pen")#بر اساس کلید ها در اینجا حذف میکنیم
print("----------------")

#popitem------------------حذف میکند اما ان را به صورت کلید و مقدار ریترن میکند<1
a=words.popitem()#اخری را فقط حذف میکند
print(a)
print(words)
print("----------------")

print('*******************')
"""یک نکته برای کم کردن مقدار یک کلید به صورت عدد"""

a=dict.fromkeys(a,count)
a['orange']-=20#نکته مهم ذر وارد کردن کلید استرینگ بودن ان است
print(a)
print('*******************')

#setdifault--------------------------------->برخلاف نامش همان اینزرت کردن است
words.setdefault('bed','تخت')
print(words)
print("----------------")

#update---------------->دیکشنری طور داده میگیرد و میتوان مقادیر متفاوت وارد کرده....iهمان serdefault
#words.update({'apple':'سیف'},{'banana':'موز اکوادر'})      این اشتباه است باید در یک دیکشنری اگر چندتاهم میخوای بنویسی
words.update({'apple':'سیف','banana':'موز اکوادر'})
print(words)



"""دیکشنری تو در تو"""
parints={"reza":{"shadi":15,"neda":10,"mani":23},"fariba":{"male":2,"tale":6},"saltana":{"khawar":50}}#فرض بر برادر خواهرهایی که فرزندلنی با این سن و سال دارند
for k,v in parints.items():#به این ایتمز توجه بشود
    print(k)
    for chaild,age in v.items():
        print(chaild,"is age years old",age)
    print("\n****************")

"""tuple"""
a=(5,8,9,5)
print(a)
print(type(a))
#نکته مهم در تاپل غیر قابل تغیر بودن متغیر های ان است و در صورت تلاش برای تغیر ارور میدهد
#میتواند مقادیر تکراری باشد
print(a.count(5))
print(a.index(5))#فقط اندیس اولی را باز میکرداند

print("_____________________")

"""برای نمایش همه"""
for index,value in enumerate(a):
    if value==5:
        print(index)

        #تفاوت استرینگ و تاپل در یک عددی
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

"""
در تاپل نه میتوان اضافه کرد نه حذف اما میتوان در صورت نیاز از لیست ها استفاده کرد
و از متد های لیست برای این منظور بهره برد
در ادامه با مثال هایی بیشتر نمایش میدهیم
"""
#تاپل را به یک لیست تبدیل کنید تا بتوانید آن را تغییر دهید
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#بری اضافه کردن یک عنصر
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#البته میتوان یک چند تایی را به چند تایی به شکل زیر اضافه کرد
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#برای حذف کردن هم به همین صورت پیش خواهیم رفت
thistuple = ("apple", "banana", "cherry")
y=list(thistuple)
y.pop()
thistuple=tuple(y)
print(thistuple)

#انپکینگorمتغیر تعریف کردن برای همه عناصر یک تاپل
#دسترسی به مقادیر با متغیر دهی منتها باید حتماعداد متغیرها باید با تعداد مقادیر موجود در تاپل مطابقت داشته باشد، در غیر این صورت، باید از علامت ستاره برای جمع‌آوری مقادیر باقیمانده به صورت لیست استفاده کنید
thistuple = ("apple", "banana", "cherry")
(green,yellow,red)=thistuple
print(green)
print(yellow)
print(red)
