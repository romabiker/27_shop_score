from extensions import db


class Order(db.Model):

    __tablename__        = 'orders'
    order_id             = db.Column('id', db.Integer, primary_key=True, index=True)
    created              = db.Column('created', db.DateTime)
    confirmed            = db.Column('confirmed', db.DateTime,  nullable=True)
