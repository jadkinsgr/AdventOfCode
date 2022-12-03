#Build function to pull in the data 
with open('input.in',  encoding='utf-8-sig') as f:
    data = [item.splitlines() for item in f.read().split('\n\n')]
    data = [[int(calorie) for calorie in item] for item in data]

#print(data)

p1 = max([sum(item) for item in data])

p2 = sum(sorted([sum(item) for item in data], reverse=True)[:3])

print(f"Advent Part One Answer: {p1}")
print(f"Advent Part Two Answer: {p2}")