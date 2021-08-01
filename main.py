import os
import argparse


if __name__ == "__main__":

    # Initalize parset
    parser = argparse.ArgumentParser(description="")

    parser.add_argument(
        "--mode", type=str, default=None,
        help="target url for the web scrapper")

    parser.add_argument(
        "--url", type=str, default=None,
        help="target url for the web scrapper")

    parser.add_argument(
        "--max_pages", type=int, default=1000,
        help="target url for the web scrapper")


    args = parser.parse_args()

    if args.mode == None: raise ValueError(
        "A mode has to be defined use the parse argument mode.\npython --mode 'train'")

    elif args.mode == "train":
        print("Running the training Module")

    elif args.mode == "scrap":
        print("Running the training Module")

    elif args.mode == "annotate":
        print("Running the training Module")
    