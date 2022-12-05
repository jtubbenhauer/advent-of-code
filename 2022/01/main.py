if __name__ == '__main__':
    with open('data.txt') as data:
        lines = data.read().splitlines()

    current_index = 0
    elf_list = []
    first_value = True

    for line in lines:
        if line:
            if first_value:
                elf_list.append(int(line))
                first_value = False
            else:
                elf_list[current_index] += int(line)
        else:
            current_index += 1
            first_value = True

    current_highest = 0

    for elf_total in elf_list:
        if elf_total > current_highest:
            current_highest = elf_total

    print(current_highest)
