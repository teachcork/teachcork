from google.appengine.ext import db


class User(db.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    email = db.EmailProperty()
    password = db.StringProperty()
    gender = db.StringProperty()
    ip_address = db.StringProperty()
    city = db.StringProperty()
    state = db.StringProperty()
    country = db.StringProperty()


class Teacher(db.Model):
    user = db.ReferenceProperty(User)


class Class(db.Model):
    teacher = db.ReferenceProperty(Teacher)
