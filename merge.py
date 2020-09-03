# Coding=utf-8

import os
import logging
logging.basicConfig()
import rdflib

path="C:/Users/user/Desktop/data"
files = os.listdir(path)
g = rdflib.Graph()
for file in files:
	if not os.path.isdir(file):
		filePath=path+'/'+file
		g.parse(filePath,format='xml')
g.serialize(destination="C:/Users/user/Desktop/data1/lubm2.nt",format="nt")
print(len(g))