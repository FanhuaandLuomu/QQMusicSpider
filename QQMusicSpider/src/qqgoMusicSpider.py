#coding:utf-8
# 从qqgoSpider.py程序爬取到的用户（提取合并为nick.txt）中选择用户爬取
# 爬取相关用户的qq空间背景音乐，保存至qq_music.txt
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.selector import Selector
import time
import re

def getMusList(qqid,qqnick,browser,filename):
	m_url='http://g.gogoqq.com/music.htm?uin=%s' %qqid
	browser.get(m_url)
	time.sleep(1)
	liList=Selector(text=browser.page_source).xpath(u'//*[@id="list"]/li/a')
	mList=[]
	for m in liList:
		mus=m.xpath('text()')[0].extract()
		#print mus  
		mList.append(mus)
	f=open(filename,'a')
	string=qqid+'#nick#'+qqnick+'#music#'+' '.join(mList)
	f.write(string+'\n')
	f.close()
	#return mList


if __name__ == '__main__':
	IE = r'C:\Program Files\Internet Explorer\IEDriverServer.exe'
	print 'start'
	filename = 'qq_music.txt'
	browser = webdriver.Ie(IE)
	source_file='nick.txt'
	f=open(source_file,'r')
	for line in f:
		try:
			qqid=line.split(' ',1)[0]
			qqnick=line.split(' ',1)[1].strip()
			getMusList(qqid,qqnick,browser,filename)
		except Exception,e:
			print 'sth err...',e
			time.sleep(5)
			continue
	f.close()
	browser.close()
	print 'end'