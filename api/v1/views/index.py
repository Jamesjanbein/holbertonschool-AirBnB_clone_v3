#!/usr/bin/python
"""
index
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", methods=['GET'])
def status():
    """
    status route
    :return: response with json
    """
    data = {
        "status": "OK"
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp
