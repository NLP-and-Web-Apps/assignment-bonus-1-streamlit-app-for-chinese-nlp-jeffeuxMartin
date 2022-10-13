# 姓名：陳建成、學號：R09942097、Streamlit cloud: https://jeffeuxmartin-assignment-bonus-1-streamlit-app-fo-srcapp-sooxon.streamlitapp.com/

from snownlp import SnowNLP
import streamlit as st
import pandas as pd

st.title("簡易情感分析")

text = st.text_input('請輸入一段話：')

if text:
    result = {
        "text": [],
    "sentiment": [],
    "emoji": [],
    }
    doc_obj = SnowNLP(text)
    for sent in doc_obj.sentences:
        result['text'].append(sent)
        res_sent = SnowNLP(SnowNLP(sent).han)
        result['sentiment'].append(res_sent.sentiments)
        if res_sent.sentiments > 0.75:
            result['emoji'].append("😍🤬")
        elif res_sent.sentiments > 0.5:
            result['emoji'].append("😊😡")
        elif res_sent.sentiments > 0.25:
            result['emoji'].append("😌🤨")
        elif res_sent.sentiments > 0.:
            result['emoji'].append("😐😕")
        
    df = pd.DataFrame.from_dict(result)
    df = df.style.hide(axis="index")

    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # Display a static table
    st.table(df)
