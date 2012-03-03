from google.appengine.ext import db
from app.model import AbstractModel


class Place(AbstractModel):
    name = db.StringProperty()
    address = db.StringProperty()
    address_number = db.StringProperty()
    address_complement = db.StringProperty()
    city = db.StringProperty()
    state = db.StringProperty()
    country = db.StringProperty()
    postal_code = db.StringProperty()
    coordinates = db.GeoPtProperty()
