import streamlit as st 
import re 
from utils.validar_email import validar_email
from datetime import date 
from  controllers.alunos_controllers import select_aluno_por_cpf, select_aluno_por_email, insert_aluno, load_alunos
import time 

@st.dialog("Formulários de cadastro de alunos", width="large")
def cadastrar_aluno():
    data_minima = date(1900, 1, 1)
    data_maxima = date.today()
    
    with st.form("Formulário de cadastro"):
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
        result_email = select_aluno_por_email(Email_aluno)
        result_cpf = select_aluno_por_cpf(CPF_aluno)

        colunas = st.columns(2)

        with colunas[0]:
            btn_cadastrar = st.form_submit_button("Cadastrar", use_container_width=True)
        
        with colunas[1]:
            btn_cancelar = st.form_submit_button("Cancelar", use_container_width=True)


    if btn_cadastrar:
        if not Nome_aluno:
            return st.warning("campo nome não pode ser vazio!")

        if not Email_aluno:
            return st.warning("campo Email não pode see vazio!")
        
        if not email_isvalid:
            return st.warning("Cpf inválido!")

        if not CPF_aluno:
            return st.warning("Campo cpf não pode ser vazio!")

        if len(cpf_aluno_numeros) != 11 or len(cpf_aluno_numeros) <11:
            return st.warning("CPF inválidos")

        if not Telefone_aluno:
            return st.warning("Campo telefone não pode ser vazio!")

        if len(Telefone_aluno_numeros) != 11 or len(Telefone_aluno_numeros) <11:
            return st.warning("Telefone inválidos")
        
        if result_email:
            return st.warning("Email já esta cadastrado com outro aluno!")
        
        if result_cpf:
            return st.warning("CPF já esta cadastrado com outro aluno!")
        
        alunos = load_alunos()

        id_aluno = (alunos[-1]["id_aluno"] + 1) if alunos else 1
        
        data_aluno = {
            "id_aluno": id_aluno,
            "nome_aluno": Nome_aluno,
            "email_aluno": Email_aluno,
            "cpf_ aluno": cpf_aluno_numeros,
            "DataNasc_aluno": DataNasc_aluno.strftime("%Y-%m-%d"),
            "Telefone_aluno": Telefone_aluno_numeros

        }
        
        result_insert = insert_aluno(data_aluno)

        if not result_insert:
            st.error("Não foi possível reallizar o cadastro!")


        st.success("cadastro realizado com suecsso!")
        time.sleep(3)
        st.rerun()

    if btn_cancelar:
        st.rerun()    

