import datetime
import shutil
import sys

import requests

with open("token") as f:
    token = f.read()

YEAR = "2023"
DAY = (sys.argv[1] if len(sys.argv) > 1 else input("Day: ")) or datetime.datetime.utcnow().day

inp = requests.get(f"https://adventofcode.com/{YEAR}/day/{DAY}/input", cookies={"session": token})
inp.raise_for_status()

with open(f"inputs/{DAY}.txt", mode="w") as f:
    f.write(inp.text.strip())

shutil.copy("template.py", f"days/{DAY}.py")
