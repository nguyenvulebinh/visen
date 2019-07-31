import sys
from visen import format


def main():  # type: () -> None
    """Read the Real Python article feed"""
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]

    # An article ID is given, show article
    if args and opts and len(args) == 1 and len(opts) == 1 and '-h' not in opts:
        if opts[0] == '-c':
            print(format.clean_tone(args[0]))
        elif opts[0] == '-r':
            print(format.remove_tone(args[0]))
    else:
        print(
            """
Usage:
------
$ python -m visen [options] sentence

Available options are:
    -h, Show this help
    -r, Remove sentence tone
    -c, Clean sentence tone
Contact:
--------
More information is available at:
- https://github.com/nguyenvulebinh/visen
"""
        )


if __name__ == "__main__":
    main()
