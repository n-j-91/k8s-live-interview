import json
import logging
import os
from . import settings


def read_json():
  data = list()
  for filename in os.listdir(settings.JSON_DIR):
    if filename.endswith(".json"):
      logging.debug("{0} is a json file".format(filename))
      try:
        with open(os.path.join(settings.JSON_DIR, filename), 'r') as inputFile:
          logging.debug("appending content from {0} to response".format(filename))
          data.append(json.load(inputFile))
      except IOError:
        logging.error("{0} cannot be opened".format(filename))
  return data