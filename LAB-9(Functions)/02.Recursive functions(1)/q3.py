def countVowels(str,i,lst,count):
    if(i==len(str)-1):
        print(count)
        return
    if(str[i] in lst):
        count+=1
    countVowels(str,i+1,lst,count)
str="Shashvat"
lst=['a','e','i','o','u']
countVowels(str,0,lst,0)
