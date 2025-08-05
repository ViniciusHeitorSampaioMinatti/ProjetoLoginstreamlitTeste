import streamlit as st
import time
from controllers.load_usuarios import load_usuarios
from datetime import date
import re 
from utils.validar_email import validar_email


st.title("projeto Streamlit")

if "email" not in st.session_state:
    st.session_state.email = None

if "nome" not in st.session_state:
    st.session_state.nome = None

def login():
    usuarios = load_usuarios()
    email = st.text_input("Email", placeholder="Email")
    senha = st.text_input("Senha", placeholder="Senha", type="password")
    login = st.button("Login")
    
    if login:
        for user in usuarios:
            if user["email"] == email and user ["senha"] == senha:
                st.session_state.email = user ["email"]
                st.session_state.nome = user ["nome"]
                st.success("login efetuado com sucesso!")
                time.sleep(3)
                st.rerun()
            else:
                st.error("email ou senha inválidos, tente novamente!")

def logout():
    if st.button("Logout"):
        st.session_state.clear()
        st.success("Finalizando o sistema!")
        time.sleep(3)
        st.rerun()

@st.dialog("Formulários de cadastro de alunos", width=True)
def cadastrar_aluno():
    data_minima = date(1900, 1, 1)
    data_maxima = date.today()
    Nome_aluno = st.text_input("Nome do aluno", placeholder="Nome do aluno")      
    Email_aluno = st.text_input("Email do aluno", placeholder="Email do aluno")      
    CPF_aluno = st.text_input(
        "CPF do aluno",
        placeholder="CPF do aluno",
        max_chars=11
        )      
    DataNasc_aluno = st.date_input(
        "Data de nascimento do aluno",
        value=data_maxima,
        min_value=data_minima,
        
        )      
    Telefone_aluno = st.text_input(
        "Telefone do aluno",
        placeholder="Telefone do aluno",
        max_chars=11
        )
    
    cpf_aluno_numeros = re.sub(r"\D", "", CPF_aluno)
    Telefone_aluno_numeros = re.sub(r"\D","", Telefone_aluno)
    email_isvalid = validar_email(Email_aluno)


    btn_cadastrar = st.button("Cadastrar")
    if btn_cadastrar:
       st.write(email_isvalid)     

def  main_page():
    tabs = st.tabs(["dashboard", "cadastro", "logout"])
    nome = st.session_state.nome

    with tabs [0]:
        st.subheader("Dashboard")
        st.write(f"**Usuário logado:** {nome}")
    
    with tabs [1]:
        st.subheader("Cadastro")
        if st.button("Abrir Formulário de Cadastro"):
            cadastrar_aluno()
    
    with tabs [2]:
        st.subheader("Logout")
        logout()
        
if st.session_state.email:
    main_page()
else:
    login()





