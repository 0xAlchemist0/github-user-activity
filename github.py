import datetime
import json

import requests
from colorama import Fore, Style
from colorama import init as colorama_init
from requester import make_request


def get_user_events(user_name):
    response = make_request(f"/users/{user_name}/events")
    # last_five = get_top_five(response)
    
    if (response):
         for values in response:
          date = format_date(values["created_at"])
          print(f"{Fore.GREEN}{date.month}/{date.day}/{date.year}: {values['repo']['name']}")
    
    else:
      print(f"{Fore.RED}Noe events found or user does not exist!")
    #nice way to formaty the date
  
    # dissect_values([], response)
    
    return None


def get_top_five(list):
    return list[0:5]

def dissect_values(key_targets, list):
    
    
    return None

def format_date(creation):
      date = datetime.datetime.strptime(creation, "%Y-%m-%dT%H:%M:%SZ")
      return date

