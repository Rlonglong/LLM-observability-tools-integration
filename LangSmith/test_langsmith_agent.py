import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

# 載入上一層資料夾的 .env 環境變數
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

# ==========================================
# 1. 定義 Tools (刻意埋伏 Bug 準備 Demo)
# ==========================================
@tool
def get_weather(location: str) -> str:
    """取得指定地點的目前天氣與溫度（攝氏）。"""
    print(f"  [Tool 執行] 查詢 {location} 天氣中...")
    return f"{location}目前是晴天，氣溫 25 度。"

@tool
def celsius_to_fahrenheit(celsius: float) -> float:
    """將攝氏溫度轉換為華氏溫度。"""
    print(f"  [Tool 執行] 計算 {celsius} 轉華氏中...")
    
    #【Bug 埋伏區】
    # 刻意使用字串 "1.8" 引發 TypeError，讓 LangSmith 抓出來
    multiplier = "1.8" 
    return (celsius * multiplier) + 32 

# ==========================================
# 2. 初始化模型與 Agent
# ==========================================
tools = [get_weather, celsius_to_fahrenheit]
# 使用 Gemini 2.5 Flash
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
agent_executor = create_react_agent(llm, tools)

# ==========================================
# 3. 執行測試
# ==========================================
if __name__ == "__main__":
    print("🚀 LangSmith Demo: 啟動帶有 Bug 的單一 Agent...")
    user_input = "台北今天天氣如何？請幫我把當下的氣溫換算成華氏。"
    
    try:
        response = agent_executor.invoke({"messages": [("user", user_input)]})
        print("\n✅ 最終回答：", response["messages"][-1].content)
    except Exception as e:
        print("\n❌ 系統崩潰！(這是預期中的錯誤)")
        print(f"錯誤: {str(e)}")
        print("\n👉 現在請打開 LangSmith 後台，查看完整的 Trace Tree 抓出這個 Bug！")