bmi = 84 / 1.65 **2

print(bmi) #normal value

print(int(bmi)) #round down

print(round(bmi)) #round up or down to nearest integer

print(round(bmi, 2)) #round up or down to nearest 2 decimal places

score = 0

# User scores a point

score += 1 
print(score)

#f-strings

score = 0
height = 1.80
is_winning = False

print(f"Your Score is = {score}, your height is = {height}, and you are {'winning' if is_winning else 'losing'}")