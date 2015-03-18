#coding:utf-8
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
print '--------------------------------------------------------------------------'
#输入的是gbk编码，要转换成unicode
city = unicode(city,'gbk')
#变成utf-8的编码
city = city.encode('utf8')
content = weather(city)
#声明变量
lookday = content['date']
print type(lookday)
#lookday = lookday.encode('utf8')
print lookday
results = content['results'][0]
currentCity = results['currentCity']
print '现在是：'+lookday+'***************您现在的城市是：s' 
print results['weather_data'][3]['weather'] 





	
		
		
