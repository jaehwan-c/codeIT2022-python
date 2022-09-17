import logging
import json
import numpy
from datetime import date
from datetime import datetime

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/magiccauldrons', methods=['POST'])
def magiccauldrons():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    data_cell = data
    result = cell(data_cell)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def cell(data_cell):
    
    def part1(data):
        n=1
        size = 100
        flow_rate = data["flow_rate"]
        time = data["time"]
        row_number = data["row_number"]
        column_number = data["col_number"]
        total_flow = flow_rate * time
        while n <= row_number:
            total_size = size * (n*(n+1)/2)
            if total_flow > total_size:
                n += 1
            amount_in_depth = total_flow - (size*(((n-1)*(n-1+1))/2))
            time_in_n = amount_in_depth / flow_rate
            flow_rate_at_n = flow_rate / (2**(n-1))
            if (column_number == 0) or (column_number == n):
                water_at_cell = flow_rate_at_n * time_in_n
            else:
                water_at_cell = flow_rate_at_n * time_in_n * (n-1)
        return water_at_cell
    
    list_to_return = []
    for i in data_cell:
        solution = {}
        part1_sol = part1(i["part1"])
        solution["part1"] = part1_sol
        list_to_return.append(solution)
    
    return list_to_return

