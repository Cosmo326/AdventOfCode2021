from Day import BaseDay
import re


class Day(BaseDay):
    day_input = None

    def __init__(self, input_array):
        super().__init__(input_array)
        # super().__init__(["start-A",
        #                   "start-b",
        #                   "A-c",
        #                   "A-b",
        #                   "b-d",
        #                   "A-end",
        #                   "b-end"])

    def part1(self):
        nodes = self.setup()

        completions = self.path_finder(nodes, "start", [], [], True)

        return len(completions)

    def part2(self):
        nodes = self.setup()

        completions = self.path_finder(nodes, "start", [], [], False)

        return len(completions)

    def setup(self):
        nodes = {}

        for line in self.day_input:
            items = line.split("-")
            if items[0] not in nodes.keys() and items[1] != "start":
                nodes[items[0]] = [items[1]]
            elif items[1] != "start":
                nodes[items[0]].append(items[1])
            if items[1] not in nodes.keys() and items[0] != "start":
                nodes[items[1]] = [items[0]]
            elif items[0] != "start":
                nodes[items[1]].append(items[0])

        return nodes

    def path_finder(self, nodes, current, path, minors, add_minors):
        next_nodes = nodes[current].copy()

        for minor in minors:
            if minor in next_nodes:
                next_nodes.remove(minor)

        if len(next_nodes) == 0:
            return []

        completions = []
        for node in next_nodes:
            if node == "end":
                completions.append("start," + ",".join(path) + ",end")
            else:
                new_minors = minors.copy()
                new_path = path.copy()
                new_path.append(node)

                if not add_minors and node.islower():
                    completions.extend(new_path for new_path in self.path_finder(nodes, node, new_path, new_minors, True) if new_path not in completions)

                if node.islower():
                    new_minors.append(node)

                completions.extend(new_path for new_path in self.path_finder(nodes, node, new_path, new_minors, add_minors) if new_path not in completions)

        return completions
