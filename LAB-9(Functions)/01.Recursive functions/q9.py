def count_alpha_digits(str):
    d = {"alphabets":0,"digits":0}
    for i in str:
        if(i.isalpha()):
            d["alphabets"]+=1
        elif(i.isdigit()):
            d["digits"]+=1
    return d

print(count_alpha_digits(str = input("Enter a string:")))