def run():
    day_input = open("Day2/input.txt", "r")
    depth = 0
    position = 0
    aim = 0

    for line in day_input:
        action = line.split(" ")
        match action[0]:
            case "forward":
                position += int(action[1])
                depth += aim * int(action[1])
            case "up":
                aim -= int(action[1])
            case "down":
                aim += int(action[1])

    print("Part 2: " + str(depth * position))
