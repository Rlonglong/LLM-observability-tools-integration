# LLM Observability 核心概念解析與工具比較

> 本文件當參考。主要以ppt為主。

---

## 1. LLM Observability 是什麼?

簡單來說:

> **LLM Observability = 看見 LLM 應用內部運作的工具與方法。**

它會即時收集 LLM 應用執行時的各種資料,
讓開發者能監控應用的行為、效能與回答品質。

> **註**:業界專家對 LLM 黑盒子問題的觀察與證言,
> 詳見 Issue #3 的整理。

## 2. 為什麼這件事很重要?(概要)

傳統軟體只要讀程式碼,就能大致知道它在做什麼。
但 LLM 不一樣 —— 你給它輸入,它給你輸出,**中間發生了什麼幾乎完全看不見**。

| 傳統軟體 | LLM 應用 |
|---------|---------|
| 同樣輸入 → 同樣輸出 | 同樣輸入 → **不一定同樣輸出** |
| 出錯會明確跳錯誤訊息 | **看似正常運作,卻悄悄答錯** |

> 💡 一句話:**「程式沒當機」不代表「答對了」**。

LLM Observability 工具的存在,就是為了解決 LLM「黑盒子」性質帶來的問題。
**具體的痛點情境與業界專家證言,請參閱 Issue #3 的整理。**

---

## 3. LLM Observability 的核心組成

LLM Observability 主要由三大核心功能構成 [1][2]:

### 3.1 Tracing (追蹤)

**完整記錄一次請求在 LLM 應用內部「走了哪些步驟」**,
並以結構化的方式呈現,讓原本看不見的內部流程變得可視化。

#### Tracing 會記錄的內容

- **Trace**:一次完整請求的紀錄 (從輸入到最終輸出)
- **Span**:Trace 中的單一執行步驟 (例如一次 LLM 呼叫、一次 Tool 使用)
- **整個 Agent 的決策流程**:Multi-Agent 之間的協作順序與交互

> 🩻 **比喻**:像 X 光片一樣,把原本看不見的內部結構顯示出來。

➡️ **本專案 Demo A** 將以 LangSmith 的 Trace 視覺化展示此功能。

---

### 3.2 Metrics (指標)

對 LLM 應用的運行狀態進行**量化統計**,協助快速發現異常並進行調校。

#### 主要指標

| 指標 | 說明 | 例 |
|------|------|---|
| **Latency** | 從輸入到輸出花費的時間 | 回應時間 (秒) |
| **Throughput** | 一段時間內處理的請求數 | 每分鐘請求數 |
| **Token Usage** | 每次請求消耗的 Token 數 | 直接影響成本 |
| **Error Rate** | 失敗回應的比例 | 衡量整體可靠性 |

> 📊 **比喻**:像健康檢查的數值報告 —— 一眼看出哪個指數異常。

➡️ **本專案 Demo B** 將以 Langfuse 儀表板展示此功能。

---

### 3.3 Evaluation (評估)

LLM 輸出的「好壞」**無法只用『跑得起來』來判斷**,需要更細緻的品質評估。

#### 評估的主要面向

| 面向 | 說明 | 例 |
|------|------|---|
| **Hallucination Rate** | 編造不正確內容的頻率 | 事實檢查 |
| **相關度** | 回答和問題的相關程度 | 問非所答的偵測 |
| **有害性** | 是否產生不當內容 | 安全性檢查 |
| **語調** | 是否符合應用預期的口吻 | 客服語氣的一致性 |

#### 評估方法

- **人工評分**:由人手動標註與評分 (最準但最慢)
- **LLM-as-a-Judge**:用另一個 LLM 來評分 (快但會有 Bias)
- **程式化檢查**:格式檢查、引用是否正確等 (規則明確時最有效)

> 🩺 **比喻**:像醫生看完檢查數據後做出的「診斷」。
> 數值正常不代表健康,還需要專業判斷。

---

## 4. 工具比較:LangSmith vs Langfuse

了解核心概念後,接下來看本專案使用的兩款代表性工具。
兩者皆覆蓋上述三大核心功能,差異主要在 **定位、授權、與生態系**:

| 比較項目 | LangSmith | Langfuse |
|---------|-----------|----------|
| 開發者 | LangChain 官方 | 開源社群 (MIT) |
| 授權方式 | 商用 SaaS (閉源) | 開源,可完全自託管 |
| 框架整合 | LangChain / LangGraph **原生支援** | **框架中立** (OpenAI SDK、LlamaIndex 等) |
| 主要強項 | 開發階段除錯、Trace 視覺化 | 成本分析儀表板、生產環境監控 |
| 部署方式 | 雲端為主,自託管需 Enterprise | 雲端 / Docker 自託管皆可 |
| 計價方式 | Seat + Trace 數 | Observation 數,**無 Seat 費** |
| 資料主權 | 資料存於 LangChain 雲端 | 自託管時資料完全在自己手上 |
| 適用情境 | 已使用 LangChain 生態系的團隊 | 需資料主權、多框架、成本敏感 |

(資料來源:[3][4][5])

### 一句話總結

- **LangSmith**:LangChain 官方原生工具,**開發階段體驗最佳**。
- **Langfuse**:開源框架中立工具,**上線運維彈性最高**。

---

## 5. 小結與本專案 Demo 對應

| 階段 | 推薦工具 | 對應核心功能 | 本專案 Demo |
|------|---------|------------|------------|
| 開發 / Debug | **LangSmith** | Tracing | Demo A:單一 Agent 除錯 |
| 上線 / 監控 | **Langfuse** | Metrics | Demo B:Multi-Agent 成本監控 |

兩款工具並非互斥 —— 業界實務上常見「**開發用 LangSmith,上線用 Langfuse**」的搭配,
本專案 Demo 也依此分工展示。

---

## 參考資料

[1] Elastic — *What is LLM Observability?*: https://www.elastic.co/what-is/llm-observability

[2] LangChain Blog — *Why LLM observability and monitoring needs evaluations*: https://www.langchain.com/articles/llm-monitoring-observability

[3] Langfuse Docs — *Langfuse vs LangSmith*: https://langfuse.com/faq/all/langsmith-alternative

[4] TECHSY — *Langfuse vs LangSmith: An Independent Verdict (2026)*: https://techsy.io/en/blog/langfuse-vs-langsmith

[5] LangSmith Official — *Observability Platform*: https://www.langchain.com/langsmith/observability