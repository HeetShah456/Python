def convert(str):
    str = str.replace(" ","")
    s = sorted(list(set(str)))
    return "".join(s)


print(convert(str = input("Enter a string:")))