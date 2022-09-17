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
    
    def coin(i,max_value):
        temp = 0
        if i%2 == 0:
            if ((i&(i-1))==0) and (i>2):
                if i > max_value:
                    max_value = i
                return max_value
            else:
                if i > max_value:
                    max_value = i
                return coin(i//2,max_value)
        elif i%2 == 1:
            if i > max_value:
                max_value = i
            return coin((i*3)+1,max_value)
    
    solution = []   
    for i in data:
        temp = []
        for j in i:
            temp.append(coin(j,0))
        solution.append(temp)
        
    return solution
