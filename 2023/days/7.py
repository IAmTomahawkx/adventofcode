import os.path
from collections import Counter

def get_typ(cards: str, s = None) -> int:
    if s is None:
        s = Counter(cards)

    matches = [x[1] for x in s.most_common()]
    if matches[0] == 5:
        return 7
    elif matches[0] == 4:
        return 6
    elif matches[0] == 3 and matches[1] == 2:
        return 5
    elif matches[0] == 3 and matches[1] == 1:
        return 4
    elif matches[0] == 2 and matches[1] == 2:
        return 3
    elif matches[0] == 2 and matches[1] == 1:
        return 2
    elif matches[0] == 1:
        return 1

    raise RuntimeError(s, matches)


def part1(inp: str) -> int:
    lines = inp.splitlines()

    finals = []

    for line in lines:
        cards: str
        cards, bet = line.split()
        bet: int = int(bet)
        typ = get_typ(cards)
        finals.append((typ, cards, bet))

    card_idx = {a: idx + 1 for idx, a in enumerate("23456789TJQKA")}

    finals = sorted(finals, key=lambda value: (value[0], [card_idx[v] for v in value[1]]))
    return sum((idx + 1) * x for idx, (_, __, x) in enumerate(finals))


def part2(inp: str) -> int:
    lines = inp.splitlines()

    finals = []

    for line in lines:
        cards: str
        cards, bet = line.split()
        bet: int = int(bet)

        ideal = cards.replace("J", "")
        if not ideal:
            ideal = "AAAAA"

        s = Counter(ideal)
        com = s.most_common(1)[0]
        s[com[0]] += cards.count("J") if cards.count("J") < 5 else 0

        typ = get_typ(cards, s=s)
        finals.append((typ, cards, bet))

    card_idx = {a: idx + 1 for idx, a in enumerate("J23456789TQKA")}

    finals = sorted(finals, key=lambda value: (value[0], [card_idx[v] for v in value[1]]))
    return sum((idx + 1) * x for idx, (_, __, x) in enumerate(finals))







def main():
    day = os.path.split(__file__)[1].removesuffix(".py")

    with open(f"../inputs/{day}.txt") as f:
        inp = f.read()

    part1_solution = part1(inp)

    print(f"\033[1;34mPart 1 solution:\033[39m{part1_solution}")

    part2_solution = part2(inp)
    print(f"\033[1;34mPart 2 solution:\033[39m{part2_solution}")

main()