# Imports important functions
from typing import Dict, Union, Optional
# Class definition
class Computer:
    
    # Constructor sets up the computer's attributes
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    def update_price(self, new_price):
        self.price = new_price # Sets the price of the computer to the new price as defined in the refurbish method

    def refurbish(self, computer):
        # Determines what price the computer should be set to based off of its year made
        if int(computer.year_made) < 2000:
            computer.update_price(0) # too old to sell, donation only
        elif int(computer.year_made) < 2012:
             computer.update_price(250) # heavily-discounted price on machines 10+ years old
        elif int(computer.year_made) < 2018:
            computer.update_price(550) # discounted price on machines 4-to-10 year old machines
        else:
             computer.update_price(1000) # recent stuff
        # Adjusts the operating system of the computer to a new one
        if self.operating_system is not None:
            computer.operating_system = "new_os" # update details after installing new OS
