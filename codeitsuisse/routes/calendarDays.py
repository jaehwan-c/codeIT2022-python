import logging
import json
import numpy
from datetime import date
from datetime import datetime

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
            solution += day_string

    for i in range(len(solution)):
        if solution[i] == ' ':
            whitespace = i
            break

    days_str = {1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat',7:'Sun'}
    whitespace = whitespace + 2001
    part2_solution = [whitespace]
    temp_solution = set()
    for j in range(1,13):
        for k in list(month_calendar[j]):
            if len(str(j)) == 1:
                yearMonth = str(whitespace) + '-0' + str(j)
            else:
                yearMonth = str(whitespace) + str(j)  
            part2 = numpy.busday_offset(yearMonth, 0,roll='forward',weekmask=days_str[k])
            part2 = part2.astype(datetime)
            temp_solution.add(part2.timetuple().tm_yday)
    temp_solution = sorted(list(temp_solution))
    part2_solution = part2_solution + temp_solution

    dict_to_return = {"part1": solution,"part2":part2_solution}
    return dict_to_return
