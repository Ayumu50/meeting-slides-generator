# 議事録スライド自動作成エージェント

営業の打ち合わせ議事録を入力すると、Azure OpenAI を使用して自動でPowerPointスライドを生成するWebアプリケーションです。

## 🚀 機能

- **議事録の自動解析**: Azure OpenAI (o4-mini) を使用して議事録を構造化
- **PowerPoint自動生成**: 解析結果から美しいスライドを自動作成
- **BANT情報抽出**: 営業に重要な予算・決裁・ニーズ・時期を自動抽出
- **成功画面への遷移**: 生成完了後に詳細情報を表示
- **自動ダウンロード**: 生成されたファイルの自動ダウンロード機能

## 📊 生成されるスライド内容

1. **タイトルスライド** - 会社名・日付入り
2. **アジェンダ** - 議事録から抽出した議題
3. **セクション別詳細** - 内容に応じて自動分割
4. **BANT情報** - 予算・決裁・ニーズ・時期
5. **課題とニーズ** - 明確化された課題と潜在ニーズ
6. **ネクストアクション** - 次のステップ
7. **まとめ** - 総括スライド

## 🛠️ 技術スタック

- **Backend**: Flask (Python)
- **AI**: Azure OpenAI (o4-mini)
- **PowerPoint生成**: python-pptx
- **Frontend**: HTML/CSS/JavaScript
- **デプロイ**: Render対応

## 📋 必要な環境変数

```bash
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=o4-mini
AZURE_OPENAI_API_VERSION=2024-12-01-preview
SECRET_KEY=your-secret-key-here
```

## 🚀 ローカル実行

1. リポジトリをクローン
```bash
git clone https://github.com/Ayumu50/meeting-slides-generator.git
cd meeting-slides-generator
```

2. 仮想環境を作成・有効化
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate  # Windows
```

3. 依存関係をインストール
```bash
pip install -r requirements.txt
```

4. 環境変数を設定
```bash
cp .env.example .env
# .envファイルを編集してAzure OpenAIの設定を入力
```

5. アプリケーションを起動
```bash
python app.py
```

6. ブラウザで http://localhost:5001 にアクセス

## 🌐 デプロイ

### Render でのデプロイ

1. Renderアカウントを作成
2. GitHubリポジトリを接続
3. 環境変数を設定
4. 自動デプロイが開始されます

### 必要な設定ファイル

- `requirements.txt` - Python依存関係
- `Procfile` - Renderでの起動コマンド
- `render.yaml` - Render設定ファイル
- `runtime.txt` - Pythonバージョン指定

## 📝 使用方法

1. Webアプリケーションにアクセス
2. 議事録テキストを入力欄に貼り付け
3. 「PowerPoint スライド作成」ボタンをクリック
4. 生成完了画面でファイルをダウンロード

### 議事録の例

```
# トレノケート株式会社様

## 概要・目的
- 日時：2025年7月9日（水）
- 実施方法：オンライン（Microsoft Teams）
- 目的：AI・データ活用による人材育成・業務効率化のご提案

## 明確な課題・潜在的ニーズ
- 既存研修データの有効活用
- AIによる業務効率化の推進
- PoC（概念実証）を限定的な範囲で実施したい

## 合意したネクストアクション
- 具体的な提案内容の整理（担当：提案側）
- 次回打ち合わせでの詳細説明準備（担当：提案側）
```

## 🎨 デザインポリシー

- **ワンスライド・ワンメッセージ**: 各スライドに1つの明確なメッセージ
- **視線を意識**: 重要な要素を上部に配置
- **色の役割**: 背景・文字・メイン・アクセントの明確な使い分け
- **左揃えの徹底**: 読みやすさを重視
- **箇条書きの制限**: 1スライドあたり最大6項目

## 🔧 カスタマイズ

### テンプレートの変更

`image/tempppt.pptx` ファイルを差し替えることで、スライドのデザインテンプレートを変更できます。

### 色設定の変更

`app.py` の以下の部分で色設定を変更できます：

```python
BACKGROUND_RGB = RGBColor(255, 255, 255)  # 背景色
PRIMARY_RGB = RGBColor(32, 89, 167)       # メインカラー
ACCENT_RGB = RGBColor(237, 242, 248)      # アクセントカラー
TEXT_RGB = RGBColor(25, 25, 25)           # テキスト色
```

## 📄 ライセンス

MIT License

## 🤝 コントリビューション

プルリクエストやイシューの報告を歓迎します。

## 📞 サポート

問題が発生した場合は、GitHubのIssuesページでお知らせください。