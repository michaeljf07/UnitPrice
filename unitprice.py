"""
For unit price program project.
I used proper software design with dynamic variable creation.

If you use any of this code please give credit to the creator:
- Michael J. Ferreira
"""

from time import sleep

no_of_items = int(input("how many items do you have? "))
details = {} # New dict

# Loop Version
for x in range(no_of_items):
    answer = int(input("What is the toal cost of the unit in $?: "))
    answer2 = int(input("How many total units do you have? "))
    details[f"unit{x}"] = [answer, answer2] # Creates new dictionary key
del x

# Calculations 
# I want to die
unit_price1 = round(details["unit0"][0] / details["unit0"][1], 2)
unit_price2 = round(details["unit1"][0] / details["unit1"][1], 2)
print(f"The unit price of the first item is ${unit_price1} while the second item's unit price is ${unit_price2}")

# Visuals (Not Necessary)
sleep(0.5)
print("Processing")
for i in range(5):
    sleep(0.3)
    print('.')

sleep(1)
# Concluding comparison
if unit_price1 > unit_price2:
    print("The first item is the better deal")
else:
    print("The second item is the better")