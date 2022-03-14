#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"

# get paths of images
dir = os.path.expanduser('~/supplier-data/images/')
list_image = os.listdir(dir)
list_image = [name for name in list_image if name.endswith('.jpeg')]

# upload images
for name in list_image:
  with open(dir+name, 'rb') as image:
    print("Successfully opened {}".format(dir+name))
    response = requests.post(url, files={'file': image})
    print("POST {} with status code {}.".format(dir+name, response.status_code))
