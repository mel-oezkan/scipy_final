import os
import re

def check_current_index() -> int:
    """ Used for getting the current index of global runs
    made until this point. Checks the logs for the 
    highest integer number
    """

    pattern = re.compile("[0-9]+")

    current_number = 0

    # assuming this function gets called from scripts
    for dir in os.listdir("../logs/network/"):
        match = pattern.search(dir)
        if match:
            number = match.group()
            number = int(number)

            if current_number < number: current_number = number

    if current_number == 0:
        return "001"
    else:
        temp = list(str(current_number))
        s_num = ["0", "0", "0"]
        s_num[-len(temp):] = temp

        return temp 
    
