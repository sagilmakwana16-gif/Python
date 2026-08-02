## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
#Persons living in flat


## Output 
# Total amount you've to pay is

rent=int(input("Enter your flat rent="))
food=int(input("Enter the amount of food order="))
Electricity_spend=int("Enter the totallectricity spend=")
Charge_per_unit=int("Enter the Charge per unit")
Persons=int(input("Enter the number of persons living in falt="))

total_bill= Electricity_spend * Charge_per_unit

Output=(rent + food + total_bill) // Persons

print("Each person will pay=")
