from extensions import db


class Order(db.Model):
    __tablename__        = 'orders'
    created              = db.Column('created', db.DateTime)
    confirmed            = db.Column('confirmed', db.DateTime,  nullable=True)
