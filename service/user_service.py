from dao.user_dao import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def post(self, data):
        return self.dao.post(data)

    def put(self, uid, data):
        user = self.get_one(uid)
        user.id = data.get("id")
        user.username = data.get("username")
        user.password = data.get("password")
        user.role = data.get("role")
        self.dao.put(user)

    def delete(self, uid):
        return self.dao.delete(uid)
