import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/instantiateDNSLookup', methods=['POST'])
def instantiateDNSLookup():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    table = data["lookupTable"]
    result = dns(table)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def dns(table):
    
    return {"content":table,"success": True}