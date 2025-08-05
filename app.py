import streamlit as st
import time
from controllers.load_usuarios import load_usuarios


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

@st.dialog("Formulários de cadastro de alunos")
def cadastrar_aluno():
    Nome_aluno = st.text_input("Nome do aluno", placeholder="Nome do aluno")      
    Email_aluno = st.text_input("Email do aluno", placeholder="Email do aluno")      
    CPF_aluno = st.text_input("CPF do aluno", placeholder="CPF do aluno")      
    DataNasc_aluno = st.date_input("Data de nascimento do aluno")      
    Telefone_aluno = st.text_input("Telefone do aluno", placeholder="Telefone do aluno")
    btn_cadastrar = st.button("Cadastrar")      

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

# if "contador" not in st.session_state:
#     st.session_state.contador = 0
 
# if st.button("Adiciomar"):
#     st.session_state.contador += 1


# if st.button("Diminuir"):
#    if st.session_state.contador > 0:
#     st.session_state.contador -= 1


# st.write(st.session_state)

# # if not teste:
# #     st.warning("A variavel esta vazia. ")
# # else:
# #     st.info("A variavel tem informação. ")