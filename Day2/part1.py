def run():
    day_input = open("Day2/day2input.txt", "r")
    depth = 0
    position = 0

    for line in day_input:
        action = line.split(" ")
        match action[0]:
            case "forward":
                position += int(action[1])
            case "up":
                depth -= int(action[1])
            case "down":
                depth += int(action[1])

    print(depth * position)
