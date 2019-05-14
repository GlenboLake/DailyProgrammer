from textwrap import dedent


def solve(times):
    times = [list(map(int, line.split())) for line in times.splitlines()]
    entrances = [t[0] for t in times]
    exits = [t[1] for t in times]
    people = 0
    time_on = 0
    for time in range(min(entrances), max(exits) + 1):
        people += entrances.count(time) - exits.count(time)
        if people:
            time_on += 1
    return time_on


if __name__ == '__main__':
    inputs = ["""\
              1 3
              2 3
              4 5""",
              """\
              2 4
              3 6
              1 3
              6 8""",
              """\
              6 8
              5 8
              8 9
              5 7
              4 7""",
              """\
              15 18
              13 16
              9 12
              3 4
              17 20
              9 11
              17 18
              4 5
              5 6
              4 5
              5 6
              13 16
              2 3
              15 17
              13 14"""]
    for i in inputs:
        print(solve(dedent(i)))