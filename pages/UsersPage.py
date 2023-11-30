class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Users:
    def __init__(self):
        self.users_list = [
            User("natalia.mateus+mf@zemoga.com", "Tester5678$"),
            User("natalia.mateus+tp@zemoga.com", "Tester1234*"),
            User("natalia.mateus@zemoga.com", "Tester5678$")
        ]

    def validate_credentials(self, username, password):
        for user in self.users_list:
            if user.username == username and user.password == password:
                return True
        return False
