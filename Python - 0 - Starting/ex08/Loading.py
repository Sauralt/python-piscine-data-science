"""
Loading.py

Recodes tqdm's progress bar behavior using a generator (yield).
"""

import sys
import time


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start = time.time()
    bar_length = 20

    for i, elem in enumerate(lst):
        count = i + 1
        percent = count / total
        elapsed = time.time() - start
        rate = count / elapsed if elapsed > 0 else 0
        eta = (total - count) / rate if rate > 0 else 0

        filled = int(bar_length * percent)
        bar = '=' * filled + ' ' * (bar_length - filled)

        sys.stderr.write(
            f"\r{int(percent * 100):3d}%|{bar}| {count}/{total} "
            f"[{elapsed:.2f}<{eta:.2f}, {rate:.2f}it/s]"
        )
        sys.stderr.flush()

        yield elem

    sys.stderr.write("\n")
    sys.stderr.flush()


from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()

if __name__ == "__main__":
    main()
