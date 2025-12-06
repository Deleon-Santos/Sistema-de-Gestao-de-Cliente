import re
campos_nulos = []

def validar_nome(nome):
    if len(nome) > 10:
        return nome
    campos_nulos.append('nome')
    return False

def validar_idade(idade):
    try:
        idade=int(idade)
        if idade >0 and idade < 110:
            return idade
        
    except ValueError:
        campos_nulos.append('nome')
        return False
    
def validar_rua(rua):
    rua_valida = rua
    rua_valida == True if rua!=None else campos_nulos.append('rua')
    return rua_valida

    
def validar_genero(genero):
    try:
        if genero :
            return 
        campos_nulos.append('genero')
        return False
    except UnboundLocalError:
        campos_nulos.append('genero')
        return False
    
def validar_numero(numero):
    try:
        numero=int(numero)
        if numero is not None:
            return 
        campos_nulos.append('numero')
        return False
    
    except ValueError:
        print(numero)
        campos_nulos.append('numero')
        return False

def validar_cep(cep):
    cep = str(cep).replace('-','')
    if len(cep)==8:
        return 
    campos_nulos.append('cep')
    return False

def validar_email(email):
    email_valido = re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+$', email)
    if email_valido:
        return 
    campos_nulos.append('email')
    print(email,email_valido)
    return 
    
def validar_bairro(bairro):
    bairro == True if bairro != None else campos_nulos.append('bairro') 
    return bairro

def validar_cidade(cidade):
    if cidade != None:
       return 
    campos_nulos.append('cidade')
    return 

def validar_uf(uf):
    if uf != None:
        return True
    campos_nulos.append('uf')
    return False

def validar_tel(tel):
    tel_valido = re.search(r'^[0-9]{11}$',tel)
    if tel_valido:
        
        return
    campos_nulos.append('tel')
    print(tel)
    return False

def validacao(nome,idade,tel,genero,rua,numero,cep,email,bairro,cidade,uf):
    validar_nome(nome)
    validar_idade(idade)
    validar_genero(genero)
    validar_rua(rua)
    validar_numero(numero)
    validar_cep(cep)
    validar_email(email)
    validar_bairro(bairro)
    validar_cidade(cidade)
    validar_uf(uf)
    validar_tel(tel)
    
#validacao('Daniel Souza Santos',13, '1112345679','masculino', 'rua silva sales','2234', '12345-678', 'castor@gmail.com', 'saldade', ' sao franciasco','sp')
    if not campos_nulos:
        return True
    else:
        return f"Campos nao validades: {', '.join(campos_nulos)}"
