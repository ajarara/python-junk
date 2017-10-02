import argparse
from pprint import pprint

# not very impressive, just poking the argparse lib.

def main():
    parser = argparse.ArgumentParser("Some top level description")

    parser.add_argument('api_key', metavar='s0meAP1key', type=str, nargs='?')
    args = parser.parse_args()

    pprint(args)

if __name__ == '__main__':
    main()
