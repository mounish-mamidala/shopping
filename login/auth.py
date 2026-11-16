class Authentication:

    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if not username or not password:
            return "Username and password required"

        if username in self.users:
            return "User already exists"

        self.users[username] = password
        return "Registration successful"

    def login(self, username, password):
        if self.users.get(username) == password:
            return "Login successful"

        return "Invalid username or password"