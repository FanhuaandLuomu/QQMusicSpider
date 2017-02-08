#coding:utf-8
# 1601441611#nick#:S mosc#music#:Smile Again ##m##小镇姑娘 (Live) 
# 从qqgoMusicSpider.py得到的qq_music.txt中统计音乐出现的频率
# 将歌曲名称及频率保存至文件 all_music.txt
# 在小规模上实现qq空间背景音乐排行榜~~
from __future__ import division
import cchardet

def getMusList(filename):
	musList=[]
	musSet=[]
	f=open(filename,'r')
	visable=0
	count=0
	for line in f:
		pieces=line.split('#music#:',1)[1].strip()
		for item in pieces.split('##m##'):
			mus=item.strip()
			if len(mus)>0:
				musList.append(mus)
			if len(mus)>0 and mus not in musSet:
				musSet.append(mus)
			#print mus
		count+=1
		if len(pieces)>0:
			visable+=1
	print 'len(musList):'+str(len(musList))
	print 'len(musSet):'+str(len(musSet))
	return musList,count,visable

def getMusDict(musList):
	musDict={}
	for mus in musList:
		musDict[mus]=musDict.get(mus,0)+1  #get 得到字典的value 否则以0表示
	return musDict,sorted(musDict.items(),key=lambda x:x[1],reverse=True) #sorted 排序 第一个参数要可迭代 第二个参数为排序关键字 第三个 倒序

def saveMus(musSorted):
	f=open('all_music.txt','w')
	for index,item in enumerate(musSorted):
		f.write('%s\t%s\t%s\n' %(index+1,item[0],item[1]))
	f.close()

if __name__ == '__main__':
	musList,count,visable=getMusList('../QQMusic/qq_music.txt')
	musDict,musSorted=getMusDict(musList)
	saveMus(musSorted)
	top=100
	print 'len(musSorted):'+str(len(musSorted))
	print u'-------随机收集%d个QQ用户空间音乐列表[其中音乐列表可见的用户有%d个--------]' %(count,visable)
	print u'--------QQ空间热曲TOP%d排行榜--------' %top
	for index,item in enumerate(musSorted[:top]):
		print 'No%d:%s [%d : %.2f%%]' %(index+1,item[0],item[1],item[1]/visable*100)
