# app/models.py
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.completed_tutorials = []
        self.completed_challenges = []

    def get_id(self):
        return self.id

# In-memory user store (for demonstration purposes)
users = {}