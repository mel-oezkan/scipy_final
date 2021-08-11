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
        "--name", type=str, default=None,
        help="name of user to scrap listings from")

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
        scrapper = Scrapper(ds_name=args.ds_name)

        if args.name:
            scrapper.user_entries(args.name)

        elif (args.max_pages and args.config):
            scrapper.run(args.config, args.max_pages)

        else:
            raise ValueError("You either have to define a \
                name for the user searcher or define a path to \
                a config file and a max_page range")
        
        scrapper.driver.quit()
        print("finished scrapping")
        
    
    elif args.mode == "annotate":
        print("Running the training Module")
    