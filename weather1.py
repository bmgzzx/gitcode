#coding:gbk
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
print content
#��������
lookday = content['date']
lookday = lookday.encode('gbk')
results = content['results'][0]
currentCity = results['currentCity']
currentCity = currentCity.encode('gbk')
print type(currentCity)
print '�����ǣ�%s***************�����ڵĳ����ǣ�%s' %(lookday,currentCity)





	
		
		
