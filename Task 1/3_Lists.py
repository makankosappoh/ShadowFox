#BEGINNER LEVEL TASK 1- [3RD LIST]
#creating list named as justice_league with different superheroes.
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
#--------------------------------------------------------------------------------------------------------------------------#

#Calculate the number of members in the Justice League
number_of_members = len(justice_league)
print("Number of members in Justice League:", number_of_members)
#--------------------------------------------------------------------------------------------------------------------------#

#Batman recruited Batgirl and Nightwing as new members
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)
#--------------------------------------------------------------------------------------------------------------------------#

#Move Wonder Woman to the beginning of the list (as the new leader)
justice_league.remove("Wonder Woman") 
justice_league.insert(0, "Wonder Woman") #0 index for 1st member of list
print(justice_league)
#------------------------------------------------------------------------------------------------------------------------#

#Separate Aquaman and Flash by moving Green Lantern between them
justice_league.remove("Green Lantern")
justice_league.insert(4, "Green Lantern") #4th index just after flash and before Aquaman
print(justice_league)
#------------------------------------------------------------------------------------------------------------------------#

#Replace the existing list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)
#-----------------------------------------------------------------------------------------------------------------------#

#Sort the Justice League alphabetically and assign the hero at index 0 as the new leader
justice_league.sort()
new_leader = justice_league[0]
print(justice_league)
print("New leader of the Justice League at 0th index:", new_leader)
#------------------------------------------------------------------------------------------------------------------------#
