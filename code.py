print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("current bill $5.")
    elif age <= 18:
        bill = 7
        print("current bill $7.")
    else:
        bill = 12
        print("current bill $12.")

    want_photo = input("do you want a photo? Type y for yes and n for no :" )
    if want_photo == "y":
        bill += 3
    print(f"Your total bill is :{bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
