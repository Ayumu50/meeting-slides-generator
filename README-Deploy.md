# 議事録スライド生成アプリ - デプロイガイド

## 🚀 Heroku デプロイ手順

### 前提条件
- Heroku CLI がインストール済み
- Git がインストール済み
- Heroku アカウント作成済み

### 1. Heroku CLI インストール
```bash
# macOS
brew tap heroku/brew && brew install heroku

# または公式サイトからダウンロード
# https://devcenter.heroku.com/articles/heroku-cli
```

### 2. Heroku ログイン
```bash
heroku login
```

### 3. Git リポジトリ初期化
```bash
git init
git add .
git commit -m "Initial commit"
```

### 4. Heroku アプリ作成
```bash
# アプリ名は自動生成
heroku create

# または特定の名前で作成
heroku create your-app-name
```

### 5. 環境変数設定（オプション）
```bash
# Azure OpenAI を使用する場合
heroku config:set AZURE_OPENAI_API_KEY=your_api_key
heroku config:set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
heroku config:set AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

### 6. デプロイ実行
```bash
git push heroku main
```

### 7. アプリ確認
```bash
heroku open
```

## 🔧 ワンクリックデプロイ

以下のボタンでHerokuに直接デプロイできます：

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## 📊 機能
- 議事録テキスト入力
- AI による自動解析（Azure OpenAI 設定時）
- PowerPoint スライド自動生成
- ファイルダウンロード

## 💰 コスト
- Heroku Eco プラン: 月$5（スリープ機能あり）
- Azure OpenAI: 使用量に応じた従量課金（オプション）

## 🔒 セキュリティ
- 環境変数による機密情報管理
- HTTPS 通信
- 一時的なファイル処理

## 🐛 トラブルシューティング

### デプロイエラー
```bash
# ログ確認
heroku logs --tail

# アプリ再起動
heroku restart
```

### 環境変数確認
```bash
heroku config
```

### ローカルテスト
```bash
heroku local web
```