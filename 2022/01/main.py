if __name__ == '__main__':
    with open('data.txt') as sample:
        lines = sample.read().splitlines()

    index = 0
    added_list = []
    first_value = True

    for line in lines:
        if line:
            if first_value:
                added_list.append(int(line))
                first_value = False
            else:
                added_list[index] += int(line)
        else:
            index += 1
            first_value = True

    current_highest = 0

    for elf in added_list:
        if elf > current_highest:
            current_highest = elf

    print(current_highest)
