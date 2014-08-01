from app import db, models
#u = models.User(nickname='John', email='john@gmail.com', role=models.ROLE_USER)
#u = models.User(nickname='Susan', email='susan@gmail.com', role=models.ROLE_USER)
#db.session.add(u)
#db.session.commit()
users = models.User.query.all()
print users
for u in users:
    print u.id, u.nickname