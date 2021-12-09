from Day import BaseDay


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        # super().__init__(["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        #                   "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        #                   "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        #                   "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        #                   "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        #                   "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        #                   "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        #                   "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        #                   "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        #                   "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"])

    def part1(self):
        count = 0
        for line in self.day_input:
            result = line.split(" | ")[1].split(" ")
            for digit in result:
                if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                    count += 1

        return count

    def part2(self):
        total = 0
        for line in self.day_input:
            parts = line.split(" | ")
            all_digits = []
            for i in parts[0].split(" ") + parts[1].split(" "):
                char_array = list(i)
                char_array.sort()
                all_digits.append(''.join(char_array))
            digits = ["", "", "", "", "", "", "", "", "", ""]

            for i in all_digits:
                if i not in digits:
                    if len(i) == 2:
                        digits[1] = i
                    elif len(i) == 4:
                        digits[4] = i
                    elif len(i) == 3:
                        digits[7] = i
                    elif len(i) == 7:
                        digits[8] = i

            for i in all_digits:
                if i not in digits:
                    if len(i) == 5 and all(item in list(i) for item in list(digits[1])):
                        digits[3] = i
                    elif len(i) == 6 and all(item in list(i) for item in list(digits[4])):
                        digits[9] = i

            for i in all_digits:
                if i not in digits:
                    if len(i) == 5 and all(item in list(digits[9]) for item in list(i)):
                        digits[5] = i

            for i in all_digits:
                if i not in digits:
                    if len(i) == 5 and i != digits[3] and i != digits[5]:
                        digits[2] = i
                    elif len(i) == 6 and all(item in list(i) for item in list(digits[5])):
                        digits[6] = i

            for i in all_digits:
                if i not in digits:
                    if len(i) == 6 and i != digits[6] and i != digits[9]:
                        digits[0] = i

            digit = ""
            for i in parts[1].split(" "):
                item = list(i)
                item.sort()
                digit += str(digits.index(''.join(item)))

            total += int(digit)

        return total
