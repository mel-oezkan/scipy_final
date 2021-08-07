import selenium
from src.scrapper.IdMaps import Mapper
from src.scrapper.ConfigParser import create_conf, read_conf
from sys import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import csv
import sys

class Scrapper:

    def __init__(self, ds_name=None):
        self.initalize_drivers()
        self._handle_ds()
        self.base_url = "https://www.vinted.de/vetements?"

    # using a static method since this function is not bound to 
    # any class variables and makes it easier to call recursively 
    @staticmethod
    def config_parser(attributes: list, config=Mapper) -> str:
        """ Takes a filter argument and returns its 
        respective query string for the url

        :args attribute: 
        :args config: the current configurations based on the mappings
        """
        conf_keys = config.keys()
        query = ""

        for attr in attributes:
            if attr in conf_keys:
                query = query + config[attr]
            else:
                return ""

        return query

    def initalize_drivers(self):
        # determine the operating system
        user_os = platform
        curr_path = os.getcwd()
        print(curr_path)

        if user_os == "linux":
            path = curr_path + "/drivers/chromedriver_linux64/chromedriver"
        
        elif user_os == "win32":
            path = curr_path + "/drivers/chromedriver_win32/chromedriver"

        # alis for mac_os
        elif user_os == "darwin":
            path = curr_path + "/drivers/chromedriver_mac64/chromedriver"

        else:
            raise ValueError(
                """ Sady there is a problem with your 
                operating system. Try running this porgram 
                on docker or a vm""")

        self.driver = webdriver.Chrome(path)

    def _handle_ds(self, name=None):
        """ Checks if name was set. If not append to global ds """ 
        
        if name:
            self.ds_path = f"data/{name}.csv"
        else:
            self.ds_path = "data/full_data.csv"

    def scrap_current(self, curr_url):
        """ Takes a url and searches for all articles which are
        scrapped afterwards
        """
        
        self.driver.get(curr_url)

        posts = self.driver.find_elements_by_class_name("feed-grid__item")

        if not(posts):
            sys.exit(0)
        
        for index, post in enumerate(posts):
            
            price = post.find_elements_by_tag_name("h3")
            
            # 0:auth, 1:likes, 2:size, 3:brand
            infos = post.find_elements_by_tag_name("h4")

            # Best matches contains span text indicating a skip section 
            is_skip = post.find_elements_by_tag_name("span")
            
            links = post.find_elements_by_tag_name("a")

            auth_source = links[0].get_attribute("href")
            art_source = links[1].get_attribute("href")

            # Handling Banners which are not articles
            if "Best Matches" in [i.text for i in is_skip]:
                continue

            print([info.text for info in infos])
            print(len(price))

            row = []
            row.append(infos[0].text)
            row.append(infos[1].text)
            row.append(infos[2].text)
            row.append(infos[3].text)
            row.append(price[0].text)
            row.append(art_source)
            row.append(auth_source)

            with open(self.ds_path, 'a') as f:
                # create the csv writer
                writer = csv.writer(f)

                # write a row to the csv file
                writer.writerow(row)
    
    def run(self, config_path, num_pages=1):
        # Handles the configuration
        config = read_conf(config_path)
        conf_url = create_conf(config) 


        # create the url
        select_page = lambda x: (None + "&page={x}")

        # loop over pages


        return None

    def test_run(self, pages=1, page_range=None):
        

        test_url = "https://www.vinted.de/vetements?color_id[]=1&color_id[]=12&catalog[]=76"

        if not(page_range):
            page_from = 1
            page_to = pages         
        else:
            if len(page_range) > 2: 
                raise ValueError("Page range exceeds two values")

            page_from = page_range[0]
            page_to = page_range[1]

        select_page = lambda x: (test_url + "&page={x}")
        for page in range(page_from, page_to):

            # add the page number
            self.scrap_current(select_page(page))


    def test(self):
        print("hallo")


