import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tickerStream1', methods=['POST'])
def tickerStream1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    stream = data["stream"]
    result = to_cumulative(stream)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def to_cumulative(stream):
    result = {}
    for i in stream:
        i = i.split(',')
        if i[0] not in result:
            result[i[0]] = {i[1]: [float(i[2]), float(i[2]) * float(i[3])]}
        else:
            if i[1] not in result[i[0]]:
                result[i[0]][i[1]] = [float(i[2]), float(i[2]) * float(i[3])]
            else:
                result[i[0]][i[1]][0] += float(i[2])
                result[i[0]][i[1]][1] += float(i[2]) * float(i[3])
    final_answer = []

    for i in result:
        answer = [i]
        for j in sorted(result[i]):
            answer += [j, str(int(result[i][j][0])), str(result[i][j][1])]
        final_answer.append(','.join(answer))
        
    dict_to_return = {"output": final_answer}    
    return dict_to_return
    #raise Exception