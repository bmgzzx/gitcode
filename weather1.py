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
print '----------------------------------------------��������---------------------------------------------------------'
print '����������ͬѧΪ�����������������գ�\n'
#�������gbk���룬Ҫת����unicode
city = unicode(city,'gbk')
#���utf-8�ı���
city = city.encode('utf8')
content = weather(city)
#��������
#��ѯ����
lookday = content['date']
lookday = lookday.encode('gbk')
#��ϸ���
results = content['results'][0]
weather = results['weather_data']
#��ѯ����
currentCity = results['currentCity']
currentCity = currentCity.encode('gbk')
#���������̨
print '�����ǣ�%s--------�����ڵĳ����ǣ�%s' %(lookday,currentCity)
print 'δ�����������Ԥ��Ϊ�����ϣ�*^*\n'
for day in weather:
	print '''Ԥ��ʱ��Ϊ��%s
	����״���ǣ�%s     �����ǣ�%s
	������¶�Ϊ��%s
'''%(day['date'].encode('gbk'),day['weather'].encode('gbk'),day['wind'].encode('gbk'),day['temperature'].encode('gbk'))
print '������Ƽ�ָ�����£�ϣ�������������ܹ����Ӿ���Ӵ����*_*\n'
for zhishu in results['index']:
	print ''' %sָ����
	ָ�����飺%s
	ָ�����壺%s
	ָ�����飺%s
'''%(zhishu['title'].encode('gbk'),zhishu['zs'].encode('gbk'),zhishu['tipt'].encode('gbk'),zhishu['des'].encode('gbk'))
rs = raw_input('�˳������𣿣�yes/no��:')






	
		
		
