from Day import BaseDay


class Day(BaseDay):
    def __init__(self, input_array):
        super().__init__(input_array)
        # self.__init__(["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"])

    def part1(self):
        epsilon = ""
        gamma = ""
        commonality = []
        for line in self.day_input:
            for i in range(len(line)):
                if len(commonality) < i + 1:
                    commonality.append(0)
                match line[i]:
                    case "0":
                        commonality[i] -= 1
                    case "1":
                        commonality[i] += 1

        for bit in commonality:
            if bit > 0:
                epsilon += "1"
                gamma += "0"
            else:
                epsilon += "0"
                gamma += "1"

        epsilon_value = int(epsilon, 2)
        gamma_value = int(gamma, 2)

        # print("Epsilon: " + str(epsilon) + " = " + str(epsilon_value))
        # print("Gamma: " + str(gamma) + " = " + str(gamma_value))
        return epsilon_value * gamma_value

    def part2(self):
        oxygen = self.get_rating(self.day_input, 0, "O")
        oxygen_value = int(oxygen, 2)
        scrubber = self.get_rating(self.day_input, 0, "CO2")
        scrubber_value = int(scrubber, 2)

        # print("Oxygen Generator Rating: " + str(oxygen) + " = " + str(oxygen_value))
        # print("CO2 Scrubber Rating: " + str(scrubber) + " = " + str(scrubber_value))
        return oxygen_value * scrubber_value

    def get_rating(self, array, index, rating):
        if len(array) == 1:
            return array[0]

        reduced_array = []
        common = 0

        for line in array:
            match line[index]:
                case "0":
                    common -= 1
                case "1":
                    common += 1

        match = "0"
        if common >= 0 and rating == "O" or common < 0 and rating == "CO2":
            match = "1"

        for line in array:
            if line[index] == match:
                reduced_array.append(line)

        return self.get_rating(reduced_array, index + 1, rating)
