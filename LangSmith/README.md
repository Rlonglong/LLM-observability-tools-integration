# LangSmith: Single-Agent Debugging & Tracing PoC

## Overview
在開發 LLM Agent 時，傳統的終端機日誌 (Console Logs) 通常難以呈現 Agent 呼叫外部工具 (Tools) 時的內部邏輯斷層與錯誤細節。

本目錄提供一個基於 LangGraph 與 Gemini 模型構建的單一 Agent 概念驗證 (PoC)。我們在工具函式中刻意植入了一個隱蔽的型別錯誤 (`TypeError`)，藉此展示如何透過 LangSmith 的 Trace 樹狀圖，在毫秒間精準定位出發生異常的節點與程式碼行數。

## Prerequisites
1. 確保已安裝根目錄 `requirements.txt` 中的相依套件。
2. 註冊 [LangSmith 帳號](https://smith.langchain.com/)，並在 Settings -> API Keys 中生成專屬金鑰。
3. 申請 [Google AI Studio](https://aistudio.google.com/api-keys) API Key。
4. 在專案根目錄配置好 `.env` 檔案（請參考 `.env.example`）：
```ini
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="your_langsmith_api_key_here"
LANGCHAIN_PROJECT="Class_Demo_LangSmith"
GOOGLE_API_KEY="your_gemini_api_key_here"
```

## Quick Start
在終端機中執行以下指令以啟動 Agent 測試腳本：
```bash
python demo_langsmith_agent.py
```

## Observability Value

### 1. Terminal Output
執行腳本後，系統會嘗試查詢天氣並進行華氏溫度轉換。如預期，系統會拋出 `TypeError` 導致 Agent 崩潰。對於開發者而言，單看終端機難以立刻得知是哪一個 Tool 傳入了錯誤型別的變數。

### 2. LangSmith Dashboard
請前往 LangSmith 後台，進入設定的專案 (`Class_Demo_LangSmith`)：
* **Error Highlighting:** 你會看到一筆標記為 `Error` 的 Trace 紀錄。
* **Trace Tree 解析:** 點開樹狀圖，可以清晰看見 Agent 的決策流程：
  1. `LLM Node`: 判斷需呼叫天氣工具 (✅ 成功)
  2. `Tool Node`: 取得氣溫 25 度 (✅ 成功)
  3. `LLM Node`: 判斷需呼叫換算工具 (✅ 成功)
  4. `Tool Node`: `celsius_to_fahrenheit` 發生錯誤 (❌ 失敗，亮紅燈)
* **Root Cause Analysis:** 點擊紅燈節點，LangSmith 會直接顯示函式內部的 Input/Output 狀態，協助開發者瞬間抓出是內部字串 (`"1.8"`) 所導致的型別衝突，大幅縮短 Debug 時間。