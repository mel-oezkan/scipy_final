import os
import argparse

from src.scrapper.WebScrapper import Scrapper

if __name__ == "__main__":

    # Initalize parset
    parser = argparse.ArgumentParser(description="")

    parser.add_argument(
        "--mode", type=str, required=True,
        help="arg for the respective mode")

    parser.add_argument(
        "--config", type=str, default=None,
        help="path to the config yaml")

    parser.add_argument(
        "--max_pages", type=int, default=None,
        help="arg for the range of pages to be scrapped")

    parser.add_argument(
        "--ds_name", type=str, default=None, 
        help="define the name of the either existing ds or new ds. Leaving this empty will append data to full_data.csv")

    args = parser.parse_args()

    if args.mode == "train":
        pass

    elif args.mode == "scrap":
        print("Running the training Module")

        assert args.max_pages, "you have to define a range of pages you want to look for"
        assert args.config, "you have to define the path to the search config"
        
        scrapper = Scrapper(ds_name=args.ds_name)
        scrapper.run(args.config, args.max_pages)


    elif args.mode == "annotate":
        print("Running the training Module")
    