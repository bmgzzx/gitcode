#coding:utf-8
#����Ԥ���������ȡ�ٶȽӿ�
import urllib2
import json
#��ѯ����
def weather(city,type='json'):
#ƴ��url��ַ
		url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=B62bffdefac86de01140e7eb207edfd1' %city
		web = urllib2.urlopen(url)
		cont = web.read()
		content = json.loads(cont)
		return content
#����Ҫ��ѯ�ĵط�
city = raw_input('��������Ҫ�鿴�ĳ��У����ǽ����̸�����������').strip(' ')
print '--------------------------------------------------------------------------'
#�������gbk���룬Ҫת����unicode
city = unicode(city,'gbk')
#���utf-8�ı���
city = city.encode('utf8')
content = weather(city)
#��������
lookday = content['date']
print type(lookday)
#lookday = lookday.encode('utf8')
print lookday
results = content['results'][0]
currentCity = results['currentCity']
print '�����ǣ�'+lookday+'***************�����ڵĳ����ǣ�s' 
print results['weather_data'][3]['weather'] 





	
		
		
