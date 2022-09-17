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
        test_lst = list()
        for j in range(len(data[i])):
            
            if data[i][j] in dict_to_return:
                print(data[i][j])
                test_lst.append(dict_to_return[data[i][j]])
                continue
            
            else:
                temp_lst = list()
                k = data[i][j]
            
                while k > 2:
                
                    if k%2 == 0:
                        
                        temp_lst.append(k)
                        k //= 2
                        if k in dict_to_return:
                            if max(temp_lst) > dict_to_return[k]:
                                dict_to_return[data[i][j]] = max(temp_lst)
                                test_lst.append(max(temp_lst))
                                break
                            else:                        
                                dict_to_return[data[i][j]] = dict_to_return[k]
                                test_lst.append(dict_to_return[k])
                                break
                    else:
                        
                        temp_lst.append(k)
                        k = k*3 + 1
                else:
                    for k in temp_lst:
                        if k in dict_to_return:
                            if max(temp_lst) > dict_to_return[k]:
                                dict_to_return[data[i][j]] = max(temp_lst)
                                test_lst.append(max(temp_lst))
                                break
                            else:                        
                                dict_to_return[data[i][j]] = dict_to_return[k]
                                test_lst.append(max(temp_lst))
                                break
                        elif k == max(temp_lst):
                            dict_to_return[k] = max(temp_lst)
                            break
                        else:
                            dict_to_return[k] = max(temp_lst)
                            
                    test_lst.append(dict_to_return[data[i][j]])
            print(temp_lst)
        lst_to_return.append(test_lst)


    return lst_to_return
