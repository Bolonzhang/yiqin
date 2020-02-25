#coding:utf-8
import json
import urllib.request
import matplotlib.pyplot as plt
import numpy as np

#调用api
url = 'http://api.tianapi.com/txapi/ncovcity/index?key=e4218f75003f678496bf7be6ebb4b781'
content = urllib.request.urlopen(url).read()
#用json解析数据
json_data=json.loads(content)
cities_data=json_data['newslist'][0]['cities']
#数据分组
city_name=[]
patients_num=[]
cured_num=[]
died_num=[]
for items in cities_data:
    city_name.append(items['cityName'])
for items in cities_data:
    patients_num.append(items['currentConfirmedCount'])
for items in cities_data:
    cured_num.append(items['curedCount'])
for items in cities_data:
    died_num.append(items['deadCount'])
del city_name[-4]
del patients_num[-4]
del cured_num[-4]
del died_num[-4]

#画图
plt.figure('湖北省疫情图',figsize=(10,8))
plt.title('2月21日湖北省疫情图',fontsize=24)
bar_width=0.2
plt.ylim(0,3000)
plt.bar(np.arange(len(city_name)),height=patients_num,width=bar_width,color='b',alpha=0.6,
        label='确诊')
plt.bar(np.arange(len(city_name))+bar_width,height=cured_num,width=bar_width,color='g',alpha=0.6,
        label='治愈')
plt.bar(np.arange(len(city_name))+bar_width*2,height=died_num,width=bar_width,color='r',alpha=0.6,
        label='死亡')

for item in range(len(patients_num)):
    if item==0:
        plt.text(item, 2900, patients_num[item], ha='center', va='bottom')
    plt.text(item,patients_num[item],patients_num[item],ha='center',va='bottom')
for item in range(len(cured_num)):
    if item==0:
        plt.text(item+bar_width, 2800, cured_num[item], ha='center', va='bottom')
    plt.text(item+bar_width,cured_num[item],cured_num[item],ha='center',va='bottom')
for item in range(len(died_num)):
    plt.text(item+bar_width*2,died_num[item],died_num[item],ha='center',va='bottom')

city_name[-1]='神农架'
plt.xticks(np.arange(len(city_name))+bar_width,city_name)
plt.xlabel('城市')
plt.ylabel('人数')
plt.legend()
plt.show()