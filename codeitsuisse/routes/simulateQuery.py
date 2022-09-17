from asyncio.windows_events import NULL
import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/simulateQuery', methods=['POST'])
def simulateQuery():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    cachesize = data["cacheSize"]
    log = data["log"]
    result = query(cachesize, log)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def query(cachesize, log):
    x =[
  { "status": 'cache miss', "ipAddress": '1.2.3.4' },
  { "status": 'cache hit', "ipAddress": '1.2.3.4' },
  { "status": 'cache miss', "ipAddress": '2.3.4.5' },
  { "status": 'cache miss', "ipAddress": '6.7.8.9' },
  { "status": 'cache hit', "ipAddress": '1.2.3.4' },
  { "status": 'cache miss', "ipAddress": '4.5.6.7' },
  { "status": 'cache hit', "ipAddress": '6.7.8.9' },
  { "status": 'invalid', "ipAddress": NULL }
]
    return x