class LoginService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, username, password):
        user = self.user_repository.get_user(username)
        if user is None:
            return False
        return user.password == password