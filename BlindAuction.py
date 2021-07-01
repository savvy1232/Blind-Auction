bids = {} 

bidding_finished = False

def find_highest_bid(bid_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidder_record:
        bid_amount = bid_record[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
print(f"The Winner is {winner} with a bid of $(highest_bid)")

print("Welcome to the Blind Auction Programme")

while not bidding_finished:
    name = input("What is your Name")
    price = int(input("What is your Bid Price ? : $"))
    bids[name] = price
    shhould_continue =input("Are there any other Bidders remaining , Type yes or no : ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidd
    elif should_continue == "yes":
        print("End")

        