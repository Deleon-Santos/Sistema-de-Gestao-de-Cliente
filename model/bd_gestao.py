import sqlite3
from sqlite3 import connect
import src.Gestao_XLSX as gerar

#função para conectar oa  bd
def conexao_bd():
    try:
        conexao=connect('BD_Gestao')
        cursor= conexao.cursor()
        return conexao , cursor
    
    except sqlite3.Error:# Tratamento de erros em conexão
        print('Erro em conexao')
        return None, None


def salvar_dados(pessoa, conexao, cursor):
    cursor.execute("""insert into pessoa (nome,tel,idade,email,genero,cep,rua,numero,complemento,bairro,cidade,uf)
                   values(?,?,?,?,?,?,?,?,?,?,?,?)"""
                   ,pessoa)
    conexao.commit()
    return


def mostrar_dados(cursor):
    pessoas= []
    cursor.execute("""select * from pessoa""")
    pessoa = cursor.fetchall()
    for pessoa_salva in pessoa:
        pessoas.append(pessoa_salva)
        print(f'id :{pessoa_salva[0]}\nnome :{pessoa_salva[1]}\nidade :{pessoa_salva[2]}\ntelefone :{pessoa_salva[3]}\nemail :{pessoa_salva[4]}\ngenero :{pessoa_salva[5]}\ncep :{pessoa_salva[6]}\nrua :{pessoa_salva[7]}\nnumero :{pessoa_salva[8]}\ncomplemento :{pessoa_salva[9]}nbairro :{pessoa_salva[10]}\ncidade :{pessoa_salva[11]}\nuf :{pessoa_salva[12]}\n\n')
    
    return pessoas #retorna todas as pessoas do bd


def criar_tabela_gestao(pessoa):
    try:
        conexao, cursor = conexao_bd()
        if conexao:# se houver conexão 
            cursor.execute( """create table if not exists pessoa (
                        id integer primary key autoincrement,
                        nome text,
                        tel text,
                        idade integer,
                        email text,
                        genero text,
                        cep text,
                        rua text,
                        numero integer,
                        complemento text,
                        bairro text,
                        cidade text,
                        uf text)""")
            
            conexao.commit() #cria a tabela se não existir

            salvar_dados(pessoa,conexao,cursor)
            pessoas=mostrar_dados(cursor)
            gerar.gravar_xlsx([pessoas],"Tabela de Pessoas.xlsx")
            conexao.close()
            return 'Documento Salvo com Sucesso'
        return 'Falha na Conexao'
        
    except sqlite3.Error as e:
        return e 





    
    