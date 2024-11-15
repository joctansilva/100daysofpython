student_scores = [150, 145, 185, 170, 160, 190, 180, 200, 210, 65, 70, 80, 90, 100]

total_exam_score = sum(student_scores)

print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)

print(max(student_scores))
print(min(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

min_score = 1000
for score in student_scores:
    if score < min_score:
        min_score = score

print(min_score)