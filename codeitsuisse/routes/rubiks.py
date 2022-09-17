import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/rubiks', methods=['POST'])
def rubiks():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ops = data["ops"]
    state = data['state']
    result = rubik_cube(ops, state)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def rubik_cube(ops, state):
    ops = list(ops)
    action = list()
    
    final_state = [[] for _ in range(6)]
    
    for i in range(len(ops)):
        if ops[i] != "i":
            if i == len(ops)-1:
                action.append(ops[i])
            elif ops[i+1] == "i":
                temp = ops[i] + ops[i+1]
                action.append(temp)
            else:
                action.append(ops[i])
        else:
            continue          
    
    final_state[0] = state['u']    
    final_state[1] = state['l']
    final_state[2] = state['f']
    final_state[3] = state['r']
    final_state[4] = state['b']
    final_state[5] = state['d']

    for i in range(len(action)):
        if "U" in action[i]:
            if "i" in action[i]: #Ui
                final_state[1][0], final_state[2][0], final_state[3][0], final_state[4][0] = final_state[4][0], final_state[1][0], final_state[2][0], final_state[3][0]
            else: #U
                final_state[1][0], final_state[2][0], final_state[3][0], final_state[4][0] = final_state[2][0], final_state[3][0], final_state[4][0], final_state[1][0]
                
        elif "L" in action[i]:
            if "i" in action[i]:
                for j in range(3): #Li
                    final_state[0][j][0], final_state[4][j][0], final_state[5][j][0], final_state[2][j][0] = final_state[2][j][0], final_state[0][j][0], final_state[4][j][0], final_state[5][j][0]
            else:
                for j in range(3): #L
                    final_state[0][j][0], final_state[4][j][0], final_state[5][j][0], final_state[2][j][0] = final_state[4][j][0], final_state[5][j][0], final_state[2][j][0], final_state[0][j][0]

        elif "F" in action[i]:
            if "i" in action[i]: #Fi
                for j in range(3):
                    final_state[3][j][0], final_state[5][0][j], final_state[1][j][0], final_state[0][2][2-j] = final_state[5][0][j], final_state[1][j][0], final_state[0][2][2-j], final_state[3][j][0]
            else:
                for j in range(3):
                    final_state[5][0][j], final_state[1][j][2], final_state[0][2][2-j], final_state[3][2-j][0] = final_state[3][2-j][0], final_state[5][0][j], final_state[1][j][2], final_state[0][2][2-j]
            
        elif "R" in action[i]:
            if "i" in action[i]:
                for j in range(3): #Ri
                    final_state[0][j][2], final_state[4][j][2], final_state[5][j][2], final_state[2][j][2] = final_state[2][j][2], final_state[0][j][2], final_state[4][j][2], final_state[5][j][2]
            else:
                for j in range(3): #R
                    final_state[0][j][2], final_state[4][j][2], final_state[5][j][2], final_state[2][j][2] = final_state[4][j][2], final_state[5][j][2], final_state[2][j][2], final_state[0][j][2]
            
        elif "B" in action[i]:
            if "i" in action[i]: #Bi
                for j in range(3):
                    final_state[5][0][j], final_state[3][2-j][2], final_state[0][0][2-j], final_state[1][j][0] = final_state[3][2-j][2], final_state[0][0][2-j], final_state[1][j][0], final_state[5][0][j]
            else: #B
                for j in range(3):
                    final_state[0][0][j], final_state[3][j][2], final_state[5][2][2-j], final_state[1][2-j][0] = final_state[3][j][2], final_state[5][2][2-j], final_state[1][2-j][0], final_state[0][0][j]           
        
        else:
            if "i" in action[i]:             
                final_state[1][2], final_state[2][2], final_state[3][2], final_state[4][2] = final_state[2][2], final_state[3][2], final_state[4][2], final_state[1][2]
            else:
                final_state[1][2], final_state[2][2], final_state[3][2], final_state[4][2] = final_state[4][2], final_state[1][2], final_state[2][2], final_state[3][2]
        
        print(final_state)
    
    dict_to_return = dict()
    
    dict_to_return['u'] = final_state[0]
    dict_to_return['l'] = final_state[1]
    dict_to_return['f'] = final_state[2]
    dict_to_return['r'] = final_state[3]
    dict_to_return['b'] = final_state[4]
    dict_to_return['d'] = final_state[5]
    
    return dict_to_return
