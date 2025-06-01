from admin import Admin
from user import User
from database import Database

a = Admin('rolf', '1234', 3)
u = User('jose', 'password')

a.save()

users = [a, u]
for user in users:
    user.save()
print(Database.content)
