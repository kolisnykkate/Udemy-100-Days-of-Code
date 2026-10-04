# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)
bids = {}

while True:
    name = input("What is your name? ")
    price = int(input("What is your bid? "))

    bids[name] = price

    other_bidders = input('Are there any other bidders? Type "yes" or "no": ').lower().strip()

    if other_bidders == "yes":
        print("\n" *100)

    if other_bidders == "no":
        print("\n" *100)
        break

winner = max(bids, key=bids.get)
winning_bid = max(bids.values())
print(winning_bid)
# winning_bid = next(iter(bids.values()))
# for name in bids:
#     if bids[name] > price:
#         winner = name
#         price = bids[name]

print(f"The winner is {winner} with a bid of ${winning_bid}")