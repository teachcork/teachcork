from google.appengine.ext import db
from app.model import AbstractModel
from app.model import User


class Teacher(AbstractModel):
    user = db.ReferenceProperty(User)
    website = db.LinkProperty()
