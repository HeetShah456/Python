#leap year
def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return "Leap"
            else:
                return "Not Leap"
        else:
            return "Leap"
a=int(input("Enter the year:"))
print("The year is:",leap_year(a))