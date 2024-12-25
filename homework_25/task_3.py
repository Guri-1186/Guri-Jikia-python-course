import datetime

class TimestampMixin:
    def __init__(self):
        self.creation_time = datetime.datetime.now()
        self.modification_time = self.creation_time
    
    def get_creation_time(self):
        return self.creation_time
    
    def get_modification_time(self):
        return self.modification_time
    
    def update_modification_time(self):
        self.modification_time = datetime.datetime.now()

class File(TimestampMixin):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
    
    def rename_file(self, new_filename):
        self.filename = new_filename
        self.update_modification_time()
        
class User(TimestampMixin):
    def __init__(self, username):
        super().__init__()
        self.username = username
    
    def change_username(self, new_username):
        self.username = new_username
        self.update_modification_time()


file = File("document.txt")
print(f"File creation time: {file.get_creation_time()}")
print(f"File modification time: {file.get_modification_time()}")

file.rename_file("new_document.txt")
print(f"File new modification time: {file.get_modification_time()}")

user = User("Guri")
print(f"\nUser creation time: {user.get_creation_time()}")
print(f"User modification time: {user.get_modification_time()}")

user.change_username("Nick")
print(f"User new modification time: {user.get_modification_time()}")