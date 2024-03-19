# app/__init__.py
from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # MySQLの設定
    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'user'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'mydatabase'

    # MySQLをアプリケーションに初期化
    mysql.init_app(app)

    # Blueprintをインポートしてアプリケーションに登録
    from .views import login
    app.register_blueprint(login.bp)  # view1のBlueprintを登録
    # app.register_blueprint(view2.bp)  # view2がBlueprintを使う場合、同様に登録

    return app
