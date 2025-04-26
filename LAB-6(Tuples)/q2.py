lst =[("Shashvat Patel","24BCP308",18),("Devansh Tilala","24BCP268",18),("Dax Patel","24BCP269",17)]
names, rollno, age = [],[],[]
for i in lst:
        if(isinstance(i,tuple)):
            names.append(i[0])
            rollno.append(i[1])
            age.append(i[2])
            
print("List of names:",names)
print("List of roll no's:",rollno)
print("List of ages:",age)
