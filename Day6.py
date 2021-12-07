from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        # super().__init__(["3,4,3,1,2"])

    def part1(self):
        converted_input = []
        broken = self.day_input[0].split(",")
        for item in broken:
            converted_input.append(int(item))

        for day in range(80):
            adds = 0
            for i in range(len(converted_input)):
                if converted_input[i] == 0:
                    adds += 1
                    converted_input[i] = 6
                else:
                    converted_input[i] -= 1

            for i in range(adds):
                converted_input.append(8)

        return len(converted_input)

    def part2(self):
        breakdown = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        max_day = 256
        days = 7
        broken = self.day_input[0].split(",")
        for item in broken:
            breakdown[item] += 1

        remainder = 0
        for day in range(0, max_day, 7):
            adds = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
            if day + days < max_day:
                for offset in range(9):
                    adds[str(offset)] = breakdown[str((days + offset) % 9)]

                breakdown = {"0": breakdown["0"] + adds["0"],
                             "1": breakdown["1"] + adds["1"],
                             "2": breakdown["2"] + adds["2"],
                             "3": breakdown["3"] + adds["3"],
                             "4": breakdown["4"] + adds["4"],
                             "5": breakdown["5"] + adds["5"],
                             "6": breakdown["6"] + adds["6"],
                             "7": adds["7"],
                             "8": adds["8"]}
            else:
                remaining_days = max_day - day
                for extra_day in range(remaining_days):
                    remainder += breakdown[str(extra_day)]

        return breakdown["0"] + breakdown["1"] + breakdown["2"] + breakdown["3"] + breakdown["4"] + breakdown["5"] + breakdown["6"] + breakdown["7"] + breakdown["8"] + remainder
