import argparse
import sys 
import os

# we need to add the root folder as import point
# such that we can use our module src
sys.path.append('.')

from src.scrapper.WebScrapper import Scrapper
from src.scrapper.ConfigParser import read_config

read_config()
