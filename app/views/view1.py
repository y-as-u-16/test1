# Flaskのリクエスト関連の関数とクラスをインポート
from flask import Blueprint, request, render_template, redirect, url_for, current_app

# Blueprintオブジェクトの作成
bp = Blueprint('view1', __name__)

# ログインページ
@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # MySQLオブジェクトへのアクセスが必要な場合は、current_appを使用
        mysql = current_app.extensions['mydatabase']
        cur = mysql.connection.cursor()
        
        cur.execute("SELECT * FROM users WHERE id=%s AND password=%s", (username, password))
        account = cur.fetchone()

        if account:
            return redirect(url_for('view1.top'))  # Blueprint名.view関数名
        else:
            return render_template('reverseForLogin.html')
    return render_template('login.html')

# ホームページ
@bp.route('/top')
def top():
    return render_template('top.html')
