#coding:utf-8
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.selector import Selector
import time
import re, os
import sys

def getMusListToFile(qqid, line, browser, filename):
	m_url = 'http://g.gogoqq.com/music.htm?uin=%s' % qqid
	browser.get(m_url)
	#time.sleep(2)
	WebDriverWait(browser, 2, 0.5).until(lambda item:item.find_element_by_xpath('//*[@id="list"]').is_displayed())
	time.sleep(1)
	liList = Selector(text = browser.page_source).xpath(u'//*[@id="list"]/li/a')
	mList = []
	for m in liList:
		mus = m.xpath('text()')[0].extract()
		print mus  
		mList.append(mus)
	f = open(filename, 'a')
	string = line + '  #music#:' + '##m##'.join(mList)
	f.write(string + '\n')
	f.close()

if __name__ == '__main__':
	t1 = time.time()
	IE = r'C:\Program Files\Internet Explorer\IEDriverServer.exe'
	print 'start'
	filename = 'sex_music.txt'
	if os.path.exists(filename):
		os.remove(filename)
	browser = webdriver.Ie(IE)
	source_file='1601441611.txt'
	f=open(source_file,'r')
	count=0
	for index,line in enumerate(f.readlines()):
		try:
			if(len(line.split(' '))>1):  #有用户信息
				getMusListToFile(line.split(' ')[0],line.strip(),browser,filename)
				count+=1
				print u'%d 个QQ用户采集完成' %count
		except Exception,e:
			print 'sth err:',e
			continue
		#print '%d 个QQ用户采集完成!' %(index+1)
	f.close()
	browser.close()


