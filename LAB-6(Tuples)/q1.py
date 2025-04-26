lst = [("Shashvat","Devansh","Dax","Tirth"),"Khushi","astha","diya"]
girls=0
for i in lst:
    if(isinstance(i,tuple)):
        print("Number of boys is",len(i))
    else:
        girls+=1        
print("Number of girls is",girls)

    
    


