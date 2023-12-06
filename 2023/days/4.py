import os.path
import collections

def part1(inp: str) -> int:
    points = 0

    for row in inp.splitlines():
        game: str = row.split(":")[1]
        winning, achieved = game.split("|")
        winning = {int(x.strip()) for x in filter(lambda segment: bool(segment), winning.split(" "))}
        achieved = {int(x.strip()) for x in filter(lambda segment: bool(segment), achieved.split(" "))}
        count = sum(1 for x in achieved if x in winning)
        if count == 1:
            points += 1
        elif count:
            c = 1
            for n in range(count - 1):
                c *= 2

            points += c

    return points


def part2(inp: str) -> int:
    total_cards = 0

    lst = inp.splitlines()
    d = {}

    for idx, row in enumerate(lst): # build card index
        idx += 1 # card number
        game: str = row.split(":")[1]
        winning, achieved = game.split("|")
        winning = {int(x.strip()) for x in filter(lambda segment: bool(segment), winning.split(" "))}
        won = {int(x.strip()) for x in filter(lambda segment: bool(segment), achieved.split(" "))}
        d[idx] = len(winning & won)

    cards = list(d.keys())


    for card in cards:
        #print("\n", card, cards)
        low = card + 1
        high = low + d.get(card, 0)
        r = list(range(low, high))
        #print(r)
        cards.extend(r)

    return len(cards)







def main():
    day = os.path.split(__file__)[1].removesuffix(".py")

    with open(f"../inputs/{day}.txt") as f:
        inp = f.read()

    part1_solution = part1(inp)

    print(f"\033[1;34mPart 1 solution:\033[39m{part1_solution}")

    part2_solution = part2(inp)
    print(f"\033[1;34mPart 2 solution:\033[39m{part2_solution}")

main()