##BEGINNER LEVEL TASK 1- [2ND NUMBERS]
#we create format named function that takes 145 and o as num and char.
def format_example(num, char):
    return format(num, char)
#rturn values as 145 and 'o' and print output.
formatted_string = format_example(145, 'o')
print("Formatted string (octal representation):", formatted_string)
#--------------------------------------------------------------------------------------------------------------------------------#

#Calculate the area of the pond and total water amount
radius = 84  # in meters
pi = 3.14
water_in_a_square_meter = 1.4  # in liters
pond_area = pi * (radius ** 2)
print("Pond Area:", pond_area)
total_water = pond_area * water_in_a_square_meter
print("Total amount of water in the pond (in liters):", int(total_water)) #as we dont need decimal numbers so int(total_water)
#----------------------------------------------------------------------------------------------------------------------------------#

#Calculate speed in metre/seconds
distance = 490  # in meters
time_minutes = 7  # in minutes
time_seconds = time_minutes * 60  # converting time to seconds
speed = distance / time_seconds
print("Speed (in meters per second):", int(speed)) #as we dont need decimal numbers so int(speed)
#----------------------------------------------------------------------------------------------------------------------------------#
