import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tickerStreamPart2', methods=['POST'])
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

    final_answer= {}
    temp = []
    prev_count = {}
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
                i, count, round(cumulative,1), delayed_i, delayed_count,
                round(delayed_cumulative,1)
            ]
        ans = [i]
        for k in final_answer:
            
            cnt = final_answer[k][4]
            cum = final_answer[k][5]
            if k not in prev_count:
                prev_count[k] = 0
            if (cnt != 0) and (cnt%quantity_block==0) and (cnt > prev_count[k]):
                ans += [k,str(cnt),str(cum)]
                prev_count[k] = cnt
        if len(ans) > 1:
            temp.append(','.join(ans))
    dict_to_return = {"output":temp}
    return dict_to_return