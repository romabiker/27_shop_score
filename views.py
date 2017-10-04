from datetime import datetime
import logging


from flask import Blueprint, render_template
from flask.helpers import get_debug_flag


from models import Order
from extensions import db


if get_debug_flag():
    logging.basicConfig(level=logging.INFO, format='%(message)s')


blueprint = Blueprint('dashboard', __name__,)


def get_timeout_color(timeout):
    if timeout < 7:
        return 'green'
    if 7 < timeout < 30:
        return 'yellow'
    if timeout > 30:
        return 'red'


@blueprint.route('/')
def score():
    all_today_orders = Order.query.filter(
        db.cast(Order.created, db.Date) == datetime.today().date())
    orders_report = {}
    open_orders_count = 0
    latest_open_order_timeout = 0
    if all_today_orders.count():
        open_orders = all_today_orders.filter(Order.confirmed.is_(None))
        open_orders_count=open_orders.count()
        confirmed_orders_count=all_today_orders.filter(
                                   Order.confirmed.isnot(None)).count()
        orders_report.update(dict(
            open_orders_count=open_orders_count,
            confirmed_orders_count=confirmed_orders_count,
            ))
        logging.info('confirmed_orders_count : {}'.format(confirmed_orders_count))
        logging.info('open_orders_count : {}'.format(open_orders_count))
    if open_orders_count:
        latest_open_order = open_orders.order_by(Order.created).first()
        if latest_open_order:
            latest_open_order_timeout = round(180 - (
                datetime.now() - latest_open_order.created).total_seconds()/60)
    logging.info('latest_open_order_timeout : {}'.format(latest_open_order_timeout))
    orders_report.update(dict(
        score_color=get_timeout_color(latest_open_order_timeout),
        latest_open_order_timeout=latest_open_order_timeout,
    ))
    logging.info('orders_report : {}'.format(orders_report))
    return render_template('score.html', orders_report=orders_report)
