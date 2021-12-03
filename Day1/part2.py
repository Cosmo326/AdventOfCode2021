def __get_increasing(array):
    first = array[0] + array[1] + array[2]
    last = array[1] + array[2] + array[3]

    if first < last:
        return 1
    return 0


def run():
    day_input = open("Day1/input.txt", "r")
    array = []
    increasing = 0

    for line in day_input:
        current = int(line)
        array.append(current)
        if len(array) == 4:
            increasing += __get_increasing(array)
            array.pop(0)

    print("Part 2: " + increasing)
