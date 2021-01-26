import os
isFile = ['configure','Makefile','vif-core','core-daemon','compile','missing','install-sh','depcomp','core-gui','README','freebsd8-config-CORE','Changelog','freebsd7-config-CORE','freebsd7-config-COREDEBUG','changelog','control','compat','rules','copyright','README-Xen','sampleIPsec','sampleIPsec','sampleVPNServer','sampleFirewall','sampleVPNClient','controlnet_updown','LICENSE','vnoded','netns','vcmd','core-manage','core-manage','core-cleanup','core-xen-cleanup','coresendmsg','coresendmsg','stamp-h1']
Dir = os.getcwd()+'/core-rel-4.8'
explored=0
word = input("Please type the word ")
def pDir(Dir,word):
	explored=0
	try:
		for i in os.listdir(Dir):
			explored +=1
			if (len(i.split("."))>=2) or (i in isFile):
				pfile(Dir+'/'+i,word)
				#print(Dir+'/'+i)
				#print(Dir)
			else:
				#print("debug")
				#pfile(Dir+'/'+i)
				pDir(Dir+'/'+i,word)
				#print(i,explored)
	except: 
		os.system("cat " +Dir +" | grep "+word)

def pfile(filename,word):
	try:
		File = open(filename,'r')
		print("--------------"+filename+"------------")
		os.system("cat " + filename +" | grep "+word)
		#os.system("cat "+filename)
	except:
		pDir(filename,word)
		

print(pDir(Dir,word))


def getsubdir(Dir):
	explored=0
	for i in os.listdir(Dir):
		explored +=1
		if (len(i.split("."))>=2) or (i in isFile):
			#pfile(Dir+'/'+i)
			print(Dir+'/'+i)
			#print(Dir)
		else:
			print("debug")
			#pfile(Dir+'/'+i)
			pDir(Dir+'/'+i)
			print(i,explored)

#Another way to do this is by checking if python can open the file since the os.path.isdir() and os.path.isfile() doesn't work. If python can not open it than we process it as a file. 'for i in os.listdir line is the line before the 
'''
try:
	filename = open(dir+'/'+i,'r')
except 
	pfile(dir+'/'+i,'r') i should really be added with dir
This simple change will allow it to search throug any file and any directory as it will be able to distinguish between file and directory
'''
#getsubdir(5)
#filename = open(Dir, 'r')
