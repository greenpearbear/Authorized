from flask_restx import Resource, Namespace
from flask import request
from dao.model.director_model import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return DirectorSchema(many=True).dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = director_service.post(req_json)
        return "", 201, {"location": f"/directors/{new_director.id}"}


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid: int):
        try:
            director = director_service.get_one(uid)
            return DirectorSchema().dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid: int):
        try:
            req_json = request.json
            director = director_service.put(uid, req_json)
            return DirectorSchema().dump(director), 200
        except Exception as e:
            return str(e), 404

    def delete(self, uid: int):
        try:
            director_service.delete(uid)
            return "", 204
        except Exception as e:
            return str(e), 404
