import os
#welcome message
print("Welcome to The Band Name Generator!")
#asking user for their input(what city they live in)
place_of_birth = input("What is name of the city you grew up in?\n")
#asking user for their input again(their pet name)
name_of_pet = input("How is your pet named?\n")
#printing out the result(place of birth and pet's name combination; name of band)
print("Your band name is:\n" + place_of_birth + " " + name_of_pet+"\n")
#waiting for user to close the script with any button
os.system('pause')