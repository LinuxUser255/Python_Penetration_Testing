#!/usr/bin/env python3

import json
import time
import argparse
import requests
from pprint import pprint



def get_proxy():
    print("Gathering proxy...""\n")
    curl = requests.get(
        'https://api.to_call.com').text
    print(f"Using proxy: {curl}")
    return {"http": curl, "https": curl}


#call the function
get_proxy()
