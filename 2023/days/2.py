import os.path
import re


def part1(inp: str) -> int:
    r = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    mx = re.compile("(\d+) (red|green|blue)")

    possible_ids: list[int] = []

    for idx, game in enumerate(inp.split("\n")):
        game = game.removeprefix(f"Game {idx+1}: ")
        draws = game.split(";")
        ok = True

        for draw in draws:
            for match in mx.finditer(draw):
                amount, colour = match.groups()
                if int(amount) > r[colour]:
                    ok = False

        if ok:
            possible_ids.append(idx+1)

    return sum(possible_ids)


def part2(inp: str) -> int:
    mx = re.compile("(\d+) (red|green|blue)")

    mins: list[int] = []

    for idx, game in enumerate(inp.split("\n")):
        game = game.removeprefix(f"Game {idx + 1}: ")
        draws = game.split(";")
        r = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for draw in draws:
            for match in mx.finditer(draw):
                amount, colour = match.groups()
                r[colour] = max(r[colour], int(amount))

        ms = r["red"] * r["green"] * r["blue"]
        mins.append(ms)

    return sum(mins)







def main():
    day = os.path.split(__file__)[1].removesuffix(".py")

    with open(f"../inputs/{day}.txt") as f:
        inp = f.read()

    part1_solution = part1(inp)

    print(f"\033[1;34mPart 1 solution:\033[39m{part1_solution}")

    part2_solution = part2(inp)
    print(f"\033[1;34mPart 2 solution:\033[39m{part2_solution}")

main()