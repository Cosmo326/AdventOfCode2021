from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)

    def part1(self):
        if not self.is_valid():
            return

        depth = 0
        position = 0

        for line in self.day_input:
            action = line.split(" ")
            match action[0]:
                case "forward":
                    position += int(action[1])
                case "up":
                    depth -= int(action[1])
                case "down":
                    depth += int(action[1])

        print("Part 1: " + str(depth * position))

    def part2(self):
        if not self.is_valid():
            return

        depth = 0
        position = 0
        aim = 0

        for line in self.day_input:
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

