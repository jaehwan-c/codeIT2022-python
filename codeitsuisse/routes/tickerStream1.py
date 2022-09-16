import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tickerStreamPart1', methods=['POST'])
def tickerStream1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    stream = data["stream"]
    result = to_cumulative(stream)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def to_cumulative(stream: list):
    
    stream_div = list()
    lst_to_return = list()

    for i in range(len(stream)):
        stream_div.append(stream[i].split(","))

    stream_div.sort(
        key=lambda x: (x[0], x[1]))  # sort by time first, then alphabetical order
    
    time_key = list()
    value_key = list()
    dict_to_print = dict()

    for i in range(len(stream)):
        stream_div[i][2] = int(float(stream_div[i][2]))
        stream_div[i][3] = int(float(stream_div[i][2])) * float(stream_div[i][3])

    for i in range(len(stream)):
        if stream_div[i][0] in time_key:
            index = time_key.index(stream_div[i][0])
            value_key[index] += [
                stream_div[i][1],
                stream_div[i][2],
                stream_div[i][3]
            ]
            dict_to_print[str(time_key[index])] = list(value_key[index])
        else:
            time_key.append(stream_div[i][0])
            index = time_key.index(stream_div[i][0])
            if index == 0:
                value_key.append([
                    stream_div[i][j] for j in range(1, 4)
                ])
                dict_to_print[str(time_key[index])] = list(value_key[index])
            else:
                value_key.append(value_key[index - 1])
                for j in range(0, len(value_key[0]) // 3):
                    if value_key[-1][j * 3] == stream_div[i][1]:
                        value_key[-1][j * 3 + 1] += stream_div[i][2]
                        value_key[-1][j * 3 + 2] += stream_div[i][3]
                dict_to_print[str(time_key[index])] = list(value_key[index])
                
    for key, value in dict_to_print.items():
        to_print = key, *value
        lst_to_return.append(','.join([str(i) for i in to_print]))

    dict_to_return = {"output": lst_to_return}
    return dict_to_return
