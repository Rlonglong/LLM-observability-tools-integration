# 團隊開發與協作指南 (Git & Kanban)

為了在這次專題中拿下 **「小組分工 (佔比 15%)」** 的分數，我們將採用業界標準的軟體工程模式來推進專案。這不是一個很長生命週期的專案，我們不需要做到太過完美或完整，但一定要留下「我們有條理地分配工作、互相協作」的工程軌跡。

## 1. 我們的專案管理工具：Kanban (看板)
請先前往我們 GitHub Repo 上的 [**Projects**](https://github.com/users/Rlonglong/projects/2) 頁籤，你會看到一個分成四個欄位的看板：

*   **Todo (待辦)：** PM 分配好的所有任務卡片都在這。
*   **In Progress (進行中)：** 當你開始處理分配給你的任務時，**請把卡片拖曳到這一欄**。
*   **Review (統整/審閱)：** 你的簡報頁面寫完了，或是 Code 測完了，請拖到這裡讓 PM 或是其他組員進行確認。
*   **Done (完成)：** 確認沒問題，任務正式結案。在關閉 Issue 的同時，系統會自動把卡片移到 Done 欄位。

---

## 2. 如何確認與執行你的任務 (Issue)？

1. 選擇你的負責
1. **確認任務：**
   - PM 已經在 GitHub 上開好所有的 Issue，並在右側的 **Assignees** 標記了負責人。
   - 請登入你的 GitHub 帳號，找到標記你的 Issue，並將看板上的卡片拖曳至 `In Progress`，這代表你已經開始動工。

2. **執行任務與修改程式碼須知：**
   - 根據卡片內的 **Task List** 一項一項完成，並勾選 (`[x]`) 讓大家知道進度。
   - **重要提醒：** Repo 裡面提供的 Python 程式碼都**只是基礎範例**，非常鼓勵大家動手修改！例如：加上 Gradio/Streamlit UI 介面、修改 Prompt 或調整 Agent 邏輯。

---

## 3. 上傳進度與關閉 Issue

依照你的任務性質，請採取對應的繳交方式：

### 情況 A：你是「研究組」或「心得組」(負責寫簡報/查資料)
1. 你的產出通常是文件或簡報，不需要寫程式碼。
2. 請將你負責的內容直接寫在大家共用的 **簡報檔案** 或是 **HackMD** 中。
3. 完成後，回到 GitHub 你的 Issue 頁面，在下方留言貼上你的文件連結（例如：`簡報 P.x 內容已完成，HackMD 參考連結：...`）。
4. 將看板上的卡片拖曳到 **Review** 欄位等待 PM 確認。

### 情況 B：你是「Demo 組」(負責跑程式、改 Code 與錄影)
1. 在本機端 Clone 我們的 Repo：`git clone https://github.com/Rlonglong/LLM-observability-tools-integration.git`
2. **開新分支 (Branch)：** 要修改程式或加 UI，**絕對不要直接推上 main**！請先開一個新分支，例如：`git checkout -b feature/add-ui-langsmith`。*但是說直接推送到 `main` 已經被我鎖起來了，你們應該也不能直接推送到 `main`。*
3. 確保環境變數設定好，跑通腳本並完成你的修改。
4. 將更改的程式碼 Push 上你的新分支，並在 GitHub 頁面上發起 **Pull Request (PR)**。
5. **Close 魔法：** 在 PR 的敘述內容中，打上 `Closes #你的Issue編號`（例如 `Closes #4`）。當 PM 審核通過並 Merge 你的 PR 時，系統就會**自動幫你關閉那個 Issue**，並把卡片移到 Done！

---
**Notes:** 如果在設定環境、Git 操作或理解工具有任何卡關，**不要卡超過一個晚上**！請直接在 Discord 群組詢問，我們隨時 debug。