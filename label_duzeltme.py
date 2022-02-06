import os
crsPath="C:\\Users\\Gökhan\\Downloads\\tasitgiremez.v1i.yolov5pytorch\\valid\\labels\\"
dizi=None
for (dirname, dirs, files) in os.walk(crsPath):
    for filename in files:
        if filename.endswith('.txt'):
            with open(crsPath+filename,"r") as dosya:
                dizi = dosya.readlines()
                a=0
                c=0
                for i in dizi:
                    if i[0]=="0":
                        i=i.replace(i[0],"23",1)
                        dizi[a]=i
                    """
                    elif i[0]=="1":
                        i=i.replace(i[0],"2",1)
                        dizi[a]=i
                
                    elif i[0]=="2":
                        i=i.replace(i[0],"11",1)
                        dizi[a]=i
                    
                    elif i[0]=="3":
                        i=i.replace(i[0],"14",1)
                        dizi[a]=i
                    
                    elif i[0]=="4":
                        i=i.replace(i[0],"23",1)
                        dizi[a]=i
                    
                    elif i[0]=="5":
                        i=i.replace(i[0],"22",1)
                        dizi[a]=i
                      
                    elif i[0]=="6":
                        i=i.replace(i[0],"5",1)
                        dizi[a]=i
                    
                    elif i[0]=="7":
                        i=i.replace(i[0],"6",1)
                        dizi[a]=i
                    
                    elif i[0]=="8":
                        i=i.replace(i[0],"7",1)
                        dizi[a]=i
                    elif i[0]=="9":
                        i=i.replace(i[0],"8",1)
                        dizi[a]=i    
                    """
                    a=a+1
                
                with open(crsPath+filename,"w") as dosya:
                    for b in dizi:
                        dosya.write(dizi[c])
                        c=c+1
        
            