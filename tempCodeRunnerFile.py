class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token
        self.temp_counter = 0

session = [getattr(UserSession,attr)]

print(session)