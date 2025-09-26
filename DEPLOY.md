# 🚀 議事録スライド生成アプリ - デプロイ完了！

## 📋 GitHubリポジトリ
**https://github.com/Ayumu50/meeting-slides-generator**

## 🌐 Render.com でのデプロイ手順

### 1. Render.com アカウント作成
1. [Render.com](https://render.com) にアクセス
2. 「Get Started for Free」をクリック
3. GitHubアカウントでサインアップ

### 2. 新しいWebサービスを作成
1. Render ダッシュボードで「New +」→「Web Service」
2. 「Connect a repository」で GitHub を選択
3. `Ayumu50/meeting-slides-generator` を選択
4. 「Connect」をクリック

### 3. デプロイ設定
以下の設定を入力：

**基本設定:**
- **Name**: `meeting-slides-generator`
- **Region**: `Oregon (US West)`
- **Branch**: `main`
- **Runtime**: `Python 3`

**ビルド設定:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --chdir genpptx --bind 0.0.0.0:$PORT app:app`

**環境変数（オプション）:**
- `AZURE_OPENAI_API_KEY`: Azure OpenAI API キー
- `AZURE_OPENAI_ENDPOINT`: Azure OpenAI エンドポイント
- `AZURE_OPENAI_DEPLOYMENT`: `gpt-4o-mini`

### 4. デプロイ実行
1. 「Create Web Service」をクリック
2. 自動的にビルドとデプロイが開始されます
3. 完了すると公開URLが表示されます

## 📊 アプリの機能
- 議事録テキスト入力
- AI による自動解析（Azure OpenAI 設定時）
- PowerPoint スライド自動生成
- ファイルダウンロード

## 💰 コスト
- **Render.com**: 無料プラン（月750時間まで）
- **Azure OpenAI**: 使用量に応じた従量課金（オプション）

## 🔧 使用方法
1. デプロイ完了後のURLにアクセス
2. 議事録テキストを入力
3. 「PowerPoint スライド作成」ボタンをクリック
4. .pptx ファイルがダウンロードされます

## 🐛 トラブルシューティング

### デプロイエラー
- Render ダッシュボードの「Logs」タブでエラーログを確認
- `requirements.txt` の依存関係を確認

### 実行時エラー
- 環境変数が正しく設定されているか確認
- Azure OpenAI の設定を確認（オプション）

## 🔄 更新方法
1. ローカルでコードを修正
2. Git にコミット・プッシュ
3. Render が自動的に再デプロイ

```bash
git add .
git commit -m "Update feature"
git push origin main
```

## 📱 代替デプロイ方法

### Railway
1. [Railway.app](https://railway.app) でアカウント作成
2. GitHub リポジトリを接続
3. 自動デプロイ

### Vercel
1. [Vercel.com](https://vercel.com) でアカウント作成
2. GitHub リポジトリをインポート
3. Python ランタイムを選択

### Heroku（有料）
1. アカウント認証完了後
2. `heroku create app-name`
3. `git push heroku main`