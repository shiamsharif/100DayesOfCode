print("Welcome to the RollerCoaster!")
height = int(input("What is your Height in cm? "))
bill = 0

if height >= 120:
    print("You can ride rollercoaster. :)")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You don't  have to pay.")
    else:
        bill = 12
        print("Please pay $12.")
    
    wants_photo = input("Do you want a photo? y OR n :  ")
    if wants_photo == "Y":
        #add $3 to take a photo
        print(f"Your Total bill is ${bill+3}")
    else:
        print(f"Your total bill is ${bill}")
else:
    print("SORRY, you have to grow taller before you can ride. :(")