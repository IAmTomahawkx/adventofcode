import math
import os.path


def part1(inp: str) -> int:
    lines = inp.splitlines()
    times = [int(x) for x in lines[0].removeprefix("Time:").split() if x]
    distances = [int(x) for x in lines[1].removeprefix("Distance:").split() if x]
    races = list(zip(times, distances))

    all_wins = []

    for time, dist in races:
        wins = 0
        for ns in range(time):
            if ns * (time - ns) > dist:
                wins += 1

        all_wins.append(wins)

    return math.prod(all_wins)

def part2(inp: str) -> int:
    lines = inp.splitlines()
    time = int(lines[0].removeprefix("Time:").replace(" ", ""))
    dist = int(lines[1].removeprefix("Distance:").replace(" ", ""))


    wins = 0
    for ns in range(time):
        if ns * (time - ns) > dist:
            wins += 1


    return wins







def main():
    day = os.path.split(__file__)[1].removesuffix(".py")

    with open(f"../inputs/{day}.txt") as f:
        inp = f.read()

    part1_solution = part1(inp)

    print(f"\033[1;34mPart 1 solution:\033[39m{part1_solution}")

    part2_solution = part2(inp)
    print(f"\033[1;34mPart 2 solution:\033[39m{part2_solution}")

main()