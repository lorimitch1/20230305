import pandas as pd
# planet = ['水星','金星','地球','火星','木星','土星']
# # s= pd.Series(planet)
# idx = ['mercury','renus','earth','mars','jupiter','saturn']
# s= pd.Series(planet, index=idx)
# print(s[0])
# print(s['mercury'])
# print(s[[0,2,3]])
# print(s[['earth','mars','saturn']])

d={ 'name':'小蔓','address':'台北市','birthday':'2000/01/05'}

p = pd.Series(d)
print(p['address'])
