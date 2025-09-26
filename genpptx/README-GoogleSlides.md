# 議事録 Google Slides 自動作成アプリ

## 📋 概要
営業の打ち合わせ議事録を入力すると、自動で Google Slides を作成するWebアプリケーションです。

## 🚀 セットアップ手順

### 1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 2. Google Cloud Console での設定

#### Google Cloud プロジェクトの作成
1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. 新しいプロジェクトを作成

#### API の有効化
以下のAPIを有効にしてください：
- Google Slides API
- Google Drive API

#### 認証情報の作成
1. 「認証情報」→「認証情報を作成」→「OAuth 2.0 クライアント ID」
2. アプリケーションの種類：「ウェブアプリケーション」
3. 承認済みのリダイレクト URI に追加：
   - `http://localhost:5000/oauth/callback`
4. 作成後、JSONファイルをダウンロード
5. ファイル名を `credentials.json` に変更
6. `genpptx/` フォルダに配置

### 3. 環境変数の設定
```bash
# .env ファイルを作成
cp genpptx/.env.example genpptx/.env

# 必要な値を設定
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
FLASK_SECRET_KEY=your-secret-key
```

### 4. アプリケーションの起動
```bash
cd genpptx
python app.py
```

## 🔧 使用方法

### 1. Google認証
1. アプリにアクセス: http://localhost:5000
2. 「Google でログイン」ボタンをクリック
3. Google アカウントでログインし、権限を許可

### 2. スライド作成
1. 議事録テキストを入力
2. 「Google Slides 作成」ボタンをクリック
3. 作成された Google Slides のリンクをクリック

## 📊 機能

### 自動解析機能
- **##見出し検出**: マークダウン形式の見出しを自動検出
- **会社名抽出**: 議事録から会社名を自動抽出
- **日時抽出**: 会議日時を自動抽出
- **AI解析**: Azure OpenAI による高精度な内容分析（オプション）

### Google Slides 生成
- **タイトルスライド**: 会社名と会議日時
- **セクションスライド**: ##見出しごとに1枚のスライド
- **箇条書き**: 自動的に箇条書き形式で整理
- **共有可能**: 作成されたスライドは即座に共有可能

## 🔒 セキュリティ

### 認証情報の管理
- OAuth 2.0 による安全な認証
- トークンはローカルファイルに保存
- 必要最小限の権限のみ要求

### データの取り扱い
- 議事録データは一時的に処理のみ
- Google Slides は作成者のアカウントに保存
- 機密情報の適切な管理

## 🐛 トラブルシューティング

### 認証エラー
```
credentials.json が見つかりません
```
→ Google Cloud Console で作成した認証情報ファイルを `genpptx/credentials.json` に配置

### API エラー
```
Google Slides API が有効になっていません
```
→ Google Cloud Console で Google Slides API と Google Drive API を有効化

### 権限エラー
```
insufficient permissions
```
→ OAuth 同意画面で必要な権限を許可

## 📝 議事録フォーマット例

```markdown
# トレノケート株式会社様

## 概要・目的
- 日時：2025年7月9日（水）
- 実施方法：オンライン（Microsoft Teams）
- 目的：AI・データ活用による人材育成・業務効率化のご提案

## 明確な課題・潜在的ニーズ
- 既存研修データの有効活用
- AIによる業務効率化の推進
- PoC（概念実証）を限定的な範囲で実施

## 合意したネクストアクション
- 具体的な提案内容の整理（担当：提案側）
- 次回打ち合わせでの詳細説明準備（担当：提案側）
```

## 🔄 アップデート履歴

### v2.0.0 - Google Slides 対応
- PowerPoint から Google Slides に変更
- OAuth 2.0 認証の実装
- リアルタイムスライド作成
- ブラウザでの直接編集が可能

### v1.0.0 - 初期版
- PowerPoint ファイル生成
- 基本的な議事録解析機能