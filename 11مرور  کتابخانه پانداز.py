import pandas as pd
df=pd.read_csv("Karo_newdata.csv")
print(df)
simple=df.dropna()
print(simple)
print("@"*30)
delet_column=df.drop("salary",axis=1)   
print(df)
print(delet_column)
print("@"*30)
data={
    "my_frinds":["Karo Amani","Ali ghosravi","Matin Abdi","Amanj Zandi"]
}
data_created=pd.DataFrame(data)
print(data_created)
print("@"*30)
print(data_created.head(2))
print("@"*30)
print(df.tail(2))
df["salary"].fillna(int(50),inplace=True)
print(df)
print(df["salary"].describe())
print(df["salary"])
print("@"*30)
print(df.iloc[0,:])
df["index"]=[1,2,3,4,5,6,7]
print(df)
new_datas=df.loc[3:5,["city","name","age"]]
print(new_datas)
print("@"*30)
print(df)
print("@"*30)
kaka=df[df["index"]<3]
print(kaka)
sort_value=df.sort_values("age")
print(sort_value)
k=[]
for i in sort_value:
    if i==True:
        k.append(i)
k.append(1)
c=0
for i in k:
    c+=1
if c==1:
    print("False")
else:
    print("True")
new_datas.to_csv("example for pandas.csv")
