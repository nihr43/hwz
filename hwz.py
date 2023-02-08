#!/usr/bin/python3

import pySMART
from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api


def check_disks():
    '''
    returns list containing dicts representing each disk
    '''
    disks = pySMART.DeviceList()
    json = []

    for i in disks:
        attributes = []
        for a in i.attributes:
            if hasattr(a, 'raw_int'):
                if a.name != 'Unknown_Attribute':
                    attributes.append({a.name: a.raw_int})

        json.append({'name': i.name,
                     'state': i.assessment,
                     'model': i.model,
                     'attributes': attributes})
    return json


def check_ecc_events():
    '''
    returns dict containing ecc error count
    '''
    ecc_events = {"ecc_error_count": 0}
    with open(r'/var/log/kern.log', 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            if 'Machine check events logged' in row:
                ecc_events['ecc_error_count'] += 1
    return ecc_events


if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)

    class all_stats(Resource):
        def get(self):
            return(jsonify(disks=check_disks(),
                           memory=check_ecc_events()))

    api.add_resource(all_stats, '/healthz/')
    app.run(host='0.0.0.0', port='5000')
