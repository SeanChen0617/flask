from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin



class Stocks(db.Model):
    stock_code = db.Column(db.String(10), primary_key=True)
    stock_name = db.Column(db.String(50))
    stock_buy_in_price = db.Column(db.String, default="0.0")

    def __repr__(self):
        return '<Stock {} {}>'.format(self.stock_code, self.stock_name)