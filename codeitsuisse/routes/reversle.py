import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/reversle', methods=['POST'])
def reversle():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    length = data["equationLength"]
    attemps = data["attemptsAllowed"]
    result = brackets(length, attemps)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def brackets(length, attemps):
    

    dict_to_return = {"equation": ["9","3","/","4","^","=","8","1"], "info":[length,attemps]}
    return dict_to_return