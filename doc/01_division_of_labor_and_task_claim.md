---
title: 01_division_of_labor_and_task_claim
---

# Division of Labor and Task Claim

date: 2026/04/30 \
by WL, LIU \
Licensed under CC BY 4.0.

---

## 專案概述
本專案旨在探討當 LLM 應用（如多 Agent 協作）變得複雜時，如何透過 Observability 工具解決「黑盒子」除錯與成本監控的問題。 \
簡單來說，在有使用多個 Tools 的 LLM 或是 Muti-agent 的 LLM，這些工具可以幫助我們追蹤到底過程中使用了哪些 Tools 或是分別呼叫了哪些 Agents。 \
我們這次主要以 **LangSmith**、**Langfuse** 這兩個 Observability 工具作為 Demo 與比較。在 Demo 階段，前者用於解決單一 Agent、後者用於 Multi-Agent。


*   **報告日期：** 5/7 (請於 5/5 前完成各自負責的簡報頁面)
*   **GitHub Repo：** [連結](https://github.com/Rlonglong/LLM-observability-tools-integration.git)
*   **Kanban 任務看板：** [連結](https://github.com/users/Rlonglong/projects/2)
*   **簡報共編連結：** [連結](https://canva.link/k1fb7eybaxeki7q) (目前僅為 AI 生成模板，若有需要可以自行增加或調整頁數、內容)

> 程式碼的部分，基於 **LangSmith**、**Langfuse** 這兩個我都有分別先寫好一份範例程式碼，照著跑應該就可以跑起來，你們可以根據這個作為基礎先跑起來，然後在看什麼需要修改即可。


## 專案分工與任務分配表 (共 8 人)
以下分工請在 5/2 前完成，應該是都蠻簡單的。如果想做的工作已經填滿，可以先填在後面。等大家都填完，我們可以在 Discord 再一起協調一下。

> 填入方式：將連結中 `github.png` 改成 `[你的 github user name].png`、`https://github.com/github` 改成 `https://github.com/[你的 github user name]`。若不能理解可以參考 [我寫的方式](#1-系統架構與專案管理-1人)。

### 1. 系統架構與專案管理 PM (1人)
*   **負責人：** 
<a href="https://github.com/Rlonglong">
  <img src="https://images.weserv.nl/?url=github.com/Rlonglong.png&mask=circle" width="24" height="24" style="vertical-align: middle;">
  <strong>劉韋良</strong>
</a>
*   **任務重點 (佔評分 15% 小組分工)：** 
    *   建立 GitHub Repo
    *   規劃 Kanban 與分支保護規則
    *   提供核心 Demo 程式碼骨架（包含 LangSmith 單一 Agent 與 Langfuse 多 Agent 雙版本範例）
    *   審核所有 PR (Pull Request)。

### 2. 核心概念與研究組 (2人)
*   **負責人：** 
<a href="https://github.com/github">
  <img src="https://images.weserv.nl/?url=github.com/github.png&mask=circle" width="24" height="24" style="vertical-align: middle;">
  <strong>研究一</strong>
</a>、
<a href="https://github.com/github">
  <img src="https://images.weserv.nl/?url=github.com/github.png&mask=circle" width="24" height="24" style="vertical-align: middle;">
  <strong>研究二</strong>
</a>
*   **任務重點 (佔評分 35%)：**
    *   以通俗易懂的方式解釋什麼是 LLM Observability (Tracing, Metrics, Evaluation)。
    *   收集 2-3 句 AI 領域知名大牛（如 Andrew Ng, Andrej Karpathy 等）或是相關文章對於「LLM Debug 困難點」或「黑盒子現象」的名言金句，用於心得分享作為客觀、有依據的觀點分析。
    *   簡單比較本次展示的兩款工具（LangSmith 著重生態系與除錯 vs Langfuse 著重儀表板與成本監控）。

### 3. Demo 實作與展示組 (2人)
*   **負責人：** 
<a href="https://github.com/github">
  <img src="https://images.weserv.nl/?url=github.com/github.png&mask=circle" width="24" height="24" style="vertical-align: middle;">
  <strong>DEMO A</strong>
</a>、
<a href="https://github.com/github">
  <img src="https://images.weserv.nl/?url=github.com/github.png&mask=circle" width="24" height="24" style="vertical-align: middle;">
  <strong>DEMO B</strong>
</a>
*   **任務重點 (佔評分 20% 現場展示)：**
    *   **Demo A 組 (LangSmith)：** 負責跑通單一 Agent 程式碼，加入簡單 UI。展示程式碼出錯時，如何從 LangSmith 後台瞬間找出是哪一個 Tool 壞掉。
    *   **Demo B 組 (Langfuse)：** 負責跑通 Multi-Agent 程式碼，加入簡單 UI。展示多代理運作時，如何透過 Langfuse 後台圖表抓出消耗了異常大量 Token 的「成本怪獸」。
    *   *(強制規範)* 修改程式碼必須開新 Branch，並透過發起 PR (`Closes #Issue編號`) 來繳交進度。
    *   可錄製一段順暢執行的螢幕錄影作為現場備案。報告時親自說明操作流程。

### 4. 實務心得與未來展望組 (3人)
*   **負責人：** 
<a href="https://github.com/github">
  <img src="https://images.weserv.nl/?url=github.com/github.png&mask=circle" width="24" height="24" style="vertical-align: middle;">
  <strong>心得一</strong>
</a>、
<a href="https://github.com/github">
  <img src="https://images.weserv.nl/?url=github.com/github.png&mask=circle" width="24" height="24" style="vertical-align: middle;">
  <strong>心得二</strong>
</a>、
<a href="https://github.com/github">
  <img src="https://images.weserv.nl/?url=github.com/github.png&mask=circle" width="24" height="24" style="vertical-align: middle;">
  <strong>心得三</strong>
</a>
*   **任務重點 (佔評分 30% 核心關鍵)：**
    *   **實務痛點對比：** 訪談 Demo 組或親自試用，整理出一張對比圖表（例如：傳統 print debug vs 現代 Trace Tree 的具體差異）。
    *   **未來應用：** 探討這套系統未來如果套用到自己的專題，或是企業內部開發，能減少多少溝通成本與開發障礙。
    *   統整全組的簡報頁面，確保上下邏輯連貫、排版風格一致，並控制在 25 分鐘的報告時間內。


## 進度時程 (Timeline)
*   **5/2 (六) 前：** 所有人選好負責的部分，PM 會 assign 每個人對應的 Issue。分配完畢之後，所有人可以在 Kanban 上把自己的卡片移到 `In Progress` 開始動工。
*   **5/4 (一) 前：** 研究組與心得組把內容填入簡報；Demo 組確認程式能順利執行，將程式碼上傳到 GitHub 並完成 PR 發起。
*   **5/5 (二) 晚上：** 線上 Sync，順一次簡報流程與 Demo 測試(暫定，時間可以再討論），或是大家都對自己的部分很有自信就不用了(Ｘ)。
*   **5/7 (四)：** 上台報告！

---
## 相關連結
1. [Project Requirement](https://hackmd.io/@R-long/HJLMOgbAbx)
2. [Division of Labor and Task Claim](https://hackmd.io/@R-long/B1jJ_3-AWl)
3. [LLM Observability Tools Introduction](Issue #2 連結放這)
4. [LLM Observability Tools Reference](Issue #3 連結放這)
5. [LLM Observability Tools Development](Issue #8 連結放這)