from flask_restful import Resource

class GetLatLng(Resource):
    def get(self):
        return "Here we read the address and get his Lat and Long", 200