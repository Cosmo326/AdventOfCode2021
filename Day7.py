from Day import BaseDay
import math


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        # super().__init__(["16, 1, 2, 0, 4, 2, 7, 1, 2, 14"])

    def part1(self):
        split_input = self.day_input[0].split(",")
        positions = []
        for input in split_input:
            position = int(input)
            positions.append(position)

        positions.sort()

        median = 0
        if len(positions) % 2 == 0:
            median = positions[round(len(positions)/2)]
        else:
            a = math.floor(len(positions) / 2)
            b = a + 1
            median = round(positions[a] + positions[b] / 2)

        fuel_consumption = 0
        for position in positions:
            fuel_consumption += abs(position - median)

        return fuel_consumption

    def part2(self):
        split_input = self.day_input[0].split(",")
        positions = []
        for input_value in split_input:
            position = int(input_value)
            positions.append(position)

        mean = float(sum(positions)) / len(positions)

        fuel_consumption_floor = 0
        fuel_consumption_ceiling = 0
        for position in positions:
            distance_floor = abs(position - math.floor(mean))
            distance_ceiling = abs(position - math.ceil(mean))
            fuel_consumption_ceiling += (pow(distance_ceiling, 2) + distance_ceiling) / 2
            fuel_consumption_floor += (pow(distance_floor, 2) + distance_floor) / 2

        return round(min(fuel_consumption_floor, fuel_consumption_ceiling))