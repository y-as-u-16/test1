FROM python:3

# WORKDIRを使用して、必要なディレクトリを作成し、ワーキングディレクトリとして設定
WORKDIR /opt/flask-app

# requirements.txtをコピー
COPY requirements.txt /tmp

# 依存関係のインストール
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# ワーキングディレクトリを指定することで、RUN mkdirは不要になります。
