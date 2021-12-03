class Day:
    day_input = None

    def __init__(self, input_array=None):
        self.day_input = input_array

    def __is_valid(self):
        return self.day_input is not None

    def part1(self):
        if not self.__is_valid():
            return

        last = 0
        increasing = 0

        for line in self.day_input:
            current = int(line)
            if last == 0:
                last = current
            else:
                if last < current:
                    increasing += 1
                last = current

        print("Part 1: " + str(increasing))

    def part2(self):
        if not self.__is_valid():
            return

        array = []
        increasing = 0

        for line in self.day_input:
            current = int(line)
            array.append(current)
            if len(array) == 4:
                increasing += self.__get_increasing(array)
                array.pop(0)

        print("Part 2: " + str(increasing))

    @staticmethod
    def __get_increasing(array):
        first = array[0] + array[1] + array[2]
        last = array[1] + array[2] + array[3]

        if first < last:
            return 1
        return 0
