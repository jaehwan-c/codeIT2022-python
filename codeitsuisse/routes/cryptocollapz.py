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
    dict_to_return = dict()
    
    dict_to_return[1] = 4
    dict_to_return[2] = 4
    for i in range(len(data)):
        for j in range(len(data[i])):
            temp_lst = list()
            k = data[i][j]
            
            while k > 2:
                
                temp_lst.append(k)
                
                if k%2 == 0:
                    k //= 2
                else:
                    k = k*3 + 1
            else:
                for k in temp_lst:
                    if k in dict_to_return:
                        if max(temp_lst) > dict_to_return[k]:
                            dict_to_return[data[i][j]] = max(temp_lst)
                        else:                        
                            dict_to_return[data[i][j]] = dict_to_return[k]
                            break
                    elif k == max(temp_lst):
                        dict_to_return[k] = max(temp_lst)
                        break
                    else:
                        dict_to_return[k] = max(temp_lst)
           
    for i in range(len(data)):
        lst_to_return.append(dict_to_return[data[i]] for i in range(len(data)))
    return lst_to_return
