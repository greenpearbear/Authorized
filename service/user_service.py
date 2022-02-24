import hashlib
import base64
from dao.user_dao import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def post(self, data):
        data['password'] = self.generate_password(data['password'])
        return self.dao.post(data)

    def put(self, uid, data):
        user = self.get_one(uid)
        user.id = data.get("id")
        user.username = data.get("username")
        user.password = self.generate_password(data['password'])
        user.role = data.get("role")
        self.dao.put(user)

    def delete(self, uid):
        return self.dao.delete(uid)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)
