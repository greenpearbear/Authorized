from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre_model import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genre = genre_service.get_all()
        return GenreSchema(many=True).dump(all_genre), 200

    def post(self):
        req_json = request.json
        new_genre = genre_service.post(req_json)
        return "", 201, {"location": f"/genres/{new_genre.id}"}


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid: int):
        try:
            genre = genre_service.get_one(uid)
            return GenreSchema().dump(genre), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid: int):
        try:
            req_json = request.json
            genre = genre_service.put(uid, req_json)
            return GenreSchema().dump(genre), 200
        except Exception as e:
            return str(e), 404

    def delete(self, uid: int):
        try:
            genre_service.delete(uid)
            return "", 204
        except Exception as e:
            return str(e), 404
