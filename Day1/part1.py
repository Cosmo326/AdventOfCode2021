def run():
    day_input = open("Day1/input.txt", "r")
    last = 0
    increasing = 0

    for line in day_input:
        current = int(line)
        if last == 0:
            last = current
        else:
            if last < current:
                increasing += 1
            last = current

    print("Part 1: " + increasing)
