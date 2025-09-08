"""work with library numpy
numerical python
"""
import numpy as np
arr=np.array([[1,2,3,4,5,6],[1,3,5,4,8,6]])
print(arr)
print("*"*30)
#for see shape
print(arr.shape)
print("*"*30)
#برای تغیر سایز
new_arr=arr.reshape(6,2)
print(new_arr)
print("*"*30)
#برای دیدن ابعاد
print(arr.ndim)
print("*"*30)
#برای دسترسی سریع به یک داده ان ماننده اسلایسینگ استفاده میکنیم
print(arr[1,3])
print("*"*30)
#برای انتخاب بخشی از ان
new_arr_session=arr[0:2,0:3]#-------->ابتدا تکلیف سطر بعد ستون را مشخص میکنیم
print(new_arr_session)
print("*"*30)
#میتوان مقدار  ها رای یکی در میان نمایش داد یا هرگونه بخواهید داده ها را در بیاورید
slice_arr=arr[:,::2]
print(slice_arr)
print("*"*30)
#copy and view
x=arr.copy()
x[0]=0
print(x)
y=arr.view()
y[0]=10
print(arr)#--------->دستور ویو ارایه اصلی را تغیر داد 
for i in arr:
    print(i)
    print("*"*30)
#تک تک عناصر را به علاوه ععددی کردن
print(arr,end="\n\n")
print("payattintion add number for array")
arrr=arr+50
print(arrr)
print("*"*30)
#درست کردن ماتریس یک با هر شکل که خواهی
print(np.ones(shape=(3,4)))
print("| "*30)
#ساختن ماتریس واحد
print(np.eye(3,4))
print("| "*30)
#ساختن ماتریس پیش فرض صفر کامل
print(np.zeros(shape=(3,10)))
print("*"*30)
#