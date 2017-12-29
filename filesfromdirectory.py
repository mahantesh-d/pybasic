import glob,os
path = r'E:\Mahantesh\pybasic\tablesdump'
files = glob.glob(path)
for file in files:
    f=open(file, 'r')
    f.readlines()
    f.close()

