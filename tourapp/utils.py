import json, os
from tourapp import app, db
from tourapp.models import Category, Product, User, UserRole, Bill
import hashlib # băm pass word

from functools import wraps
from flask_login import current_user
from flask import redirect
from sqlalchemy import func, extract

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_categories():
    return Category.query.all()
    # return read_json(os.path.join(app.root_path, 'data/catgories.json'))


def load_product(cate_id=None, kw=None, from_price=None, to_price=None):
    products = Product.query.filter(Product.active.__eq__(True))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
    if kw:
        products = products.filter(Product.name.contains(kw))
    if from_price:
        products = products.filter(Product.price_big.__ge__(from_price))
    if to_price:
        products = products.filter(Product.price_small.__le__(to_price))
    return products
    # products = read_json(os.path.join(app.root_path, 'data/products.json'))
    #
    # if cate_id:
    #     products = [p for p in products if p["category_id"] == int(cate_id)]
    # if kw:
    #     products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
    # if from_price:
    #     products = [p for p in products if p['price'] >= float(from_price)]
    # if to_price:
    #     products = [p for p in products if p['price'] <= float(to_price)]
    # return products


def get_product_by_id(product_id):
    return Product.query.get(product_id)
    # products = read_json(os.path.join(app.root_path, 'data/products.json'))
    #
    # for p in products:
    #     if p['id'] == product_id:
    #         return p
    # return None


def add_bill(name, email, amount_big, amount_young, phone, address, cccd, total, pay_date, product_id, user_id):
    user = Bill(name=name.strip(),
                email=email.strip(),
                amount_big=amount_big.strip(),
                amount_young=amount_young.strip(),
                phone=phone.strip(),
                address=address.strip(),
                cccd=cccd.strip(),
                product_id=product_id.strip(),
                total=total,
                pay_date=pay_date,
                user_id=user_id)

    db.session.add(user)
    db.session.commit()


def get_bill_by_user_id(user_id):
    bills = Bill.query.filter(Bill.active.__eq__(True))

    if user_id:
        bills = bills.filter(Bill.user_id.__eq__(user_id))
    return bills


def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name.strip(),
                username=username.strip(),
                password=password,
                email=kwargs.get('email'))
    db.session.add(user)
    db.session.commit()


def check_login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password)).first()


def check_user(username, password, role=UserRole.USER):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password),
                             User.user_role.__eq__(role)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def anmonymous_user(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect('/')
        return f(*args, **kwargs)

    return decorated_func


def stats_revenue(month = None):
    query = db.session.query(Bill.pay_date,Product.name, func.sum(Bill.total))\
                      .join(Bill, Bill.product_id.__eq__(Product.id))

    if month:
        query = query.filter(extract('month', Bill.pay_date).__eq__(month))

    return query.group_by(Bill.pay_date, Product.name).all()


def total_revenue(month = None):
    query = db.session.query(func.sum(Bill.total))

    if month:
        query = query.filter(extract('month', Bill.pay_date).__eq__(month))

    return query.all()


def count_tour_by_cate(month = None):
    query = db.session.query(Product.name,Product.price_big, func.count(Bill.product_id))\
            .join(Bill, Bill.product_id.__eq__(Product.id), isouter=True)
    if month:
        query = query.filter(extract('month', Bill.pay_date).__eq__(month))

    return query.group_by(Product.name, Product.price_big).all()


def update_pass(username,p):
    p = str(hashlib.md5(p.strip().encode('utf-8')).hexdigest())
    User.query.filter_by(username=username).first().password = p
    db.session.commit()