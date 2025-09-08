#تابع ایول
exp="5*(5+6)"
print(eval(exp))

#--------------->pandas
import pandas as pd#--------->use for datacins andتحلیل اماری  چ
#ابتدا با فایل سی اس وی یعنی کاما سیپریتور ولیو ____>داده ها با کاما جدا میشود
import pandas as pd
"""Series"""
samples=pd.Series(['karo','ali'])
print(samples)
print("*"*30)

#create
data={
    "name":['Karo','Ali','Ribvar'],
    "age":[19,20,25]
}
df=pd.DataFrame(data)
print(df)
print("*"*30)

#read
df=pd.read_csv("karocsv.csv")
print(df)
print("*"*30)

#head--------->چون داده ها ممکنه خیلی زیاد باشه برای دیدن قسمت بالایی از این کد 
print(df.head(3))
print("*"*30)

#tail------->چون داده ها ممکنه خیلی زیاد باشه برای دیدن قسمت پایینی از این کد 
print(df.tail(5))
print("*"*30)

#discribe--------->information for table
print(df.describe())
print("*"*30)

#for show column
print(df["age"])
print("*"*30)

#for show row
#عبارت پایین سطر صفر و همه ستون ها میباشد
print(df.iloc[0,:])#کل مشخصات سطر صفر  و سطر ها هم از صفر شروع میشه
print("#"*30)
print(df.iloc[:,:])#برای نمایش همه هم میتوان از این استفاده کرد ولی معمول نیست
print("#"*30)
print(df.iloc[2,0])#سطر دو و ستون صفر
print("*"*30)

#filter
filtered_dataframe=df[df["age"]>20]
print(filtered_dataframe)
print("*"*30)

#sort
sorted_df=df.sort_values("age")#همه رو براساس سن به ترتیب از کوچک به بزرگ چاپ میکنه
print(sorted_df)
print("*"*30)

#subset#------->ساخت یک جدول جدید زیر رشته
subset=df.loc[2:4,["age","name"]]#میگیم از دو تا چهار جدول دی اف رو میخوام و در لیست بعدی هم سطون هایی که میخووام رو مینویسم 
print(subset)
print("*"*30)

#group
df_grouped=df.groupby("age")
print(df_grouped.count())
print("#"*30)
print(df_grouped.max())
print("*"*30)

#add a new column
df["salary"]=[1,2,3,4,5,6]
print(df)
print("*"*30)

#delet a colum
new_df=df.drop("salary",axis=1,inplace=False)#اسم ستون حذفی رو مینویسیم و در کامای بعدی اکسیز رو1میزاریم تا ستونی عمل کنه و اینجا میتونست دستور ادپلیس داشته باشه ترو تا در متغیر جدید سیو نکنیم
print(new_df)
print("*"*30)

#add row
#for lenth number you can use fanction len()--نکته
#نکته چون از صفر میشماریم سطر ها رو از دستور 
df.loc[len(df)]={
    "name":"karo",
    "city":"karaj",
    "age":40
}
print(df)

#تشخیس نه ن داشتن یا نداشتن  مقدار ها ____________>همان خالی ها
print(df.isna())
print("#"*30)
#for delet na or nan
a=df.dropna()
print(a)
print("#"*30)
#for fill na or nan
b=df.fillna(999999)
print(b)
print("*"*30)

#for save file in new data .csv---->write
df.to_csv("Karo_newdata.csv")
#see True or False for تکرار
print(df["salary"].duplicated())