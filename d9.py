

import os

def clear():
    os.system('clear')

bids = []
others = False

def highest():
    high = 0
    for h in bids:
        if h > high:
            high = h
    print(f'highest is {high}')

def bidder():
    name = input("Enter name: ")
    bid = int(input("Enter bid: "))
    others = input("Enter 'yes' or 'no': ").lower()
    
    bids.append(bid)
    

    if others == 'yes':
        others = False
        clear()
        bidder()
    elif others == "no":
        others = True
        highest()

bidder()

