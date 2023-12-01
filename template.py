import os.path


def part1(inp: str) -> str:
    pass

def part2(inp: str) -> str:
    pass







def main():
    day = os.path.split(__file__)[1].removesuffix(".py")

    with open(f"../inputs/{day}.txt") as f:
        inp = f.read()

    part1_solution = part1(inp)

    print(f"\033[1;34mPart 1 solution:\033[39m{part1_solution}")

    part2_solution = part2(inp)
    print(f"\033[1;34mPart 2 solution:\033[39m{part2_solution}")

main()