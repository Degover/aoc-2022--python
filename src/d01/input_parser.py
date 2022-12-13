def parse_calories_per_elf(input):
    calories = []
    sum = 0
    for row in [row.strip() for row in input]:
        if row == "":
            calories.append(sum)
            sum = 0
            continue

        sum += int(row)

    calories.append(sum)
    calories.sort()
    calories.reverse()
    return calories
