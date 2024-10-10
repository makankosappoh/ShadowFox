#BEGINNER LEVEL TASK 1- [8th CLASS AND OBJECTS]
#List of friends' names
friends = ["Aditya", "Priya", "Rohan", "Sonal", "Vivek"]
# List of tuples with names and their lengths using list comprehension
Tuple_namelength = [(name, len(name)) for name in friends]
print("List converted to a tuple of friends with their name lengths:")
print(Tuple_namelength)
#-----------------------------------------------------------------------------------------------------------------------------#

my_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}
# Calculate the total expenses for you and your partner
my_total = sum(my_expenses.values())
partner_total = sum(partner_expenses.values())
print("Your total expenses: ", my_total)
print("Your partner's total expenses: ", partner_total)
#-----------------------------------------------------------------------------------------------------------------------------#

#calculate who spent more
if my_total > partner_total:
    print("I spent more than my partner.")
elif partner_total > my_total:
    print("my partner spent more than me.")
else:
    print("Both of us spent the same amount.")
#-----------------------------------------------------------------------------------------------------------------------------#

#Find the category with a significant difference in spending
print("\nExpense differences between me and mine partner: ")
for category in my_expenses:
    difference = abs(my_expenses[category] - partner_expenses[category])
    if difference > 100: #because other than hotel else diff is same as 100
        print(f"Significant difference in {category}: {difference}")
#-----------------------------------------------------------------------------------------------------------------------------#
