""" دستورات حلقه ها"""

#ایا عدد اول است یا خیر؟
n=int(input("Enter n :"))
counte=0
for i in range(1,n+1):
    if n%i==0:
        counte+=1
if counte==2:
    print("aval")
else:
    print("aval nist")
   
#برنامه ای بنویسید که مثبت یا منفی بودن عدد را تشخیص بدهد

if n>0:
    print('postive')
elif n<0:
    print('nagetive')
else:
    print("zero is honsa") 

#عکس کردن ترتیب یک عدد

for i in range(12):
    print(n%10,end="")
    n=n//10
    if n==0:
        break #به معنای قطع کردن دستور میباشد

#همین کد قبلی منتها ما ابتدا در یک لیست قرار داده و سپس عکس کرده
a=[]
n=input('enter n')
for i in range(len(n)):
   a+=n[i]
print(a[::-1])
#کد بالا به صورت خیلی ساده تر
a=list(n)
print(a[::-1])

#درست کردن جدول ضرب

for i in range(1,10):
    for j in range(1,10):
        print(i*j ,end=" \t")
    print()
#فاکتوریل
n=6
c=1
for i in range(1,n+1):
    c=c*i
    print(c)
"""استفاده از حلقه به طور تعداد نامشخص
while:"""
#همان کد برعکس کردن اعداد چون ما مطمِین نیستیم که کاربر بیشتر از دوازده وارد نمیکند بهتر است از حلقه وایل استفاده کنیم
n=int(input("Enter n :"))
while n!=0:
    print(n%10,end="")
    n=n//10
print()

#درست کردن جدول ضرب با while:
colm=1

while colm != 10:
    row=1#نکته مهمی است زیرا این متغیر اکیدا باید درون حلقه اجرا شود زیرا بعد از رسیدن به نه شرط بعدی که داخلی است یچوقت انجام نمیگیرد
    while row !=10:
        print(colm*row, end ="\t")
        row+=1
    print()
    colm+=1