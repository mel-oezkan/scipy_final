import os
import sys
import argparse

# we need to add the root folder as import point
# such that we can use our module src
sys.path.append('.')

parser = argparse.ArgumentParser(description="")

# Run the flask web app

os.system("python ../src/annotator/main.py")