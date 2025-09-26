#!/bin/bash

echo "🚀 Heroku デプロイスクリプト"

# Heroku CLI の確認
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI が見つかりません。"
    echo "インストール: brew tap heroku/brew && brew install heroku"
    exit 1
fi

# Git の確認
if ! command -v git &> /dev/null; then
    echo "❌ Git が見つかりません。"
    exit 1
fi

echo "✅ 環境チェック完了"

# Heroku ログイン確認
if ! heroku auth:whoami &> /dev/null; then
    echo "🔐 Heroku にログインしてください..."
    heroku login
fi

echo "✅ Heroku 認証確認完了"

# Git リポジトリ初期化（まだの場合）
if [ ! -d ".git" ]; then
    echo "📦 Git リポジトリを初期化中..."
    git init
    git add .
    git commit -m "Initial commit for Heroku deployment"
else
    echo "📦 変更をコミット中..."
    git add .
    git commit -m "Update for deployment" || echo "変更なし、そのまま続行"
fi

# Heroku アプリ作成または確認
if ! heroku apps:info &> /dev/null; then
    echo "🆕 新しい Heroku アプリを作成中..."
    heroku create meeting-slides-$(date +%s)
else
    echo "✅ 既存の Heroku アプリを使用"
fi

# 環境変数設定（オプション）
echo "🔧 環境変数を設定しますか？ (y/N)"
read -r setup_env
if [[ $setup_env =~ ^[Yy]$ ]]; then
    echo "Azure OpenAI API Key を入力してください（空白でスキップ）:"
    read -r api_key
    if [ -n "$api_key" ]; then
        heroku config:set AZURE_OPENAI_API_KEY="$api_key"
    fi
    
    echo "Azure OpenAI Endpoint を入力してください（空白でスキップ）:"
    read -r endpoint
    if [ -n "$endpoint" ]; then
        heroku config:set AZURE_OPENAI_ENDPOINT="$endpoint"
    fi
    
    echo "Azure OpenAI Deployment 名を入力してください（デフォルト: gpt-4o-mini）:"
    read -r deployment
    deployment=${deployment:-gpt-4o-mini}
    heroku config:set AZURE_OPENAI_DEPLOYMENT="$deployment"
fi

# デプロイ実行
echo "🚀 Heroku にデプロイ中..."
git push heroku main

if [ $? -eq 0 ]; then
    echo "✅ デプロイ完了！"
    echo "🌐 アプリを開いています..."
    heroku open
    echo ""
    echo "📋 アプリ情報:"
    heroku apps:info
    echo ""
    echo "📊 ログを確認するには: heroku logs --tail"
else
    echo "❌ デプロイに失敗しました。"
    echo "📊 ログを確認してください: heroku logs --tail"
    exit 1
fi