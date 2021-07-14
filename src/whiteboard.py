""" This 'whiteboard' file is for experimentation and concept validation only; it can change at any time."""

import os
import sys
import pprint


def dumpenv():
    return pprint.pformat(
        ['{} = "{}"'.format(k, v) for k, v in list(os.environ.items())], width=99
    )


def main():
    v = ["p", "y", "t", "h", "o", "n"]
    pprint.pprint(v[:])
    # env_list = dumpenv()
    # print(env_list)


if __name__ == "__main__":
    sys.exit(main())
