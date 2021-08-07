"""

$ python scan_repos.py path/to/repos.txt

Pull a bunch of repos and print the commit hash on each branch.

The file `repos.txt` has one git ssh url per line.

Prints to stdout.

"""

from util import analyze_repo
import os
import sys
from datetime import datetime

repos = []

file = os.path.abspath(sys.argv[1])

print(f'Report on {datetime.utcnow().isoformat()}\n')


with open(file) as f:
    repos = f.read().split('\n')

for r in repos:
    analyze_repo(r, r)