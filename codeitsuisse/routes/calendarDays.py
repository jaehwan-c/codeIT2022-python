import logging
import json
from datetime import date

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/calendarDays', methods=['POST'])
def calendarDays1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    numbers = data["numbers"]
    result = calendar1(numbers)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def calendar1(numbers):
    
    solution = ""
    year = numbers[0]
    days = numbers[1:]
    month_calendar = {}

    for k in range(1,13):
        month_calendar[k] = set()

    for day in days:
        if (day < 1) or (day > 365):
            continue
        temp = date.fromordinal(date(year, 1, 1).toordinal() + day - 1)
        month = temp.month
        month_calendar[month].add(temp.isoweekday())

    weekday = [1,2,3,4,5]
    weekend = [6,7]
    allday = [1,2,3,4,5,6,7]
    days_dict = {1:'m',2:'t',3:'w',4:'t',5:'f',6:'s',7:'s'}
    for i in month_calendar:
        if len(month_calendar[i]) == 0:
            solution += "       ,"
        elif month_calendar[i] == set(weekend):
            solution += "weekend,"
        elif month_calendar[i] == set(weekday):
            solution += "weekday,"
        elif month_calendar[i] == set(allday):
            solution += "alldays,"
        else:
            day_string=''
            for j in days_dict:
                if j in month_calendar[i]:
                    day_string += days_dict[j]
                else:
                    day_string += ' '
                if j == 7:
                    day_string += ','

    dict_to_return = {"part1":solution,"part2":[]}
    return dict_to_return
