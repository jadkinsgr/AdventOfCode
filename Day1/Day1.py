#Build function to pull in the data 
def get_input(file_name):
#special encoding for my sensitive mac 
    with open(file_name,  encoding='utf-8-sig') as f:
        data = [elf.splitlines() for elf in f.read().split('\n\n')]
    data = [[int(meal) for meal in elf] for elf in data]
    return data

#build part one, which is to get the sum of all values per elf and show the top value
def part_one(data):
    maximum = max([sum(elf) for elf in data])
    return maximum

#build part two which is to sort the top values in reverse order and then sum up the top 3
def part_two(data):
    return sum(sorted([sum(elf) for elf in data], reverse=True)[:3])

#pulling it
def main():
    file_name = r'data.txt'
    data = get_input(file_name)
    print(f"Advent Part One Answer: {part_one(data)}")
    print(f"Advent Part Two Answer: {part_two(data)}")


if __name__ == "__main__":
    main()
