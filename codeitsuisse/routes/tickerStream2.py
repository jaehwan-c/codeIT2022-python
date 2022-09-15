import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tickerStream2', methods=['POST'])
def tickerStream2():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    quantity_block = data["quantityBlock"]
    stream = data["stream"]
    result = to_cumulative_delayed(stream, quantity_block)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def to_cumulative_delayed(stream, quantity_block):
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
    for i in sorted(result):
        for j in sorted(result[i]):
            if j not in final_answer:
                count = 0
                cumulative = 0
                delayed_count = 0
                delayed_cumulative = 0
                delayed_i = i
            else:
                count = final_answer[j][1]
                cumulative = final_answer[j][2]
                delayed_count = final_answer[j][4]
                delayed_cumulative = final_answer[j][5]
                delayed_i = final_answer[j][3]
            for k in range(int(result[i][j][0])):
                cumulative += (result[i][j][1] / result[i][j][0])
                count += 1
                if count % quantity_block == 0:
                    delayed_count = count
                    delayed_cumulative = cumulative
                    delayed_i = i
            final_answer[j] = [
                i, count, cumulative, delayed_i, delayed_count,
                delayed_cumulative
            ]

    sorted_final_answer = sorted(final_answer.items(),
                                 key=lambda item: item[1][3])

    last = []
    for i in sorted_final_answer:
        temp = [i[1][3], i[0], str(i[1][4]), str(i[1][5])]
        last.append(','.join(temp))
    return last