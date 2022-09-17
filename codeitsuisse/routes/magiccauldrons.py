import logging
import json
import numpy
from datetime import date
from datetime import datetime

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/magiccauldrons', methods=['POST'])
def magiccauldrons():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    data_cell = data
    result = cell(data_cell)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def cell(data_cell):
    x = data_cell
    return x
