#!/usr/bin/python3

import pySMART
from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api


# returns list of dicts parsable by jsonify
def check_disks():
    disks = pySMART.DeviceList()
    json = []

    for i in disks:
        json.append({'name': i.name,
                     'state': i.assessment,
                     'model': i.model,
                     'reallocated_block_count': i.attributes[5].raw_int,
                     'read_error_rate': i.attributes[1].raw_int,
                     'temp': (i.attributes[190] or i.attributes[194]).raw_int})
    return json


def check_ecc_events():
    ecc_count = 0
    with open(r'/var/log/kern.log', 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            word = 'mce: [Hardware Error]: Machine check events logged'
            if row.find(word) == 0:
                ecc_count += 1
    return ecc_count


if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)

    class all_stats(Resource):
        def get(self):
            disks_output = check_disks()
            ecc_events = {"ecc_error_count": check_ecc_events()}
            return(jsonify(disks=disks_output, ecc=ecc_events))

    api.add_resource(all_stats, '/healthz/')
    app.run(host='0.0.0.0', port='5000')
