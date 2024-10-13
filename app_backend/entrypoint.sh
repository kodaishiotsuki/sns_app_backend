#!/bin/sh

# DATABASE 環境変数が "postgres" の場合、PostgreSQLが起動しているかを確認
if [ "$DATABASE" = "postgres" ] 
then
    echo "データベースが起動中か確認しています..."

    # データベースが起動するまで、接続確認を0.1秒間隔でリトライ
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "データベースが正常に起動しました :-D"
fi

# Djangoのマイグレーションファイルを作成
python manage.py makemigrations
# Djangoのマイグレーションを適用
python manage.py migrate

# 最後に渡されたコマンドを実行（通常はrunserver）
exec "$@"
