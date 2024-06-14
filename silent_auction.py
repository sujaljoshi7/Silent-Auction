from art import logo

print(logo)
print("Welcome to the secret auction program")
continue_bidding = True
bids = {}

while continue_bidding:
    name = input("What is your name? ")
    bid_amount = input("What is your bid amount? ₹")
    bids[name] = bid_amount
    continue_question = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if continue_question != "yes":
        continue_bidding = False

max_bid = 0
winner = ""
for name in bids:
    bidding_amount = int(bids[name])
    if bidding_amount > max_bid:
        max_bid = bidding_amount
        winner = name
        break
print(f"The winner is {winner} with a bid of ₹{max_bid}.")
