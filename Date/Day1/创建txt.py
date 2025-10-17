fp = open ('note.txt','w')#打开文件w-->write
print('北京欢迎你',file = fp)#将“北京欢迎你”输出到note。txt文件中
fp.close()#关闭文件
