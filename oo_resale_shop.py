# Imports important functions including information from the computer.py file
from typing import Dict, Union, Optional
from computer import *
# Class definition
class ResaleShop:
    itemID = 0 # Number associated with a computer in the dictionary
    
    def __init__(self, inventory, itemID):
        self.inventory = inventory
        self.inventory = {} # Creates the inventory and makes it a dictionary

        self.itemID = itemID

    # Appends a computer to the inventory, and increments the itemID
    def buy(self, computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        print("Item", self.itemID, "bought!")

    # Deletes a computer from the inventory based off of its ID
    def sell(self):
        if self.itemID in self.inventory:
            del self.inventory[self.itemID]
            print("Item", self.itemID, "sold!")
        else: 
            # prints error message if item cannot be found
            print("Item", self.itemID, "not found. Please select another item to sell.")

    # Prints a list of objects in the inventory
    def print_inventory(self):
        # If the inventory is not empty_
        for computer in self.inventory:
            if self.inventory:
                    print(self.inventory)
            else:
                print("No inventory to display.")

    # Locates the computer and refurbishes it
    def refurbishCheck(self, computer):
        computer.refurbish(computer) # locate the computer
        print("Computer's Price and OS has been updated!")
