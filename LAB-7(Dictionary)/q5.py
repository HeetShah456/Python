d_price = {"Masala":60,"Snacks":50,"Milk":60,"Fruits":100,"Vegetables":110}
d_quantity = {"Masala":3,"Snacks":2,"Milk":1,"Fruits":2,"Vegetables":5}
total=0
for i,p in d_price.items():
    q = d_quantity[i]
    total += p*q


print(total)


