from google.appengine.ext import db
from app.model import AbstractModel
from app.model import Place
from app.model import Teacher

EASY, MEDIUM, HARD = range(3)


class Clase(AbstractModel):
    name = db.StringProperty()
    description  = db.StringProperty()
    difficulty_level = db.IntegerProperty(default=MEDIUM)
    website = db.LinkProperty()
    delivery_service = db.BooleanProperty(default=False)
    language = db.StringProperty()
    category = db.StringProperty()
    subcategory = db.StringProperty()
    place = db.ReferencePropert(Place)
    teacher = db.ReferenceProperty(Teacher)
    # price = db.ReferenceProperty(Price) ????
    # amount currency how are we going to manage this
