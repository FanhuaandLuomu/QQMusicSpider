#coding:utf-8
#语料预处理 将音乐按性别分类 boy.txt girl.txt other.txt 存入 昵称 音乐列表
#1141275605 打着雨伞的鱼 女, 存在了23年, 1992年7月1日出生, 巨蟹座, 现居辽宁省大连市,
#铁岭是我的无比思念的家乡。  #music#:出人头地 ##m##我的好兄弟 
import os
import time
import cchardet

def writeToFile(filename,gender,sid,nick,musicList): #将信息写入相应的性别文件
	genderDict={0:'_girl2.txt',1:'_boy2.txt',-1:'_other2.txt'}
	f=open(filename+genderDict[gender],'a')  
	f.write(sid+' '+nick+'#music#'+musicList+'\n')
	f.close()

def getInfo(line):
	if u'男' in line.decode('GB18030'):
		gender=1
	elif u'女' in line.decode('GB18030'):
		gender=0
	else:
		gender=-1
	sid=line.split()[0].strip()
	nick=line.split()[1].strip()
	musicList=line.split('#music#')[1].strip()
	return gender,sid,nick,musicList

if __name__ == '__main__':
	t1=time.time()
	for i in xrange(2):
		if os.path.exists('gender_%d.txt' %i):
			os.remove('gender_%d.txt' %i)
	with open('QQMusic/qq_music.txt') as f:
		for line in f:
			gender,sid,nick,musicList=getInfo(line.strip())  #提取性别 昵称 音乐列表信息
			writeToFile('QQMusic/music',gender,sid,nick,musicList)  #将提取的信息按性别写入相应文件

  	f.close()
  	t2=time.time()
  	print 'all time cost:%.2f' %(t2-t1)

