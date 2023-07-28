print("Welcome to the tip calculator.")
#total bill input
bill = float(input("What was the total bill? $"))

#Given tips
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_tip = bill * (tip/100)

total_bill = total_tip + bill

print(total_bill)

#number od people
people = int(input("How many people to splite the bill? "))

per_person_bill = total_bill / people
# final_amount = round(per_person_bill,2)

#"{:.2f}".format()

final_amount = "{:.2f}".format(per_person_bill)

print(f"Each person should pay ${final_amount}")