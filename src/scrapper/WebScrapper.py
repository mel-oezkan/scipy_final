from typing import final
import selenium
from src.scrapper.config import Config

def get_config(attributes: list, config=Config) -> str:
    """ Takes a filter argument and returns its 
    respective query string for the url

    :args attribute: 
    """
    conf_keys = config.keys()
    query = ""

    for attr in attributes:
        if attr in conf_keys:
            query = query + config[attr]
        else:
            return ""

    return query


def initalize_url():
    pass