#coding:gbk
#天气预报软件，调取百度接口
import urllib2
import json
#查询函数
def weather(city,type='json'):
#拼凑url地址
		url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=B62bffdefac86de01140e7eb207edfd1' %city
		web = urllib2.urlopen(url)
		cont = web.read()
		content = json.loads(cont)
		return content
#输入要查询的地方
city = raw_input('请输入你要查看的城市，我们将立刻告诉您天气：').strip(' ')
print '----------------------------------------------萌萌天气---------------------------------------------------------'
print '下面由萌萌同学为您播报天气，萌萌哒！\n'
#输入的是gbk编码，要转换成unicode
city = unicode(city,'gbk')
#变成utf-8的编码
city = city.encode('utf8')
content = weather(city)
#声明变量
#查询日期
lookday = content['date']
lookday = lookday.encode('gbk')
#详细结果
results = content['results'][0]
weather = results['weather_data']
#查询城市
currentCity = results['currentCity']
currentCity = currentCity.encode('gbk')
#输出到控制台
print '现在是：%s--------您现在的城市是：%s' %(lookday,currentCity)
print '未来三天的天气预报为您奉上：*^*\n'
for day in weather:
	print '''预报时间为：%s
	天气状况是：%s     风力是：%s
	今天的温度为：%s
'''%(day['date'].encode('gbk'),day['weather'].encode('gbk'),day['wind'].encode('gbk'),day['temperature'].encode('gbk'))
print '今天的推荐指数如下：希望给您的生活能够增加精彩哟！！*_*\n'
for zhishu in results['index']:
	print ''' %s指数：
	指数详情：%s
	指数含义：%s
	指数建议：%s
'''%(zhishu['title'].encode('gbk'),zhishu['zs'].encode('gbk'),zhishu['tipt'].encode('gbk'),zhishu['des'].encode('gbk'))
rs = raw_input('退出程序吗？（yes/no）:')






	
		
		
