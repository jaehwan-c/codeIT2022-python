import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/cryptocollapz', methods=['POST'])
def cryptocollapz():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = crypto_func(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def crypto_func(data):
    lst_to_return = list()
    for i in range(data):
        temp_lst = list()
        for j in range(len(data[i])):
            temp_lst.append(max_value_checker(data[i][j]))
        temp_lst.append(lst_to_return)
    
    return lst_to_return

def max_value_checker(i):
    while i % 2 == 0:
        i = i // 2
    else:
        return i * 3 + 1