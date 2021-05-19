# to make folders of extension type and place the files in sorted order in afolder

import os
import shutil

path=input("Enter name of directory to be sorted: ")
#get all files in dir
listoffiles=os.listdir(path)
#get extensions
for file in listoffiles:
    name,ext=os.path.splitext(file)
    
    ext=ext[1:]
    if ext =='':
        continue
    
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
        
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
        
            

# sort o extensons
