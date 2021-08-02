import selenium
from src.scrapper.IdMaps import Mapper
from sys import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

class Scrapper:

    def __init__(self):
        self.initalize_drivers()

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

        if user_os == "linux":
            path = os.path.join(curr_path, "drivers/chromedriver_linux64")
        
        elif user_os == "win32":
            path = os.path.join(curr_path, "drivers/chromedriver_win32")

        # alis for mac_os
        elif user_os == "darwin":
            path = os.path.join(curr_path, "drivers/chromedriver_mac64")

        else:
            raise ValueError(
                """ Sady there is a problem with your 
                operating system. Try running this porgram 
                on docker or a vm""")

        self.driver = webdriver.Chrome(path)




