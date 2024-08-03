#Importação de bibliotecas

import openai
import streamlit as st
import streamlit_chat
import os
from streamlit_chat import message as msg 


openai.api_key = "$ENV:SENHA_OPEN_AI = "API_KEY"


st.title('Harmoniza')
st.write("***")

if "hst_conversa" not in st.session_state:
    st.session_state.hst_conversa = []

 # Adiciona a parte específica à pergunta
 
pergunta = st.text_input("Digite o prato que deseja harmonizar:")
pergunta_harmonizacao = "Que bebida harmoniza " + pergunta + "?" 
btn_enviar = st.button("Enviar pergunta")

if btn_enviar:
    st.session_state.hst_conversa.append({"role": "user", "content": pergunta_harmonizacao})
   
    retorno_openai = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = st.session_state.hst_conversa,
        max_tokens = 1000,
        n=1
    )

    #st.write(retorno_openai)
    st.session_state.hst_conversa.append({"role":"assistant",
                                              "content": retorno_openai['choices'][0]['message']["content"]})

if len(st.session_state.hst_conversa) > 0:
    
    for i in range(len(st.session_state.hst_conversa)):
        if i % 2 == 0:
                msg("Você: " + st.session_state.hst_conversa[i]["content"], is_user=True)
        else:
                msg("Resposta IA: " + st.session_state.hst_conversa[i]["content"])

