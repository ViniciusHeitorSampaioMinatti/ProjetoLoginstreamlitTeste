import re 

def validar_email(email):
    email_padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA=Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_padrao, email) is not None