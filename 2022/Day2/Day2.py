# Getting data
with open('input.in', encoding='utf-8-sig') as file:
    data = [i.replace(" ", "") for i in file.read().strip().split("\n")]

# View data - testing access
# print(data)

#Combo types in the dictionary format
part_one = {
    "AX": 4, "AY": 8, "AZ": 3,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 7, "CY": 2, "CZ": 6
}


part_one_result = 0
for round in data:
    part_one_result += part_one[round]


# part two
# Changed the values of the outcomes depending on the rules
# X = LOSS, Y = DRAW, Z = WIN
part_two = {
    "AX": 3, "AY": 4, "AZ": 8,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 2, "CY": 6, "CZ": 7
}

part_two_result = 0
for round in data:
    part_two_result += part_two[round]

# Answers
print(f"The answer to Part 1: {part_one_result}")
print(f"The answer to Part 1: {part_two_result}")
