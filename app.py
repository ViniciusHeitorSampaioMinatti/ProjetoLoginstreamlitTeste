import streamlit as st
import time
from controllers.load_usuarios import load_usuarios
from components.cadastro import cadastrar_aluno
from components.show_alunos import show_alunos


st.set_page_config("sistema de cadastro", layout="wide")

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

        
        show_alunos()
    

    with tabs [2]:
        st.subheader("Logout")
        logout()
        
if st.session_state.email:
    main_page()
else:
    login()





