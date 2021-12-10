from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        # super().__init__(["[({(<(())[]>[[{[]{<()<>>",
        #                   "[(()[<>])]({[<{<<[]>>(",
        #                   "{([(<{}[<>[]}>{[]{[(<()>",
        #                   "(((({<>}<{<{<>}{[]{[]{}",
        #                   "[[<[([]))<([[{}[[()]]]",
        #                   "[{[{({}]{}}([{[{{{}}([]",
        #                   "{<[[]]>}<{[{[{[]{()[[[]",
        #                   "[<(<(<(<{}))><([]([]()",
        #                   "<{([([[(<>()){}]>(<<{{",
        #                   "<{([{{}}[<[[[<>{}]]]>[]]"])

    def part1(self):
        point_total = 0

        for line in self.day_input:
            point_total += self.get_syntax_error_point(line)

        return point_total

    @staticmethod
    def get_syntax_error_point(line):
        opposite = {"(": ")", "[": "]", "{": "}", "<": ">"}
        points = {")": 3, "]": 57, "}": 1197, ">": 25137}
        queue = []

        for instruction in list(line):
            if instruction in ["(", "[", "{", "<"]:
                queue.append(opposite[instruction])
            else:
                expected = queue.pop()
                if instruction != expected:
                    return points[instruction]

        return 0

    def part2(self):
        uncorrupted_lines = []
        for line in self.day_input:
            if self.is_line_uncorrupted(line):
                uncorrupted_lines.append(line)

        points = []
        for line in uncorrupted_lines:
            points.append(self.get_syntax_pointa(line))

        points.sort()

        return points[round(len(points) / 2)]

    @staticmethod
    def is_line_uncorrupted(line):
        opposite = {"(": ")", "[": "]", "{": "}", "<": ">"}
        queue = []

        for instruction in list(line):
            if instruction in ["(", "[", "{", "<"]:
                queue.append(opposite[instruction])
            else:
                expected = queue.pop()
                if instruction != expected:
                    return False

        return True

    @staticmethod
    def get_syntax_pointa(line):
        total_points = 0
        opposite = {"(": ")", "[": "]", "{": "}", "<": ">"}
        points = {")": 1, "]": 2, "}": 3, ">": 4}
        queue = []

        for instruction in list(line):
            if instruction in ["(", "[", "{", "<"]:
                queue.append(opposite[instruction])
            else:
                queue.pop()

        queue.reverse()
        for item in queue:
            total_points = ((total_points * 5) + points[item])
        return total_points
