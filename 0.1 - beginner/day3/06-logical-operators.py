print("Welcome to the rollercoaster!")
height = int(input("What is your heigth in centimeters? "))
bill = 0

if height >= 120: 
  print("You can ride the rollercoaster at this height.")
  age = int(input("How old are you? "))
  if age <= 12:
    bill = 5
    print("Please pay 5$ for the ride.")
  elif age <= 18:
    bill = 10
    print("Please pay 10$ for the ride.")
    #LOGICAL OPERATOR "AND" HERE
  elif age >= 45 and age <= 60: # we can write this on the simple way using: 45 <= age <= 55:
    print("Everything is goint to be ok. Have a free ride on us!")
  else:
    bill = 20
    print("Please pay 20$ for the ride.")

  wants_photo = input("Do you want to have a photo take? Type y for yes or n for no: ")

  if wants_photo == "y":
    bill += 3
  
  print(f"Your final bill is {bill}")

else:
    print("Sorry, You can`t ride the rollercoaster at this height.")