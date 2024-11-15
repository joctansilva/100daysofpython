import random

friends = ["Celio", "Joao", "Maria", "Pedro", "Renato", "Thiago"]

#first way
random_friend = random.choice(friends)
print(f"The frient that pay the bill is {random_friend}")

#second way
random_index = random.randint(0, 4)
print(f"The frient that pay the bill is {friends[random_index]}")