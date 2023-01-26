print("Welcome to bidding")
record = {}


def ask():
    name = input("Enter your name: ")
    bid = input("Enter your bid: ")
    record[name] = bid


another = True
while another != False:
    ask()
    anyone = input("Are there any other bidder? yes or no.")
    if anyone == "no":
        another = False
names = list(record)
scores = list(record.values())
i = 0
highest = "none"
for z in scores:
    if max(record.values()) == z:
        highest = names[scores.index(z)]
print(f'The highest bid is {max(record.values())} by {highest}')
print()
