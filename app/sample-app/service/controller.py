import logging
from flask import Flask, request, jsonify
from . import jsonreader
from . import settings

app = Flask("receiver")


@app.route("/health", methods=["GET"])
def health_check():
    """
    Requests sent to /health (root) are handled by this method.
    Considered as a health check endpoint for the application.
    :return: A tuple with json data and status_code
    """
    data = {"msg": "Server is healthy", "status_code": 200}
    return jsonify(data), 200


@app.route("/readsecret", methods=["GET"])
def read_secret():
    """
    Requests sent to /readsecret (root) are handled by this method.
    :return: A secret read from MY_SECRET environment variable with status code
    """
    data = None
    if settings.MY_SECRET is not None:
        logging.debug("secret, {0} is available in MY_SECRET environment variable".format(settings.MY_SECRET))
        data = {"msg": "MY_SECRET is {0}".format(settings.MY_SECRET), "status_code": 200}
        return jsonify(data), 200
    else:
        logging.error("secret is not available in MY_SECRET environment variable")
        data = {"msg": "MY_SECRET is not found in environment variables", "status_code": 404}
        return jsonify(data), 404


@app.route("/readjson", methods=["GET"])
def read_json():
    """
    Requests sent to /readjson (root) are handled by this method.
    :return: A list of all json content loaded from the settings.JSON_DIR with status code
    """
    data = jsonreader.read_json()
    if len(data) == 0:
        data = {"msg": "No json files found in {0}".format( settings.JSON_DIR), "status_code": 404}
        logging.error("no json files found in {0}".format(settings.JSON_DIR))
        return jsonify(data), 404
    else:
        logging.debug("json files found in {0}".format(settings.JSON_DIR))
        return jsonify(data), 201