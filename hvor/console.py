#!/usr/bin/env python
import sys
import json
from .hvor import point


def _exit_with_usage(msg=None):
    if not msg:
        print("Usage: hvor p1 p2")
        sys.exit()
    else:
        # exit code = 1 when sys.exit receives message
        sys.exit(msg)


def _print_point_to_json(p1: float, p2: float) -> None:
    """This function is called when hvor is called from the console.
    It prints the point dict to std.out.
    """
    pt = point(p1, p2)
    print(json.dumps(pt, indent=4))


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        _exit_with_usage()
    if len(sys.argv) != 3:
        exit("Usage: hvor p1 p2")
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    try:
        f1, f2 = float(s1), float(s2)
    except ValueError as err:
        msg = f"hvor takes two floating point numbers: {err}"
        _exit_with_usage(msg)
    _print_point_to_json(f1, f2)


if __name__ == "__main__":
    main()
