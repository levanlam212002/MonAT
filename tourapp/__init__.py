import cloudinary
import paypalrestsdk as paypalrestsdk
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_admin import Admin
from flask_login import LoginManager



app = Flask(__name__)
app.secret_key = '689567gh$^^&*#%^&*^&%^*DFGH^&*&*^*'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:%s@localhost/mytour?charset=utf8mb4' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['CART_KEY'] = 'cart'
db = SQLAlchemy(app=app)

cloudinary.config(
  cloud_name="dscgr0uz7",
  api_key="733838136987965",
  api_secret="9EoH7kRaSdUq9EU2akhPHAN4qcE",
  secure=True
)

paypalrestsdk.configure({
  "mode": "sandbox",
  "client_id":"AaLiKSVM8MW6wvwnkQgcmHJq-PcDCrxW8F9Ce9TXPI3ylX0INo0FoMGBJmegeFCOJUlsQLws8PCPPIzo",
  "client_secret": "EOim3geG1r7r0IEdRLwSEt_3nfjILskcpRVoAwoWX_QzeyHxZ1MSFpPGGWCYOwTZD7oa2DEojMeHR8jh"
})

login = LoginManager(app=app)