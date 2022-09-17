import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/quordleKeyboard', methods=['POST'])
def quordleKeyboard():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    answers = data["answers"]
    attemps = data["attemps"]
    numbers = data["numbers"]
    result = keyboard(answers, attemps, numbers)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def keyboard(answers, attemps, numbers):
    i = 9
    alphabet = {}
    print(set(''.join(answers)))
    for attempt in attempts:
        if attempt in answers:
            answers.remove(attempt)
        for char in attempt:
        
            if char not in set(''.join(answers)):
                if char not in alphabet:
                    print(char,i)
                    alphabet[char] = str(i)
        i -= 1

    alphabet = dict(sorted(alphabet.items()))
    part1 = ''.join(list(alphabet.values()))
    dict_to_return = {"part1": part1,"part2": ""}  
    return dict_to_return