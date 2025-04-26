while True:
    n = input("Enter an integer :")
    try:
        n = int(n)
        break
    except ValueError:
        print("Enter an integer..")

