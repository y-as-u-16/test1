# app/__init__.py
from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'user'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'mydatabase'

    mysql.init_app(app)

    with app.app_context():
        from .views import view1, view2

    return app
