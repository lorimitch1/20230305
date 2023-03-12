import pandas as pd

d= {'name':['小黃','小陳','小呆'],
    'address' : ['台中','台北','高雄'],
    'birthday':['2000/01/01','1980/05/05','1970/12/12']}
df1 = pd.DataFrame(d)
print(df1)

# 二
d=[]
d.append({'name':'小黃','address':'台中','birthday':'2000/01/01'})
d.append({'name':'小陳','address':'台北','birthday':'1980/05/05'})
d.append({'name':'小呆','address':'高雄','birthday':'1970/12/12'})

df2 = pd.DataFrame(d)
print(df2)

# for r in rs:
#     d.append('name':r[0],'address':r[1],'birthday':r[2])
# df2=pd.DataFrame