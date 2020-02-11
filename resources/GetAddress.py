import config
import requests
from flask_restful import Resource
from flask import request as req


class GetAddress(Resource):
    def get(self):
        base_uri = config.GOOGLE_APIS['geocoding']
        
        payload = {
            "latlng": "%s,%s" % (req.args['lat'], req.args['lng']),
            "key": config.GOOGLE_API_KEY
        }
        send = requests.get(base_uri, params=payload)
        
        status_code = 200
        
        return send.json(), status_code
