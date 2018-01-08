sodas = ["Coke", "Pepsi", "Mountain Dew"]
candy = ["Snickers", "Twix", "Recess"]

while True:
    choice = input("Would you like a SODA or some CANDY? ").lower()
    try:
        if choice == "soda":
            snack = sodas.pop()
            
        elif choice == "candy":
            snack = candy.pop()
        else:
            print("Sorry I didn't understand that.")
            continue

    except IndexError:
        print("We are all out of {}".format(choice))
    else:
        print("Heres your {}".format(snack))
        