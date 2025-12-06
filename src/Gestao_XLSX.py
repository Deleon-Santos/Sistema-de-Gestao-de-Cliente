
import pandas as pd

def gravar_xlsx(pessoas, nome_arquivo="Tabela de Pessoas.xlsx", formatar=True):
    titulos = ['Id','Nome', 'Tel', 'Idade', 'Email', 'Genero','Cep', 'Rua', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'UF']
    try:
        for pessoa in pessoas:
            tabela = pd.DataFrame(pessoa, columns=titulos)

            with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
                tabela.to_excel(writer, index=False, sheet_name='Pessoas')

                # Formatação condicional (opcional)
                if formatar:
                    worksheet = writer.sheets['Pessoas']
                    worksheet.column_dimensions['C'].number_format = '0'  # Formatar coluna "Idade" como número inteiro

        print("Planilha salva com sucesso!")
    except (IOError, ValueError) as e:
        print(f"Erro ao salvar a planilha: {e}")




