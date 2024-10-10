#BEGINNER LEVEL TASK 1- [8th CLASS AND OBJECTS]
#There is list of avengers and superheroes
super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
#Create a class named Avenger with several sub-tasks as:
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader
#------------------------------------------------------------------------------------------------------------------------------------#

#Method to get information about the superhero
    def get_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nSuper Power: {self.super_power}\nWeapon: {self.weapon}"
#------------------------------------------------------------------------------------------------------------------------------------#

#Method to check if the superhero is a leader
    def is_leader(self):
        return f"{self.name} is the leader." if self.leader else f"{self.name} is not the leader."
#----------------------------------------------------------------------------------------------------------------------------------#

#Create six superheroes using the Avenger class
super_heroes = [
    Avenger("Captain America", 100, "Male", "Super strength", "Shield", leader=True),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")
]
# Display the information about each superhero
for hero in super_heroes:
    print(hero.get_info())
    print(hero.is_leader())
    print("\n")
#----------------------------------------------------------------------------------------------------------------------------------#

