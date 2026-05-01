import os
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langfuse.langchain import CallbackHandler

# 載入上一層資料夾的 .env 環境變數
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

# ==========================================
# 1. 設定 Langfuse Callback Handler
# ==========================================
langfuse_handler = CallbackHandler()

# ==========================================
# 2. 定義 Graph State
# ==========================================
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# ==========================================
# 3. 初始化 Gemini 模型與 Node 行為
# ==========================================
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

def researcher_agent(state: AgentState):
    """研究員：正常回答 (低消耗)"""
    print("  [Agent 1] Researcher 正在搜尋精準資料...")
    sys_msg = SystemMessage(content="你是一個精準的研究員，請用最簡短的一句話回答事實，不要廢話。")
    # 傳入 langfuse_handler 進行追蹤
    response = llm.invoke(
        [sys_msg] + state["messages"], 
        config={"callbacks": [langfuse_handler]}
    )
    return {"messages": [response]}

def writer_agent(state: AgentState):
    """寫手：Token 消耗怪物 (高消耗)"""
    print("  [Agent 2] Writer 正在瘋狂擴寫文章...")
    sys_msg = SystemMessage(
        content="你是一個極度囉唆的作家。請將收到的資訊擴寫成至少 500 字的長篇大論，加入大量無意義的修辭與廢話。"
    )
    info = state["messages"][-1].content
    user_msg = HumanMessage(content=f"請根據以下資訊進行擴寫：\n\n{info}")
    # 傳入 langfuse_handler 進行追蹤
    response = llm.invoke(
        [sys_msg, user_msg], 
        config={"callbacks": [langfuse_handler]}
    )
    return {"messages": [response]}

# ==========================================
# 4. 建立與編譯 LangGraph
# ==========================================
workflow = StateGraph(AgentState)
workflow.add_node("researcher", researcher_agent)
workflow.add_node("writer", writer_agent)

workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)

app = workflow.compile()

# ==========================================
# 5. 執行測試
# ==========================================
if __name__ == "__main__":
    print("🚀 Langfuse Demo: 啟動雙 Agent 成本監測...")
    user_input = "請告訴我地球上最高的山是什麼？"
    
    # 執行 Workflow 並透過 config 注入 langfuse 追蹤器
    final_state = app.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config={"callbacks": [langfuse_handler]}
    )
    
    print("\n✅ 最終回答 (會非常長！)：")
    print(final_state["messages"][-1].content)
    
    print("\n👉 請至 Langfuse 後台的 Traces 頁面，對比 researcher 與 writer 的 Token 消耗量差異！")
    
    # Langfuse 的 SDK 會在程式結束時自動上傳日誌，不需要手動 flush