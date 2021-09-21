import logging
from flask import Flask, request, jsonify
from . import jsonreader
from . import settings

app = Flask("receiver")


@app.route("/health", methods=["GET"])
def health_check():
    """
    Requests sent to / (root) are handled by this method.
    Considered as a health check endpoint for the application.
    :return: A tuple with json data and status_code
    """
    data = {"msg": "Server is healthy", "status_code": 200}
    return jsonify(data), 200

@app.route("/readjson", methods=["GET"])
def read_json():
    """
    Requests sent to / (root) are handled by this method.
    Considered as a health check endpoint for the application.
    :return: A tuple with json data and status_code
    """
    data = jsonreader.read_json()
    if data is None:
        data = {"msg": "No {0} file is found in {1}".format(settings.FILE_NAME, settings.JSON_DIR), "status_code": 404}
        return jsonify(data), 404
    else:
        return jsonify(data), 201