import os.path
import multiprocessing # you know its good when


def part1(inp: str) -> str:
    chunked = inp.split("\n\n")
    seeds, *raw_maps = chunked

    seeds = [int(x) for x in seeds.removeprefix("seeds: ").split()]

    maps: dict[str, dict] = {}

    for m in raw_maps:
        m: list[str] = m.splitlines()
        name = m.pop(0).removesuffix(" map:")
        maps[name] = current = {}
        for line in m:
            dest, src, rng = line.split()
            current[(int(src), int(src) + int(rng))] = int(dest)

    seed_terms = []

    for seed in seeds:
        value = seed
        for name, map_ in maps.items():
            for rng, val in map_.items():
                if rng[0] < value < rng[1]:
                    value = val + (value - rng[0])
                    #print(name, value)
                    break

        seed_terms.append(value)


    return min(seed_terms)


def solve_part2_mp(maps: dict[str, dict], seed):
    resp = 999999999999999999999999  # lol

    print(f"run seed {seed[0]}-{seed[0] + seed[1] - 1} with range {seed[1] - 1}")
    for seed in range(seed[0], seed[0] + seed[1]):
        value = seed
        for name, map_ in maps.items():
            for rng, val in map_.items():
                if rng[0] <= value <= rng[1]:
                    value = val + (value - rng[0])
                    break

        if value < resp:
            resp = value

    print(f"return seed {seed[0]} with value {resp}")
    return resp

def part2(inp: str) -> str:
    # fwiw i never solved this
    chunked = inp.split("\n\n")
    _seeds, *raw_maps = chunked

    _seeds = [int(x) for x in _seeds.removeprefix("seeds: ").split()]

    seeds = list(zip(_seeds[::2], _seeds[1::2]))

    maps: dict[str, dict] = {}

    for m in raw_maps:
        m: list[str] = m.splitlines()
        name = m.pop(0).removesuffix(" map:")
        maps[name] = current = {}
        for line in m:
            dest, src, rng = line.split()
            current[(int(src), int(src) + int(rng) - 1)] = int(dest)


    # i tried to do fancy range things but ended up just brute forcing it
    #seed, seed_offset = seeds[0]
    #map_ = maps["seed-to-soil"]
    #start, end, d_start, d_end = next(iter(map_))
    #if start < seed and seed + seed_offset < end:


    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    resp = None

    def cb(value):
        nonlocal resp
        if resp is None:
            resp = value
        else:
            if value < resp:
                resp = value

    for seed in seeds:
        pool.apply_async(solve_part2_mp, args=(maps, seed), )

    return resp






def main():
    day = os.path.split(__file__)[1].removesuffix(".py")

    with open(f"../inputs/{day}.txt") as f:
        inp = f.read()

    part1_solution = part1(inp)

    print(f"\033[1;34mPart 1 solution:\033[39m{part1_solution}")

    part2_solution = part2(inp)
    print(f"\033[1;34mPart 2 solution:\033[39m{part2_solution}")

main()