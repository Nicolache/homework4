from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app_base_path = os.path.dirname(os.path.abspath(__file__))
app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
app = Flask(app_name)
app.secret_key = b'012465789'
db_folder = os.path.join(app_base_path, 'db')
if not os.path.exists(db_folder):
    os.mkdir(db_folder)
db_file = '%s.db' % os.path.join(db_folder, app_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
