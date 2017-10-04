from extensions import db


class Order(db.Model):

    __tablename__        = 'orders'
    order_id             = db.Column('id', db.Integer, primary_key=True, index=True)
    contact_name         = db.Column('contact_name', db.String(200))
    contact_phone        = db.Column('contact_phone', db.String(100))
    contact_email        = db.Column('contact_email', db.String(150))
    created              = db.Column('created', db.DateTime)
    confirmed            = db.Column('confirmed', db.DateTime,  nullable=True)
    comment              = db.Column('comment', db.Text())
    price                = db.Column('price', db.Float)


    def __repr__(self):
        return '<Order {order_id}>'.format(order_id=self.order_id)
