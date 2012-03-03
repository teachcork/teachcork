from google.appengine.ext import db
from app.model import AbstractModel


class User(AbstractModel):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )

    first_name = db.StringProperty()
    last_name = db.StringProperty()
    nick_name = db.StringProperty()
    email = db.EmailProperty()
    password = db.StringProperty()
    gender = db.StringProperty()
    ip_address = db.StringProperty()
    phone = db.StringProperty()
    birth_date = db.DateProperty()
    image_url = db.StringProperty()

    facebook_account_id = db.StringProperty()
    twitter_account_id = db.Stringproperty()
    linkedin_account_id = db.Stringproperty()

    city = db.StringProperty()
    state = db.StringProperty()
    country = db.StringProperty()
    postal_code = db.StringProperty()
 
