import os.path
import re

def part1(inp: str) -> int:
    finals = []

    for val in inp.split("\n"):
        nums = re.findall("\d", val)
        finals.append(int(nums[0] + nums[-1]))

    return sum(finals)


mapped = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
reg = re.compile("\d|" + "|".join(mapped))

def part2(inp: str) -> int:
    finals = []

    for val in inp.split("\n"):
        nums = []
        offset = 0
        while offset < len(val):
            t = reg.search(val[offset:])
            if t is None:
                break

            nums.append(mapped.get(t.group(0), t.group(0)))
            offset += max(t.pos, 1)

        finals.append(int(nums[0] + nums[-1]))

    return sum(finals)







def main():
    day = os.path.split(__file__)[1].removesuffix(".py")

    with open(f"../inputs/{day}.txt") as f:
        inp = f.read()

    part1_solution = part1(inp)

    print(f"\033[1;34mPart 1 solution:\033[39m {part1_solution}")

    part2_solution = part2(inp)
    print(f"\033[1;34mPart 2 solution:\033[39m {part2_solution}")

main()