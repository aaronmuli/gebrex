import argparse
from gebrex import Gebrex


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--manifest",
                        help="Generate a mainfest file only", action="store_true")
    parser.add_argument(
        "-f", "--full", help="Generate a full manifest file with all the features included", action="store_true")
    parser.add_argument("-v", "--version",
                        help="The version of gebrex", action="store_true")
    parser.add_argument("-V", "--verbosity",
                        help="Increase output verbosity", action="store_true")
    parser.add_argument(
        "-i", "--init", help="Initialize a new project in the current directory", action="store_true")

    args = parser.parse_args()

    gebrex = Gebrex(args.manifest, args.full, args.version, args.verbosity)

    if args.init:
        gebrex.get_info()

    elif args.version:
        print(gebrex.gebrex_version)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
