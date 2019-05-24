# ORM and user authentification will be added afterwards

class User(UserMixin):
    users = {}
    count = 0

    @classmethod
    def add_user(cls, obj):
        cls.count += 1
        if obj.username in cls.users:
            obj.username += str(cls.count)
        cls.users[obj.username] = (obj.name, obj.surname)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.username = self.name + self.surname
        self.add_user(self)

    def __repr__(self):
        return '<User {0}>'.format(self.username)
