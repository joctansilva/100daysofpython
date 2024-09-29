print("Welcome to the rollercoaster!")
height = int(input("What is your heigth in centimeters? "))

if height >= 120: 
  print("You can ride the rollercoaster at this height.")
  age = int(input("How old are you? "))
  if age <= 12:
    print("Please pay 5$ for the ride.")
  elif age <= 18:
    print("Please pay 10$ for the ride.")
  else:
    print("Please pay 20$ for the ride.")
else:
    print("Sorry, You can`t ride the rollercoaster at this height.")