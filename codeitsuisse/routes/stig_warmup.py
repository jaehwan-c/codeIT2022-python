import logging
import json
import math

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stig/warmup', methods=['POST'])
def stig_warmup():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    questions = data[0]["questions"]
    maxRating = data[0]['maxRating']
    result = warmup_stig(questions, maxRating)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def warmup_stig(questions, maxRating):
    
    lower_int = questions[0]['lower']
    upper_int = questions[0]['upper']
    lst_to_return = list()
    
    gap = upper_int - lower_int + 1
    p = gap // math.gcd(gap, maxRating)
    q = maxRating // math.gcd(gap, maxRating)
    
    dict_to_return = dict()
    
    dict_to_return['p'] = p
    dict_to_return['q'] = q
    
    lst_to_return.append(dict_to_return)
    
    return dict_to_return
