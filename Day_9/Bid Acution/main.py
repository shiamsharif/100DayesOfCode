# clear terminal
import os 

# import logo art in log.py 
from logo import logo
print(logo)

bids = {}
bidding_finished = False

#find heighest bid :
def find_heighest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_Record = {"shiam" : 120,"sharif" : 250}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("Whay is your name?\n")
    price = int(input("Whay is your bid? : $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_heighest_bidder(bids) #called function
    elif should_continue == "yes":
        os.system("cls")  #clear terminal