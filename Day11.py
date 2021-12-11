from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        # super().__init__(["5483143223",
        #                   "2745854711",
        #                   "5264556173",
        #                   "6141336146",
        #                   "6357385478",
        #                   "4167524645",
        #                   "2176841721",
        #                   "6882881134",
        #                   "4846848554",
        #                   "5283751526"])

    def part1(self):
        octo_map = []
        for line in self.day_input:
            octo_map.append(list(map(int, list(line))))

        flashes = 0
        for tick in range(100):
            for y in range(len(octo_map)):
                for x in range(len(octo_map[y])):
                    octo_map[y][x] += 1

            for y in range(len(octo_map)):
                for x in range(len(octo_map[y])):
                    flashes += self.flash(x, y, octo_map)

            for y in range(len(octo_map)):
                for x in range(len(octo_map[y])):
                    if octo_map[y][x] == -1:
                        octo_map[y][x] = 0

            # print(tick, octo_map)

        return flashes

    def flash(self, x, y, octo_map):
        if octo_map[y][x] >= 10:
            octo_map[y][x] = -1
            sub_flashes = 0
            if x - 1 >= 0 and octo_map[y][x-1] != -1 :  # W
                octo_map[y][x-1] += 1
                sub_flashes += self.flash(x-1, y, octo_map)
            if x - 1 >= 0 and y - 1 >= 0 and octo_map[y - 1][x - 1] != -1:  # NW
                octo_map[y - 1][x - 1] += 1
                sub_flashes += self.flash(x - 1, y - 1, octo_map)
            if y - 1 >= 0 and octo_map[y - 1][x] != -1:  # N
                octo_map[y - 1][x] += 1
                sub_flashes += self.flash(x, y - 1, octo_map)
            if y - 1 >= 0 and x + 1 < len(octo_map[y]) and octo_map[y - 1][x + 1] != -1:  # NE
                octo_map[y - 1][x + 1] += 1
                sub_flashes += self.flash(x + 1, y - 1, octo_map)
            if x + 1 < len(octo_map[y]) and octo_map[y][x + 1] != -1:  # E
                octo_map[y][x + 1] += 1
                sub_flashes += self.flash(x + 1, y, octo_map)
            if x + 1 < len(octo_map[y]) and y + 1 < len(octo_map) and octo_map[y + 1][x + 1] != -1:  # SE
                octo_map[y + 1][x + 1] += 1
                sub_flashes += self.flash(x + 1, y + 1, octo_map)
            if y + 1 < len(octo_map) and octo_map[y + 1][x] != -1:  # S
                octo_map[y + 1][x] += 1
                sub_flashes += self.flash(x, y + 1, octo_map)
            if y + 1 < len(octo_map) and x - 1 >= 0 and octo_map[y + 1][x - 1] != -1:  # SW
                octo_map[y + 1][x - 1] += 1
                sub_flashes += self.flash(x - 1, y + 1, octo_map)

            return 1 + sub_flashes
        return 0

    def part2(self):
        octo_map = []
        for line in self.day_input:
            octo_map.append(list(map(int, list(line))))

        flashes = 0
        synchronized = False
        tick = 0
        while not synchronized:
            tick += 1
            for y in range(len(octo_map)):
                for x in range(len(octo_map[y])):
                    octo_map[y][x] += 1

            for y in range(len(octo_map)):
                for x in range(len(octo_map[y])):
                    flashes += self.flash(x, y, octo_map)

            for y in range(len(octo_map)):
                for x in range(len(octo_map[y])):
                    if octo_map[y][x] == -1:
                        octo_map[y][x] = 0

            synchronized_lines = 0
            for y in range(len(octo_map)):
                if all(item == 0 for item in octo_map[y]):
                    synchronized_lines += 1

            synchronized = len(octo_map) == synchronized_lines

        return tick

