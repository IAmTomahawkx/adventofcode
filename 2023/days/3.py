import math
import os.path
import re

def part1(inp: str) -> int:
    comp = re.compile("\d+")
    ints = []

    map_ = inp.split("\n")
    for ridx, row in enumerate(map_):
        for match in comp.finditer(row):
            places = [(ridx, match.start() - 1), (ridx, match.end())]
            places += [(ridx + 1, match.start() + a) for a in range(-1, len(match.group(0)) + 1)] # below
            places += [(ridx - 1, match.start() + a) for a in range(-1, len(match.group(0)) + 1)] # above

            if any(
                    (
                        ((len(map_[0]) - 1 > x > -1) and (-1 < y < len(map_) - 1)) # location exists
                        and (not map_[x][y].isdigit() and map_[x][y] != ".") # is symbol
                    ) for x, y in places):
                ints.append(int(match.group()))

    return sum(ints)




def part2(inp: str) -> int:
    comp = re.compile("\d+")
    ints: dict[tuple[int, int], list[int]] = {}

    map_ = inp.split("\n")
    for ridx, row in enumerate(map_):
        for match in comp.finditer(row):
            places = [(ridx, match.start() - 1), (ridx, match.end())]
            places += [(ridx + 1, match.start() + a) for a in range(-1, len(match.group(0)) + 1)]  # below
            places += [(ridx - 1, match.start() + a) for a in range(-1, len(match.group(0)) + 1)]  # above

            for x, y in places:
                if ((len(map_[0]) - 1 > x > -1) and (-1 < y < len(map_) - 1) and    # location exists
                            (not map_[x][y].isdigit() and map_[x][y] == "*")):  # is star
                    if (x,y) not in ints:
                        ints[(x,y)] = []

                    ints[(x, y)].append(int(match.group()))

    return sum(math.prod(val) for idx, val in ints.items() if len(val) == 2)







def main():
    day = os.path.split(__file__)[1].removesuffix(".py")

    with open(f"../inputs/{day}.txt") as f:
        inp = f.read()

    part1_solution = part1(inp)

    print(f"\033[1;34mPart 1 solution:\033[39m{part1_solution}")

    part2_solution = part2(inp)
    print(f"\033[1;34mPart 2 solution:\033[39m{part2_solution}")

main()