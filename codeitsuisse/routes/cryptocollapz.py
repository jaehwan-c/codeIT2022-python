import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/cryptocollapz', methods=['POST'])
def cryptocollapz():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    data = list(data)
    result = crypto_func(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def crypto_func(data):
    lst_to_return = list()
    for i in range(len(data)):
        temp_lst = list()
        for j in range(len(data[i])):
            temp_lst.append(max_value_checker(data[i][j]))
        lst_to_return.append(temp_lst)
    
    return lst_to_return

def max_value_checker(i):
    num = i
    lst = []
    
    if i == 1 or i == 2:
        return 4
    
    else:
        while num not in lst:

            if num % 2 == 0:
                lst.append(num)
                num = num // 2
            else:
                lst.append(num)
                num = 3 * num + 1
        else:
            return max(lst)
