def get_signals(input) -> list[(int, int)]:
    curr_cycle = 0
    x = 1

    for row in [r.strip() for r in input]:
        if row == "noop":
            curr_cycle += 1
            yield (x, curr_cycle)
        else:
            value = int(row.split(" ")[-1])

            curr_cycle += 1
            yield (x, curr_cycle)

            curr_cycle += 1
            yield (x, curr_cycle)
            x += value
