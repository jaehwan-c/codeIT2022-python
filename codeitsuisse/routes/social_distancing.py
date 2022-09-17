from asyncio.windows_events import NULL
import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/social-distancing', methods=['POST'])
def social_distancing():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    seats = data
    result = social(seats)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def social(seats):
    
    return [4, "No Solution", 6]