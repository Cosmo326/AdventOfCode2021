import re
from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        self.map_array = {}
        # super().__init__(["0,9 -> 5,9",
        #                   "8,0 -> 0,8",
        #                   "9,4 -> 3,4",
        #                   "2,2 -> 2,1",
        #                   "7,0 -> 7,4",
        #                   "6,4 -> 2,0",
        #                   "0,9 -> 2,9",
        #                   "3,4 -> 1,4",
        #                   "0,0 -> 8,8",
        #                   "5,5 -> 8,2"])

    def part1(self):
        count = 0

        for line in self.day_input:
            coordinates = re.split(" -> |,", line)
            x1 = int(coordinates[0])
            x2 = int(coordinates[2])
            y1 = int(coordinates[1])
            y2 = int(coordinates[3])

            locations = []
            if x1 == x2:
                locations = self.get_locations(x1, x2 + 1, min(y1, y2), max(y1, y2) + 1)
            elif y1 == y2:
                locations = self.get_locations(min(x1, x2), max(x1, x2) + 1, y1, y2 + 1)

            for loc in locations:
                if loc not in self.map_array.keys():
                    self.map_array[loc] = 0
                self.map_array[loc] += 1

        for coord in self.map_array.values():
            if coord > 1:
                count += 1

        return count

    def part2(self):
        count = 0

        for line in self.day_input:
            coordinates = re.split(" -> |,", line)
            x1 = int(coordinates[0])
            x2 = int(coordinates[2])
            y1 = int(coordinates[1])
            y2 = int(coordinates[3])

            locations = []
            if x1 != x2 and y1 != y2:
                diff = abs(x1 - x2) + 1
                x_dir = 1
                if x2 < x1:
                    x_dir = -1
                y_dir = 1
                if y2 < y1:
                    y_dir = -1
                for i in range(diff):
                    locations.append(str(x1 + (i * x_dir)) + "," + str(y1 + (i * y_dir)))

            for loc in locations:
                if loc not in self.map_array.keys():
                    self.map_array[loc] = 0
                self.map_array[loc] += 1

        for coord in self.map_array.values():
            if coord > 1:
                count += 1

        return count

    @staticmethod
    def get_locations(x1, x2, y1, y2):
        locations = []
        for x in range(x1, x2):
            for y in range(y1, y2):
                locations.append(str(x) + "," + str(y))

        return locations
