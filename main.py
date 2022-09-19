# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
#from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish
from computer import *
from oo_resale_shop import *

def main():
    resaleshop = ResaleShop([],0)
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    print("Buying")
    print("Adding to inventory...")
    resaleshop.buy(computer)
    resaleshop.print_inventory()
    resaleshop.refurbishCheck(computer)
    resaleshop.sell()
    resaleshop.print_inventory()

# Calls the main() function when this file is run
if __name__ == "__main__": main()
