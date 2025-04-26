def lenStr(string, count=0):
    if string == "":  
        return count
    return lenStr(string[1:], count + 1)  
string = "Shashvat"
print(lenStr(string))  