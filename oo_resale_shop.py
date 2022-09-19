from typing import Dict, Union, Optional
from computer import *
class ResaleShop:
    itemID = 0

    # What attributes will it need?


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, itemID):
    # constructs the resale shop and creates inventory and itemID
        self.inventory = inventory
        self.inventory = {}

        self.itemID = itemID

    # What methods will you need?

    # adds computer to inventory and updates the itemID
    def buy(self, computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        print("Item", self.itemID, "bought!")

    # removes computer from inventory and prints message
    def sell(self):
        if self.itemID in self.inventory:
            del self.inventory[self.itemID]
            print("Item", self.itemID, "sold!")
        else: 
            # prints error message if item cannot be found
            print("Item", self.itemID, "not found. Please select another item to sell.")

    # prints inventory
    def print_inventory(self):
        # If the inventory is not empty_
        for computer in self.inventory:
            if self.inventory:
                    print(self.inventory)
            else:
                # prints that inventory is empty
                print("No inventory to display.")

    # updates price based on year the computer was made, and updates the OS
    def refurbishCheck(self, computer):
        computer.refurbish(computer) # locate the computer
        print("Computer's Price and OS has been updated!")
