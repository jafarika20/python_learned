class Machine :
    def __init__(self):
        print("Machine created")
        self.data_list=[]
    def add(self,name,model,color,price,horse):
        dictionare_data={
        "name":name,
        "model":model,
        "color":color,
        "price":price,
        "horse":horse
        }
        self.data_list.append(dictionare_data)
    def search_machine(self,name):
        for i in self.data_list:
            if i["name"]==name:
                print(f"Your car --->{i["name"]}\t model:{i["model"]}\n color:{i["color"]}\n price:{i["price"]}\n hourse:{i["horse"]}")
                print("*"*40)
                break
        else:
            print("wrong name .")
            print("*"*40)
    def delet(self,name):
        for i in self.data_list:
            if i["name"]==name:
                x=input("Are you will DELET machine in list:( y/n )?  ")
                if x=='y' or x=='Y':
                    self.data_list.remove(i)
                    print("Ok,delet for all")
                    print("*"*40)
                else:
                    break
        else:
            print("your name can not fond in data list .")
            print("*"*40)
    def show_all_machine(self):
        for i in self.data_list:
            print(f"Your car --->{i["name"]}\t model:{i["model"]}\t color:{i["color"]}\t price:{i["price"]}\t hourse:{i["horse"]}")
            print("*"*40)
cars=Machine()
cars.add("bmw",1384,"black",2000000,4000)
cars.add("kmc",1388,"black",1000000,2000)
cars.add("lambo",1395,"black",1000000,1000)
cars.search_machine("bmw")
cars.delet("pershia")
cars.show_all_machine()
print("\n"*5)
#--------->cabsolation
"""
مخفی سازی یک سری عملکرد ها
ندادن دسترسی مستقیم به یک شی

"""
class bank:
    def __init__(self):
        self.mojode=0
    def show_mojode(self):
        print(self.mojode)
        print("*"*40)
    def variz_shode(self):
        number_sharj=int (input("pleas enter your cash :"))
        self.mojode+=number_sharj
        print(f"varize shode be to{number_sharj}")
        print("*"*40)
    def bardasht(self):
        print("pleas enter your cash for give me :")
        a=int(input("\t"))
        if a<=self.mojode:
            self.mojode-=a
            print("give cash")
            print("*"*40)
        else:
            print("mojode kafi nist")
            print("*"*40)
    def varize(self):
        print("pleas enter your cash for variz :")
        a=int(input("\t"))
        if a<=self.mojode:
            self.mojode-=a
            print("varize shod")
            print("*"*40)
        else:
            print("mojode kafi nist")
            print("*"*40)
melat_bank=bank()
melat_bank.variz_shode()
melat_bank.show_mojode()
melat_bank.bardasht()
melat_bank.show_mojode()
melat_bank.varize()
print("\n"*5)

#انتزاع
"""
پیچیدگی یک کار را به کاربر نمایش  نمیدهیم 
و در عوض یک عمل ساده تر برای دسترسی قرار میدهیم
"""
def class_object(a):
    if a =="melat_bank":
        melat_bank.variz_shode()
        melat_bank.show_mojode()
        melat_bank.bardasht()
        melat_bank.show_mojode()
        melat_bank.varize()
        print("\n"*5)
    elif a=="Machine":
        cars.search_machine("bmw")
        cars.delet("pershia")
        cars.show_all_machine()
        print("\n"*5)
    else:
        print("wrong name")
entza=class_object("Machine")#بدون دسترسی فقط با فراخوانی یک تابع کل متد هی ماشین را اجرا کردیم
print("\n"*5)

#polymorphism------>چند ریختی
"""
برای اینکه یک شی کار های مختلفی انجام بده در حالی 
که کارها متفاوت هستش
"""
class dog:
    def play_sound(self):
        print("bark")
class cat:
    def play_sound(self):
        print("meow")
def play_sounds(obj):
    obj.play_sound()
my_dog=dog()
my_cat=cat()
play_sounds(my_dog)
play_sounds(my_cat)
print("\n"*5)
#inheditens------->وراثت
"""
یک سری ویژگی های مشترک را میتوان
بدون تکرار از یک کلاس به ارث برد

"""
class car:
    def abject(self):
        print("4 tire")
class bmw(car):
    def new_object(self):
        print("anjector and 32 silandr .")
new_car=bmw()
new_car.abject()# متدکلاس کار را به وسیله شی کلاس بی ام دبلیو فراخوانی و استفاده کردیم
new_car.new_object()
print("\n"*30)
