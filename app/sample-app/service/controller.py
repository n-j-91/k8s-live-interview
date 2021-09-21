import logging
from flask import Flask, request, jsonify
from . import jsonreader
from . import settings

app = Flask("receiver")


@app.route("/_status/healthz", methods=["GET"])
def health_check():
    """
    Requests sent to / (root) are handled by this method.
    Considered as a health check endpoint for the application.
    :return: A tuple with json data and status_code
    """
    data = {"msg": "Server is healthy", "status_code": 200}
    return jsonify(data), 200

@app.route("/v1/readjson", methods=["GET"])
def read_json():
    """
    Requests sent to / (root) are handled by this method.
    Considered as a health check endpoint for the application.
    :return: A tuple with json data and status_code
    """
    data = jsonreader.read_json()
    if len(data) == 0:
        data = {"msg": "No json files found in {0}".format( settings.JSON_DIR), "status_code": 404}
        logging.error("no json files found in {0}".format(settings.JSON_DIR))
        return jsonify(data), 404
    else:
        logging.debug("json files found in {0}".format(settings.JSON_DIR))
        return jsonify(data), 201