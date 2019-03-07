from blog import db
db.create_all()

from blog.models import User
from blog.models import Category

u=User('test',123456)
c=Category('title',"test title content")

db.session.add(u)
db.session.add(c)

db.session.commit()

