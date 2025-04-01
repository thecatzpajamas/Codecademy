# The project was to create a program that will generate a destination year and location then calculate the cost based on the different between the current and generated year.
# The lesson was to demonstrate the import and use of modules.

import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# Vars
cost = Decimal('1.00')
dests = ["Italy", "France", "Germany", "England", "Japan", "New Zealand"]

# Randomizer
rand_time = randint(-1000000, 1000000)
rand_dest = choice(dests)

# Calculate cost
cost_multiplier = dt.datetime.now().year - Decimal(rand_time)
final_cost = abs(Decimal(cost * cost_multiplier)).quantize(Decimal('0.00'))

# Use of custom import 
custom_module.generate_time_travel_message(rand_time,rand_dest,final_cost)
