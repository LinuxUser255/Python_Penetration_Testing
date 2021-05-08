#!/usr/bin/env python3

import json
import time
import argparse
import requests
from pprint import pprint

#url = https://api.github.com/users/username

def get_proxy():
    print("Gathering proxy...""\n")
    curl = requests.get(
        'https://api.github.com/users/LinuxUser255').text
    print(f"Using proxy: {curl}")
    return {"http": curl, "https": curl}


#call the function
get_proxy()
