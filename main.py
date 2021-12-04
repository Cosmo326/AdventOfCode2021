from urllib import request

day = 4

print("Running Day " + str(day))

day_input = None
try:
    sessionIdFile = open("SessionId.txt", "r")
    sessionId = sessionIdFile.read()
    req = request.Request("https://adventofcode.com/2021/day/" + str(day) + "/input")
    req.add_header("Cookie", "session=" + sessionId)
    page = request.urlopen(req)

    html_bytes = page.read()
    html = html_bytes.decode("utf8")[:-1]
    day_input = html.split("\n")
except BaseException as ex:
    print("Input not retrieved\n")

Day = getattr(__import__("Day" + str(day)), "Day")
day = Day(day_input)

day.part1()
day.part2()


