def run():
    day_input = open("day1input.txt", "r")
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