# Langfuse: Multi-Agent Cost & Token Monitoring PoC

## Overview
隨著 AI 系統從單一模型演進至「多代理協作 (Multi-Agent)」架構，Token 消耗量與運算成本往往容易失控。若其中一個 Agent 陷入無窮迴圈或產生極度冗長的幻覺輸出，企業將面臨鉅額的 API 帳單。

本目錄提供一個雙 Agent 協作的概念驗證 (PoC)。系統中包含一個正常的 `Researcher` Agent 與一個被設定為高 Token 消耗的 `Writer` Agent。透過整合 Langfuse，我們將展示如何直觀地追蹤並隔離出系統中的「成本怪物」。

## Prerequisites
1. 確保已安裝根目錄 `requirements.txt` 中的相依套件。
2. 註冊 [Langfuse 帳號](https://cloud.langfuse.com/)，並建立一個新專案。
3. 前往專案的 Settings -> API Keys 生成金鑰
4. 申請 [Google AI Studio](https://aistudio.google.com/api-keys) API Key。
5. 並於專案根目錄配置好 `.env` 檔案：
```ini
LANGFUSE_SECRET_KEY="your_secret_key_here"
LANGFUSE_PUBLIC_KEY="your_public_key_here"
LANGFUSE_HOST="https://cloud.langfuse.com"
GOOGLE_API_KEY="your_gemini_api_key_here"
```

## Quick Start
在終端機中執行以下指令以啟動 Multi-Agent 測試腳本：
```bash
python demo_langfuse_multi_agent.py
```

## Observability Value

### Terminal Output
腳本執行後，`Researcher` 會先精準回覆簡短事實，隨後交棒給 `Writer` 進行擴寫。終端機最終會印出一篇極度冗長、充滿廢話的文章。在傳統日誌中，開發者僅能看到最終的長篇字串，無法量化個別環節的開銷。

### Langfuse Dashboard
腳本執行完畢後（確保 `langfuse_handler.flush()` 已執行），請前往 Langfuse 後台的 **Traces** 頁面：
* **Node-Level Metrics:** 展開最新一筆 Trace 的樹狀圖，你可以獨立檢視每個節點 (Node) 的效能指標。
* **Cost Comparison:** 
  * 點擊 `researcher` 節點：觀察其右側的 `Usage` (Token 消耗) 與 `Latency` (延遲)，數值應極低。
  * 點擊 `writer` 節點：對比其暴增的 Token 消耗量與執行時間。
* **Architectural Insight:** 透過這套視覺化指標，系統架構師能在上線前精準揪出並重構高耗能的 Agent (例如優化其 System Prompt 或更換較小的模型)，實現企業級的成本合規監控。