import os
import requests
from datetime import datetime
from typing import List, Dict, Any
from dotenv import load_dotenv
load_dotenv()
# --- 設定値（環境変数や設定ファイルで管理推奨） ---
NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# --- Notion API ヘルパー ---
def get_unprocessed_companies() -> List[Dict[str, Any]]:
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    payload = {
        "filter": {
            "property": "ステータス",
            "select": {"equals": "未処理"}
        }
    }
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json().get("results", [])

def update_notion_row(page_id: str, summary: str):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    now = datetime.now().isoformat()
    payload = {
        "properties": {
            "分析結果": {"rich_text": [{"text": {"content": summary}}]},
            "ステータス": {"select": {"name": "完了"}},
            "更新日時": {"date": {"start": now}}
        }
    }
    requests.patch(url, headers=headers, json=payload)

# --- Azure OpenAI ヘルパー ---
def summarize_policy(company: str, info: str) -> str:
    url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT}/chat/completions?api-version=2024-02-15-preview"
    headers = {
        "api-key": AZURE_OPENAI_KEY,
        "Content-Type": "application/json"
    }
    prompt = f"""
あなたは人材育成企業の営業支援のために企業情報を提供します。以下の情報をもとに、「人材育成」や「最新のプロダクト」に関して具体的に教えて下さい。また最新のプレスリリース、ニュースやIR情報の名前も箇条書きで出力してください。すべてで200文字以内で出力してください。
---
企業名: {company}
情報: {info}
"""
    data = {
        "messages": [
            {"role": "system", "content": "あなたは企業分析の専門家です。"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 256,
        "temperature": 0.2
    }
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()

# --- メイン処理 ---
def main():
    companies = get_unprocessed_companies()
    for row in companies:
        page_id = row["id"]
        props = row["properties"]
        company = props["企業名"]["title"][0]["plain_text"] if props["企業名"]["title"] else ""
        # TODO: 企業情報の収集（Bing Search APIやIR PDF等）
        info = f"{company}のIR情報やWeb情報（ここに自動収集結果を格納）"
        summary = summarize_policy(company, info)
        update_notion_row(page_id, summary)
        print(f"[完了] {company} の要約をNotionに記録しました")

if __name__ == "__main__":
    main()
