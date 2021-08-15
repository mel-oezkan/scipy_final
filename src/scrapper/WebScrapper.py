import selenium
from src.scrapper.IdMaps import Mapper
from src.scrapper.ConfigParser import Config
from sys import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import re
import csv
import sys
import time

import imageio as io
import urllib.request

class Scrapper:

    def __init__(self, ds_name=None, silent=True):
        """
        :params ds_name: name of the dataset. If left empty
            it will write on full_data.csv
        :params silent: decides if the chrome browser will be shown
        """

        self.initalize_drivers(silent)
        self._handle_ds(ds_name)
        self.base_url = "https://www.vinted.de/vetements?"

    def initalize_drivers(self, silent):
        """ Initalizes the 'browser'. This will require a
        functioning chromdriver and chrome installed.
        If the chromdriver does not match the chrome browser
        the user will be prompted to download a matching one
        """

        # determine the operating system
        user_os = platform
        curr_path = os.getcwd()

        if user_os == "linux":
            path = curr_path + "/drivers/chromedriver_linux64/chromedriver"

        elif user_os == "win32":
            path = curr_path + "/drivers/chromedriver_win32/chromedriver"

        # alis for mac_os
        elif user_os == "darwin":
            path = curr_path + "/drivers/chromedriver_mac64/chromedriver"

        else:
            raise ValueError(
                "It seems as if the current chromdriver does not \
                work on your device. Try downloading a suitable chromdriver at \
                https://chromedriver.chromium.org/ and repace it in the \
                folder of your respective os. After that tyr running \
                this script again")

        options = webdriver.ChromeOptions()
        if silent:

            options.add_argument("headless")
            options.add_argument('disable-blink-features=AutomationControlled')
            options.add_argument('user-agent=fake_user')


        self.driver = webdriver.Chrome(path, chrome_options=options)

    def _handle_ds(self, name=None):
        """ Checks if name was set. If not append to global ds """

        if name:
            self.ds_path = f"data/{name}.csv"
        else:
            self.ds_path = "data/full_data.csv"

    def scrap_current(self, curr_url, curr_conf) -> None:
        """ Takes the modified url (by config) and searches the page for listings.
        Given the listings it scraps the information from them and appends them
        to the respective dataset (csv file)

        :params curr_ulr: url on which the config tokens are already applied
            (or possibly any url with similar page structure and class naming)
        :params curr_conf: only used to get search parametes for better handling
            of the datasets
        """

        self.driver.get(curr_url)

        self.driver.maximize_window()
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


            row = []
            row.append(curr_conf["gender"])
            row.append(curr_conf["category"])
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
        """ Runs the scrapper given a search parameter config"""

        # Handles the configuration
        config = Config()
        conf_url, _ = config.create_conf(config_path)

        # create the url
        select_page = lambda x: (conf_url + f"&page={x}")

        # loop over pages
        for curr_conf, page in zip(config.config, range(1, num_pages+1)):
            self.scrap_current(select_page(page), curr_conf)
            # print(select_page(page))

    def article_images(self, art_url, sample=False, savepath=None):
        """ Visits the listings url and either all images as numpy array
        or only the main image

        :params art_url: url of the listing
        :params sample: parameter to decide wether to return all images
            of the listing or only one sample. (True -> only main image)
        :params savepath: path where to save the scrapped image
        """

        self.driver.get(art_url)
        self.driver.implicitly_wait(5)
        image_container = self.driver.find_element_by_class_name("item-photos")


        if not(image_container):
            # returns None which will be a signal
            # for the main code to act acordingly
            return None

        images = image_container.find_elements_by_tag_name("a")

        as_list = []

        for img in images:
            img_url = img.get_attribute("href")

            if savepath:
                file_path = os.path.join(savepath, f"{time.time():.0f}.jpg")
                urllib.request.urlretrieve(img_url, file_path)

            else:
                temp_img = io.imread(img_url)
                if sample:
                    return [temp_img]
                as_list.append(temp_img)

        return as_list

    def search_user(self, name) -> str:
        """ Function to seach for an username. Will stop after searching
        for it on the fist result page. Name should be matches with the fist entry

        returns: the url of the user
        """

        search_url = "https://www.vinted.de/member/general/search?search_text="
        search_url = search_url + name

        # get  the page
        self.driver.get(search_url)

        # check for empty results by looking for div elements
        # with class: empty-state
        is_content = self.driver.find_elements_by_class_name("empty-state")
        if is_content:
            raise ValueError(f"the given name {name} does not yield any results")

        # iterate over elements with the class of follow
        # to get all users (serches for exact match)
        pattern = re.compile(name)

        users = self.driver.find_elements_by_class_name("follow")

        for user in users:
            temp = user.find_element_by_class_name("follow__name")
            if pattern.fullmatch(temp.text):
                link = temp.get_attribute("href")
                return link

    def user_entries(self, name:str):
        """ Given an username this method will first search for the user
        url. After visiting the user page it will first scroll to the bottom of
        the page to load all listings and than scrap every listing while also
        looking at the listing url to get information about gender and category.

        :params name: name of the user
        """

        print("Searching for user")
        url = self.search_user(name)

        self.driver.get(url)


        # since some pages have many entries the scrapper would have
        # to scroll down the page to reveal all elements thus the
        # scrapper has to simulate this by itself

        # get the scroll height
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight")
        latest_stop = 0

        print("start scrolling")
        while True:


            # There is some js (mabe react) code which detect is the visitor
            # jumps to the end of the page thus we have to eas into the
            # scrolling part and wait create a smooth scrolling part

            # Scroll down to bottom
            self.driver.execute_script(
                    f"window.scrollTo({latest_stop}, document.body.scrollHeight-300);")

            for step in range(last_height-300, last_height, 5):
                self.driver.execute_script(
                    f"window.scrollTo({step-5}, {step});")
                time.sleep(.002)

            # Wait to load page
            time.sleep(0.5)
            latest_stop = last_height

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

        print("finished scrolling")

        # now all elemenst should be loaded in
        # scrapping can start

        # listings can be found by sarching for elements with
        # class containing the name: feed-grid__item-content
        elements = self.driver.find_elements_by_class_name("feed-grid__item-content")

        for element in elements:
            link = element.find_elements_by_tag_name("a")
            price = element.find_elements_by_tag_name("h3")
            price = price[0].text

            listing = link[0].get_attribute("href")

            information = element.find_elements_by_tag_name("h4")
            text_info = [x.text for x in information]
            # somtimes there can be an entry without a size
            # thus we have to check for empty entries in infos
            if "" in text_info:
                # when this happens the size will not be displayed
                # since a brand is always defined
                likes = text_info[0]
                size = None
                brand = text_info[1]

            else:
                likes = text_info[0]
                size = text_info[2]
                brand = text_info[1]

            # since the page scrapper contains gender and category
            # we have to artificaialy get thos values
            # However, these values are contained in the listing url
            # url = vinde.de/gender/clothing_type/category/sub_category1/.../sub_category_n/listing.id
            url_args = listing.split("/")

            # get the gender set for the listing
            if "damen" in url_args:
                gender = "female"

            elif "herren" in url_args:
                gender = "male"
            else:
                # Since we only consider male and female clothing
                # we will skip other items and clothing for children
                continue

            # we will only save the listings contained in the predefined
            # mappings used in filtered web scrapper
            possible_categories = list(Mapper[gender]["category"].keys())

            # pre initalization to test if the category is in our
            # predefined mappings
            category = None

            # using the reversed list to capute the most specific library
            for url_arg in url_args[::-1]:
                # print(url_arg)
                if url_arg in possible_categories:
                    category = url_arg
                    break

            if not(category):
                # print the uls of listings that didn't make it
                # print(url_args)
                continue

            row = [gender, category, name, likes, size, brand, price, listing]

            with open(self.ds_path, 'a') as f:

                # create the csv writer
                writer = csv.writer(f)

                # write a row to the csv file
                writer.writerow(row)
