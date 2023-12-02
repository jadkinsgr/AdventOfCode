import re

# Dictionary mapping spelled-out numbers to digits
number_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# Open and read the file for both parts
with open('input.in', 'r') as file:
    lines = file.readlines()

# Initialize sums for both parts
total_sum_part_one = 0
total_sum_part_two = 0

# Iterate through each line for both parts
for line in lines:
    # Part one
    first_num_part_one = re.search(r'\d', line).group()
    last_num_part_one = re.findall(r'\d', line)[-1]
    two_digit_num_part_one = int(first_num_part_one + last_num_part_one)
    total_sum_part_one += two_digit_num_part_one

    # Part two
    line_part_two = line
    for number, digit in number_mapping.items():
        line_part_two = line_part_two.replace(number, digit)
    first_num_part_two = next(int(s) for s in line_part_two if s.isdigit())
    last_num_part_two = next(int(s) for s in line_part_two[::-1] if s.isdigit())
    two_digit_num_part_two = int(str(first_num_part_two) + str(last_num_part_two))
    total_sum_part_two += two_digit_num_part_two

# Print the total sums for both parts
print("Total sum for part one:", total_sum_part_one)
print("Total sum for part two:", total_sum_part_two)