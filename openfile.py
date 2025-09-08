f=open("karotxt.txt","r")
print(f.read())
f.close()#--->always close because save to file and free ram and edit whise some app
print("*"*30)
"""
برای این که ممکنه بات بره فایل رو ببندی میتونی از 
with open()as f
استفاده بکنی
"""
with open("karotxt.txt","r") as F:
    print(F.read())#-->for read all 
print("-"*30)

#برای خواندن یک لاین یا بخشی از لاین ها
"print(f.readline())--->این ارور داره زیرا فایل که بسته شد دوباره باید باز بشه"
with open("karotxt.txt","r") as F:
    print(F.readline())
    print(F.readline())#دو خط اول
    lines=F.readlines()
    for i , line in enumerate(lines,start=1):
        print(f'{i}={line}')
print("-"*30)

with open("karotxt.txt","r")as f:
    for i in f:
        print(i)#چاپ دقسق منتها بین هر خط دو تا اینتر میخورد
    for i in f:
        print(i.strip())    #نمایش بهتر و حذف تب ها و اینتر های اضافی
print("-"*30)
 
with open("karotxt.txt",'a')as f:
    f.write("welcome in my class")
with open("karotxt.txt",'r')as f:
    print(f.read())#یک نکته در دستور رید میتوان عدد نوشت تا به ان تعداد کاراکتر متن را چاپ کند

""" در بین تغیر دادن قسمتی از محتوا"""
with open("karotxt.txt",'r')as f:
    content=f.read()
    new_content=content.replace("f","karo")
with open("karotxt.txt",'w')as f:
    f.write(new_content)
with open("karotxt.txt",'r')as f:   
    print(f.read())