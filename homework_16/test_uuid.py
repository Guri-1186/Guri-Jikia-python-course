import uuid
session_id = str(uuid.uuid4())
list_of_id = []
for _ in range(10):
    session_id = str(uuid.uuid4())
    list_of_id.append(session_id)
print(*list_of_id, sep = "\n")

