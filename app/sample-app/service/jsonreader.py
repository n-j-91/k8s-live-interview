import json
import logging
import os
from . import settings


def read_json():
  data = list()
  for entry in os.scandir(settings.JSON_DIR):
    if (entry.path.endswith(".json") and entry.is_file()):
      logging.debug("{0} is a json file".format(entry))
      try:
        with open(entry.path, 'r') as inputFile:
          logging.debug("appending content from {0} to response".format(entry))
          data.append(json.load(inputFile))
      except IOError:
        logging.error("{0} cannot be opened".format(entry.path))
  return data