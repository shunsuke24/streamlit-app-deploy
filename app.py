from dotenv import load_dotenv

load_dotenv()


import streamlit as st

st.title("サンプルアプリ②: 少し複雑なWebアプリ")

st.write("##### 動作モード1: 数学者")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでAIに質問できます。")

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


# human_message = HumanMessage(content="私の名前は良子です。")

# ai_message = AIMessage(content="こんにちは、太郎さん！")

# human_message2 = HumanMessage(content="私の名前が分かりますか？")

# messages = [human_message, ai_message, human_message2]

# ai_response = llm(messages)
# print(ai_response.content)

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