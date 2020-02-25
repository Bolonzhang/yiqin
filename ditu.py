#coding:utf-8
import json
import urllib.request
from pyecharts.charts import Map
from pyecharts import options as opts

#获取数据
url = 'http://api.tianapi.com/txapi/ncovcity/index?key=e4218f75003f678496bf7be6ebb4b781'
resp = urllib.request.urlopen(url)
content = resp.read()
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

city_name2=[]
for item in city_name:
    if item=='恩施州':
        city_name2.append('恩施土家族苗族自治州')
    elif item=='神农架林区':
        city_name2.append('神农架林区')
    else:
        city_name2.append(item+'市')
#用pyecharts画图
def map_hubei() -> Map:
    c = (
        Map()
        .add("确诊人数", [list(z) for z in zip(city_name2, patients_num)], "湖北")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="湖北省疫情图(截至 2019/2/21 16:00)"),
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                             pieces=[
                                                 {'min':5000,'label':'>=5000'},
                                                 {'min':1500,'max':4999,'label':'1500-4999'},
                                                 {'min':1000,'max':1499,'label':'1000-1499'},
                                                 {'min':500,'max':999,'label':'500-999'},
                                                 {'min':200,'max':499,'label':'200-499'},
                                                 {'max':199,'label':'0-199'}]
                                             )
                        )
        .render("hubei123.html")
        )
    return c
map_hubei()
