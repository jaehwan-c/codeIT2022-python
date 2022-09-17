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
    attempts = data["attempts"]
    numbers = data["numbers"]
    result = keyboard(answers, attempts, numbers)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def keyboard(answers, attempts, numbers):
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

    chunks = []
    for i in range(0, len(numbers),5):
        chunk = numbers[i:i + 5]
        chunks.append(chunk)

    binary = []
    for chunk in chunks:
        temp = []
        for c in chunk:
            if str(c) in part1:
                temp.append('1')
            else:
                temp.append('0')
        binary.append(''.join(temp))
    art2_alphabet = []
    for b in binary:
        part2_alphabet.append(chr(int(b,2)+64))

    part2_alphabet = ''.join(part2_alphabet)
    for alpha in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if alpha not in alphabet:
            part2_alphabet += alpha
    dict_to_return = {"part1": part1,"part2": part2_alphabet} 
    return dict_to_return