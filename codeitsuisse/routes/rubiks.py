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
    
    dict_to_return = dict()
    final_state = state
    
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
        
    for i in range(len(action)):
        direction = ""
        if 'i' in action[i]:
            direction = '-'
        else:
            direction = '+'
            
        if "L" in action[i]:
            if direction == '-':
                 final_state['u'][0][0],  final_state['b'][-1][-1],  final_state['d'][0][0],  final_state['f'][0][0] =  final_state['f'][0][0],  final_state['u'][0][0],  final_state['b'][-1][-1],  final_state['d'][0][0]
                 final_state['u'][1][0],  final_state['b'][-2][-1],  final_state['d'][1][0],  final_state['f'][1][0] =  final_state['f'][1][0],  final_state['u'][1][0],  final_state['b'][-2][-1],  final_state['d'][1][0]
                 final_state['u'][2][0],  final_state['b'][-3][-1],  final_state['d'][2][0],  final_state['f'][2][0] =  final_state['f'][2][0],  final_state['u'][2][0],  final_state['b'][-3][-1],  final_state['d'][2][0]
            elif direction == '+':
                 final_state['u'][0][0],  final_state['f'][0][0],  final_state['d'][0][0],  final_state['b'][-1][-1] =  final_state['b'][-1][-1],  final_state['u'][0][0],  final_state['f'][0][0],  final_state['d'][0][0]
                 final_state['u'][1][0],  final_state['f'][1][0],  final_state['d'][1][0],  final_state['b'][-2][-1] =  final_state['b'][-2][-1],  final_state['u'][1][0],  final_state['f'][1][0],  final_state['d'][1][0]
                 final_state['u'][2][0],  final_state['f'][2][0],  final_state['d'][2][0],  final_state['b'][-3][-1] =  final_state['b'][-3][-1],  final_state['u'][2][0],  final_state['f'][2][0],  final_state['d'][2][0]
        elif 'R' in action[i]:
            if direction == '-':
                 final_state['u'][0][-1],  final_state['f'][0][-1],  final_state['d'][0][-1],  final_state['b'][-1][0] =  final_state['b'][-1][0],  final_state['u'][0][-1],  final_state['f'][0][-1],  final_state['d'][0][-1]
                 final_state['u'][1][-1],  final_state['f'][1][-1],  final_state['d'][1][-1],  final_state['b'][-2][0] =  final_state['b'][-2][0],  final_state['u'][1][-1],  final_state['f'][1][-1],  final_state['d'][1][-1]
                 final_state['u'][2][-1],  final_state['f'][2][-1],  final_state['d'][2][-1],  final_state['b'][-3][0] =  final_state['b'][-3][0],  final_state['u'][2][-1],  final_state['f'][2][-1],  final_state['d'][2][-1]
            elif direction=='+':
                 final_state['u'][0][-1],  final_state['b'][-1][0],  final_state['d'][0][-1],  final_state['f'][0][-1] =  final_state['f'][0][-1],  final_state['u'][0][-1],  final_state['b'][-1][0],  final_state['d'][0][-1]
                 final_state['u'][1][-1],  final_state['b'][-2][0],  final_state['d'][1][-1],  final_state['f'][1][-1] =  final_state['f'][1][-1],  final_state['u'][1][-1],  final_state['b'][-2][0],  final_state['d'][1][-1]
                 final_state['u'][2][-1],  final_state['b'][-3][0],  final_state['d'][2][-1],  final_state['f'][2][-1] =  final_state['f'][2][-1],  final_state['u'][2][-1],  final_state['b'][-3][0],  final_state['d'][2][-1]
        elif 'F' in action[i]:
            if direction == '-':
                 final_state['u'][-1][0],  final_state['l'][-1][-1],  final_state['d'][0][-1],  final_state['r'][0][0] =  final_state['r'][0][0],  final_state['u'][-1][0], final_state['l'][-1][-1], final_state['d'][0][-1]
                 final_state['u'][-1][1],  final_state['l'][-2][-1],  final_state['d'][0][-2],  final_state['r'][1][0] =  final_state['r'][1][0],  final_state['u'][-1][1], final_state['l'][-2][-1], final_state['d'][0][-2]
                 final_state['u'][-1][2],  final_state['l'][-3][-1],  final_state['d'][0][-3],  final_state['r'][2][0] =  final_state['r'][2][0], final_state['u'][-1][2], final_state['l'][-3][-1], final_state['d'][0][-3]
            elif direction=='+':
                 final_state['u'][-1][0],  final_state['r'][0][0],  final_state['d'][0][-1],  final_state['l'][-1][-1] =  final_state['l'][-1][-1], final_state['u'][-1][0], final_state['r'][0][0], final_state['d'][0][-1]
                 final_state['u'][-1][1],  final_state['r'][1][0],  final_state['d'][0][-2],  final_state['l'][-2][-1] =  final_state['l'][-2][-1], final_state['u'][-1][1], final_state['r'][1][0], final_state['d'][0][-2]
                 final_state['u'][-1][2],  final_state['r'][2][0],  final_state['d'][0][-3],  final_state['l'][-3][-1] =  final_state['l'][-3][-1], final_state['u'][-1][2], final_state['r'][2][0], final_state['d'][0][-3]
        elif 'B' in action[i]:
            if direction == '-':
                 final_state['u'][0][-1],  final_state['r'][-1][-1],  final_state['d'][-1][0],  final_state['l'][0][0] =  final_state['l'][0][0], final_state['u'][0][-1], final_state['r'][-1][-1], final_state['d'][-1][0]
                 final_state['u'][0][-2],  final_state['r'][-2][-1],  final_state['d'][-1][1],  final_state['l'][1][0] =  final_state['l'][1][0], final_state['u'][0][-2], final_state['r'][-2][-1], final_state['d'][-1][1]
                 final_state['u'][0][-3],  final_state['r'][-3][-1],  final_state['d'][-1][2],  final_state['l'][2][0] =  final_state['l'][2][0], final_state['u'][0][-3], final_state['r'][-3][-1], final_state['d'][-1][2]
            elif direction == '+':
                 final_state['u'][0][-1],  final_state['l'][0][0],  final_state['d'][-1][0], final_state['r'][-1][-1] =  final_state['r'][-1][-1], final_state['u'][0][-1], final_state['l'][0][0], final_state['d'][-1][0]
                 final_state['u'][0][-2],  final_state['l'][1][0],  final_state['d'][-1][1], final_state['r'][-2][-1] =  final_state['r'][-2][-1], final_state['u'][0][-2], final_state['l'][1][0], final_state['d'][-1][1]
                 final_state['u'][0][-3],  final_state['l'][2][0], final_state['d'][-1][2], final_state['r'][-3][-1] =  final_state['r'][-3][-1], final_state['u'][0][-3], final_state['l'][2][0], final_state['d'][-1][2]
        elif 'U' in action[i]:
            if direction == '-':
                 final_state['f'][0][0],  final_state['r'][0][0], final_state['b'][0][0], final_state['l'][0][0] =  final_state['l'][0][0], final_state['f'][0][0], final_state['r'][0][0], final_state['b'][0][0]
                 final_state['f'][0][1],  final_state['r'][0][1], final_state['b'][0][1], final_state['l'][0][1] =  final_state['l'][0][1], final_state['f'][0][1], final_state['r'][0][1], final_state['b'][0][1]
                 final_state['f'][0][2],  final_state['r'][0][2], final_state['b'][0][2], final_state['l'][0][2] =  final_state['l'][0][2], final_state['f'][0][2], final_state['r'][0][2], final_state['b'][0][2]
            elif direction=='+':
                 final_state['f'][0][0],  final_state['l'][0][0], final_state['b'][0][0], final_state['r'][0][0] =  final_state['r'][0][0], final_state['f'][0][0], final_state['l'][0][0], final_state['b'][0][0]
                 final_state['f'][0][1],  final_state['l'][0][1], final_state['b'][0][1], final_state['r'][0][1] =  final_state['r'][0][1], final_state['f'][0][1], final_state['l'][0][1], final_state['b'][0][1]
                 final_state['f'][0][2],  final_state['l'][0][2], final_state['b'][0][2], final_state['r'][0][2] =  final_state['r'][0][2], final_state['f'][0][2], final_state['l'][0][2], final_state['b'][0][2]
        elif 'D' in action[i]:
            if direction == '-':
                 final_state['f'][-1][0],  final_state['l'][-1][0], final_state['b'][-1][0], final_state['r'][-1][0] =  final_state['r'][-1][0], final_state['f'][-1][0], final_state['l'][-1][0], final_state['b'][-1][0]
                 final_state['f'][-1][1],  final_state['l'][-1][1], final_state['b'][-1][1], final_state['r'][-1][1] =  final_state['r'][-1][1], final_state['f'][-1][1], final_state['l'][-1][1], final_state['b'][-1][1]
                 final_state['f'][-1][2],  final_state['l'][-1][2], final_state['b'][-1][2], final_state['r'][-1][2] =  final_state['r'][-1][2], final_state['f'][-1][2], final_state['l'][-1][2], final_state['b'][-1][2]
            elif direction == '+':
                 final_state['f'][-1][0],  final_state['r'][-1][0], final_state['b'][-1][0], final_state['l'][-1][0] =  final_state['l'][-1][0], final_state['f'][-1][0],  final_state['r'][-1][0],  final_state['b'][-1][0]
                 final_state['f'][-1][1],  final_state['r'][-1][1], final_state['b'][-1][1], final_state['l'][-1][1] =  final_state['l'][-1][1], final_state['f'][-1][1],  final_state['r'][-1][1], final_state['b'][-1][1]
                 final_state['f'][-1][2],  final_state['r'][-1][2], final_state['b'][-1][2], final_state['l'][-1][2] =  final_state['l'][-1][2], final_state['f'][-1][2],  final_state['r'][-1][2], final_state['b'][-1][2]
       
    dict_to_return['u'] = final_state['u']
    dict_to_return['l'] = final_state['l']
    dict_to_return['f'] = final_state["f"]
    dict_to_return['r'] = final_state["r"]
    dict_to_return['b'] = final_state["b"]
    dict_to_return['d'] = final_state["d"]
    
    return dict_to_return
