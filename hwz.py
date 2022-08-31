#!/usr/bin/python3

import pySMART
from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api


def main():
    app = Flask(__name__)
    api = Api(app)

    class all_stats(Resource):
        def get(self):
            disks_output = check_disks()
            return(jsonify(disks=disks_output))

    api.add_resource(all_stats, '/healthz/')
    app.run(host='0.0.0.0', port='5000')


# returns list of dicts parsable by jsonify
def check_disks():
    disks = pySMART.DeviceList()
    json = []

    for i in disks:
        json.append({'name': i.name,
                     'state': i.assessment,
                     'model': i.model,
                     'reallocated_block_count': i.attributes[5].raw_int,
                     'read_error_rate': i.attributes[1].raw_int})
    return json


if __name__ == '__main__':
    main()
