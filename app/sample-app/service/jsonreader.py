import json
import logging
import os
from . import settings


def read_json():
  data = None
  try:
    with open("{0}/{1}".format(settings.JSON_DIR, settings.FILE_NAME), 'r') as inputFile:
      data = json.load(inputFile)
  except IOError:
    logging.error("{0}/{1} is not accessoble".format(settings.JSON_DIR, settings.FILE_NAME))
  return data