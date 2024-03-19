# 新規登録画面のPythonファイル

# app/views/registration.py
from flask import Blueprint, render_template, request, redirect, url_for

registration_bp = Blueprint('registration', __name__, url_prefix='/registration')

@registration_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # フォームデータの処理
        pass
    return render_template('signup.html')
