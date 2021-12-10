from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        # super().__init__(["2199943210",
        #                   "3987894921",
        #                   "9856789892",
        #                   "8767896789",
        #                   "9899965678"])

    def part1(self):
        map_array = []
        for line in self.day_input:
            map_array.append(list(map(int, list(line))))

        total_risk = 0
        for y in range(len(map_array)):
            for x in range(len(map_array[y])):
                left = True
                if x - 1 >= 0:
                    left = map_array[y][x] < map_array[y][x-1]
                right = True
                if x + 1 < len(map_array[y]):
                    right = map_array[y][x] < map_array[y][x + 1]
                up = True
                if y - 1 >= 0:
                    up = map_array[y][x] < map_array[y-1][x]
                down = True
                if y + 1 < len(map_array):
                    down = map_array[y][x] < map_array[y + 1][x]

                if left and right and up and down:
                    total_risk += map_array[y][x] + 1

        return total_risk

    def part2(self):
        map_array = []
        for line in self.day_input:
            map_array.append(list(map(int, list(line))))

        low_points = []
        for y in range(len(map_array)):
            for x in range(len(map_array[y])):
                left = True
                if x - 1 >= 0:
                    left = map_array[y][x] < map_array[y][x - 1]
                right = True
                if x + 1 < len(map_array[y]):
                    right = map_array[y][x] < map_array[y][x + 1]
                up = True
                if y - 1 >= 0:
                    up = map_array[y][x] < map_array[y - 1][x]
                down = True
                if y + 1 < len(map_array):
                    down = map_array[y][x] < map_array[y + 1][x]

                if left and right and up and down:
                    low_points.append([x,y])

        basins = []
        basin_sizes = []
        for low_point in low_points:
            basin = self.get_basin(low_point, map_array, [])
            basin.sort()
            if basin not in basins:
                basins.append(basin)
                basin_sizes.append(len(basin))

        basin_sizes.sort()

        return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

    def get_basin(self, low_point, map_array, basin):
        x = low_point[0]
        y = low_point[1]

        if x - 1 >= 0 and map_array[y][x-1] != 9 and str(x-1) + "," + str(y) not in basin:
            basin.append(str(x - 1) + "," + str(y))
            self.get_basin([x-1, y], map_array, basin)
        if x + 1 < len(map_array[y]) and map_array[y][x + 1] != 9 and str(x + 1) + "," + str(y) not in basin:
            basin.append(str(x + 1) + "," + str(y))
            self.get_basin([x + 1, y], map_array, basin)
        if y - 1 >= 0 and map_array[y - 1][x] != 9 and str(x) + "," + str(y - 1) not in basin:
            basin.append(str(x) + "," + str(y - 1))
            self.get_basin([x, y - 1], map_array, basin)
        if y + 1 < len(map_array) and map_array[y + 1][x] != 9 and str(x) + "," + str(y + 1) not in basin:
            basin.append(str(x) + "," + str(y + 1))
            self.get_basin([x, y + 1], map_array, basin)

        return basin
