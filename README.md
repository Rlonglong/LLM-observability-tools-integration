# LLM Observability Tools Integration

## Project Goal
**目的**：在開發與調試大型語言模型 (LLM) 時，解決傳統終端機日誌 (Console Logs) 所面臨的「資訊過載」與「追蹤斷層」問題。
**方法**：透過導入 LangSmith 與 Langfuse 兩大主流可觀察性平台，實現對多代理人 (Multi-Agent) 協作流程的視覺化追蹤、成本監控與除錯分析。



## Tech Stack

### Core Components
- **Framework**: [LangGraph](https://langchain.com/langgraph) - 構建有狀態、循環的 Agent 協作流程。
- **LLM Provider**: [Google Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs) - 提供高性價比的推理能力。
- **Environment**: Python 3.10+

### Observability Platforms
- **[LangSmith](https://smith.langchain.com/)**
  - *定位*：LangChain 官方的開發者平台。
  - *功能*：適合*開發階段*。提供詳細的 **Trace Tree**（追蹤樹）、錯誤快照 (Snapshots) 及串流除錯 (Streaming Debugging)。
- **[Langfuse](https://langfuse.com/)**
  - *定位*：開源的 LLM/AI 追蹤與品質監控平台。
  - *功能*：適合*上線階段*。側重於**成本分析** (Cost Analytics)、Token 使用量統計與生產環境的品質監控。



## Project Structure

### LangSmith Demo (Single-Agent)
- `LangSmith/test_langsmith_agent.py`:
  - **概念**：單一 Agent 執行流程。
  - **核心**：刻意植入 `TypeError` (型別錯誤)，展示 LangSmith 如何精準定位到錯誤發生的 Tool 節點。
- `LangSmith/README.md`:
  - 示範如何使用 LangSmith Trace Tree 視覺化分析 Agent 的決策邏輯與錯誤堆疊。

### Langfuse Demo (Multi-Agent)
- `Langfuse/test_langfuse_multi_agent.py`:
  - **概念**：雙 Agent 協作 (Research -> Writing)。
  - **核心**：利用 LangGraph 構建兩個行為迥異的 Agent，展示 Langfuse 在*成本監控*上的優勢。
- `Langfuse/README.md`:
  - 示範如何利用 Langfuse 比較兩個 Agent 的 Token 消耗量，用於優化模型選擇與 Prompt 設計。


## Getting Started

1. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

2. **環境設定**
   在專案根目錄建立 `.env` 檔案，填入您的 API Key：
   ```ini
   # Google Gemini
   GOOGLE_API_KEY="your_gemini_api_key"

   # LangSmith
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   LANGCHAIN_API_KEY="your_langsmith_api_key"
   LANGCHAIN_PROJECT="Class_Demo_LangSmith"

   # Langfuse
   LANGFUSE_SECRET_KEY="your_langfuse_secret_key"
   LANGFUSE_PUBLIC_KEY="your_langfuse_public_key"
   LANGFUSE_BASE_URL="https://us.cloud.langfuse.com"
   ```

3. **執行測試**
   - 執行 LangSmith Demo：
     ```bash
     python LangSmith/test_langsmith_agent.py
     ```
   - 執行 Langfuse Demo：
     ```bash
     python Langfuse/test_langfuse_multi_agent.py
     ```

4. **查看結果**
   - 執行程式後，依照終端機的指示，打開對應平台的 Web UI（提供連結）。
   - 比較兩個平台的界面，感受不同的可觀察性體驗。
