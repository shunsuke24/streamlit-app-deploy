# from dotenv import load_dotenv
# load_dotenv()  # Streamlit Cloudでは環境変数を直接設定する方が良いです

import streamlit as st
import os

st.title("サンプルアプリ②: 少し複雑なWebアプリ")

st.write("##### 動作モード1: 数学者")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでAIに質問できます。")

# ここを修正
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# 以下は同じ
selected_item = st.radio(
    "動作モードを選択してください。",
    ["数学者", "科学者"]
)

st.divider()

if selected_item == "数学者":
    input_message = st.text_input(label="数学の問題を入力してください。")
    human_message = HumanMessage(content="あなたは数学者です。")
    ai_message = AIMessage(content=input_message)

else:
    input_message = st.text_input(label="科学の問題を入力してください。")
    human_message = HumanMessage(content="あなたは科学者です。")
    ai_message = AIMessage(content=input_message)

if st.button("実行"):
    st.divider()

    if selected_item == "数学者":
        if input_message:
            messages = [human_message, ai_message]
            ai_response = llm(messages)
            st.write(ai_response)

        else:
            st.error("文字を入力してください")

    else:
        if input_message:
            messages = [human_message, ai_message]
            ai_response = llm(messages)
            st.write(ai_response)

        else:
            st.error("文字を入力してください")