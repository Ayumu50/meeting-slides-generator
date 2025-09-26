# Python 3.12のベースイメージを使用
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# システムパッケージの更新とクリーンアップ
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 依存関係ファイルをコピー
COPY requirements.txt .

# Python依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# Gunicornをインストール
RUN pip install gunicorn

# アプリケーションファイルをコピー
COPY genpptx/ ./genpptx/

# ポート5000を公開
EXPOSE 5000

# 本番環境用の設定
ENV FLASK_ENV=production
ENV FLASK_DEBUG=False

# 作業ディレクトリをgenpptxに変更
WORKDIR /app/genpptx

# Gunicornを使用してアプリケーションを起動
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "app:app"]