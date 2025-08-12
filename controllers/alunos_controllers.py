import json 
import os 

ALUNOS = "data/alunos.json"

def load_alunos():
    if os.path.exists(ALUNOS):
        with open(ALUNOS, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def select_todos_alunos():
    alunos = load_alunos()

    for aluno in alunos:
        return aluno
    
def select_aluno_por_email(email):
    alunos = load_alunos()

    for aluno in alunos:
        if alunos["email_alunos"] == email:
            return True 
    else:
        return False
    
def select_aluno_por_cpf(cpf):
    alunos =load_alunos()

    for aluno in alunos:
        if aluno["cpf_aluno"] == cpf:
            return True
    else:
        return False

def insert_aluno(data_aluno):
    alunos = load_alunos()

    if not isinstance(data_aluno, dict) or not data_aluno:
        return False
    
    alunos.append(data_aluno)

    with open(ALUNOS, "w", encoding="utf-8") as arq_json:
        json.dump(alunos, arq_json, indent=4, ensure_ascii= False)
    
    return True