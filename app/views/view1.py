# Flaskのリクエスト関連の関数とクラスをインポート
from flask import request, render_template, redirect, url_for, current_app

# ログインページ
@app.route('/', methods=['GET', 'POST'])
def login():
    # POSTリクエストをチェック
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # MySQLオブジェクトへのアクセスが必要な場合は、current_appを使用
        mysql = current_app.extensions['mysql']
        cur = mysql.connection.cursor()
        
        # 簡単なユーザー名とパスワードのチェック
        cur.execute("SELECT * FROM users WHERE id=%s AND password=%s", (username, password))
        account = cur.fetchone()

        if account:
            return redirect(url_for('top'))
        else:
            return render_template('reverseForLogin.html')
    # GETリクエストの場合はログインページを表示
    return render_template('login.html')

# ホームページ
@app.route('/top')
def top():
    return render_template('top.html')
