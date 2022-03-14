#!/usr/bin/env python3

import os
import requests

# get list of text files
dir = os.path.expanduser('~/supplier-data/descriptions/')
list_desc = os.listdir(dir)

endpoint = 'http://34.67.217.166/fruits/'

def convert_to_list(file):
  """Converts an opened file object into list of lines."""
  list_content = [line.rstrip('\n') for line in list(file)]
  return list_content

def convert_to_dict(description, name):
  """Parses list of lines into description dictionary."""
  dict = {}

  dict['name'] = description[0]

  # convert from string "xxx lbs" to integer xxx
  dict['weight'] = int(description[1].split()[0])

  dict['description'] = description[2]

  # add the corresponding image
  dict['image_name'] = os.path.splitext(name)[0] + '.jpeg'
  return dict


for name in list_desc:
  with open(dir+name) as file:
    description = convert_to_list(file)
    dict_desc = convert_to_dict(description, name)

    response = requests.post(endpoint, data=dict_desc)
    print("POST review {}. Status code {}.".format(dir+name, response.status_code))
