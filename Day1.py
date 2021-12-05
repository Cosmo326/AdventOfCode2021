from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)

    def part1(self):
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

        return increasing

    def part2(self):
        array = []
        increasing = 0

        for line in self.day_input:
            current = int(line)
            array.append(current)
            if len(array) == 4:
                increasing += self.__get_increasing(array)
                array.pop(0)

        return increasing

    @staticmethod
    def __get_increasing(array):
        first = array[0] + array[1] + array[2]
        last = array[1] + array[2] + array[3]

        if first < last:
            return 1
        return 0
