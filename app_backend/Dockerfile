# Python 3.12.2-slim-bullseye をベースイメージとして使用
FROM python:3.12.2-slim-bullseye

# 作業ディレクトリを設定
WORKDIR /usr/src/app_backend

# Pythonバイトコード（.pycファイル）の生成を抑制
ENV PYTHONDONTWRITEBYTECODE 1
# 出力をバッファリングせず、リアルタイムでログを出力する設定
ENV PYTHONUNBUFFERED 1

# システムパッケージを最新に更新し、netcat（ネットワーク接続確認用）をインストール
RUN apt-get update && apt-get install -y netcat

# pipを最新バージョンにアップグレード
RUN pip install --upgrade pip
# requirements.txtをコンテナにコピー
COPY ./requirements.txt .
# requirements.txtに記載されたPythonパッケージをインストール
RUN pip install -r requirements.txt

# entrypoint.shスクリプトをコンテナにコピー
COPY ./entrypoint.sh .
# Windowsの改行コード（CRLF）をLinuxの改行コード（LF）に変換
RUN sed -i 's/\r$//g' /usr/src/app_backend/entrypoint.sh
# entrypoint.shに実行権限を付与
RUN chmod +x /usr/src/app_backend/entrypoint.sh

# プロジェクトの全ファイルをコンテナにコピー
COPY . .

# entrypoint.shをエントリーポイントとして指定
ENTRYPOINT [ "/usr/src/app_backend/entrypoint.sh" ]
