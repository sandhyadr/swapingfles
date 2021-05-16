def swapFileData():
    fil1=input("Enter the file1 name :")
    file2=input("Enter 2nd file name:")
    a=open(fil1,'r')
    data_a= a.readlines()
    print(data_a)
    a.close()
    b=open(file2,'r')
    data_b=b.readlines()
    print(data_b)
    b.close()
    a=open(fil1,'a')
    a.writelines(data_b)
    a.close()
    b=open(file2,'w+')
    b.writelines(data_a)
    b.close()
    
    
swapFileData()    
    
    
    
    