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

    final_answer = {}
    tickers = set()
    for i in sorted(result):
    
        final_answer[i] = {}

        for j in sorted(list(tickers)):
            if j in result[i]:
                final_answer[i][j] = [(final_answer[prev_i][j][0] + result[i][j][0]),(final_answer[prev_i][j][1] + result[i][j][1])]
            else:
                final_answer[i][j] = [final_answer[prev_i][j][0],final_answer[prev_i][j][1] ]

        for k in result[i]:
            if k not in tickers:
                final_answer[i][k] = [result[i][k][0], result[i][k][1],1]           
                tickers.add(k)
        prev_i = i       
          
    solution = []
    for i in final_answer:
        answer = [i]
        for j in final_answer[i]:
            answer += [j, str(int(final_answer[i][j][0])), str(round(final_answer[i][j][1],1))]
        solution.append(','.join(answer)) 
    dict_to_return = {"output":solution} 

    return dict_to_return
