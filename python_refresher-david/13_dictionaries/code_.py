friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

# Extract value
friend_ages['Rolf']
# Add a new key with value
friend_ages["Bob"] = 20

# print(friend_ages)

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]
# print(friends[0]['name'])


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")


for k, v in student_attendance.items():
    print(f"{k}: {v}")

# -- Using the `in` keyword --
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student")


# -- Calculate an average with `.values()` --
attendance_value = student_attendance.values()
print(f'The total attendance_value: {sum(attendance_value)}')
print(f'The total number of attendance : {len(attendance_value)}')
print(sum(attendance_value) / len(attendance_value))
