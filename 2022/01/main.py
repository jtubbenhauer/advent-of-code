import heapq


def parse_data(x):
    with open(x) as data:
        return data.read().splitlines()


def get_three_largest(x):
    return heapq.nlargest(3, x)


def get_most_calories(x):
    most_calories = 0
    for elf_total in x:
        if elf_total > most_calories:
            most_calories = elf_total
    return most_calories


def calculate_elf_calories(x):
    current_index = 0
    elf_list = []
    first_value = True

    for line in x:
        if line:
            if first_value:
                elf_list.append(int(line))
                first_value = False
            else:
                elf_list[current_index] += int(line)
        else:
            current_index += 1
            first_value = True
    return elf_list


if __name__ == '__main__':
    elf_list = calculate_elf_calories(parse_data('data.txt'))

    print(get_most_calories(elf_list))

    print(sum(get_three_largest(elf_list)))
