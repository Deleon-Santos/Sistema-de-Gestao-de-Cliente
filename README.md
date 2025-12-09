![imagen de cadastro de pessoas](/src/Captura%20de%20tela%20de%202025-12-08%2023-42-51.png)
## Documentação do Sistema de Gestão de Pessoas .

### Introdução

Este documento tem como objetivo fornecer uma visão geral do sistema de gestão de pessoas, detalhando suas funcionalidades, arquitetura e tecnologias utilizadas.

### Funcionalidades

* **Cadastro de clientes:**
    * Campos obrigatórios e opcionais.
    * Salvamento das informações no banco de dados.

* **Consulta de clientes:** 
    * Exibição dos resultados em uma Planilha Excel.

* **Personalização da interface:**
    * Opções de temas (claro, escuro, sistema).
    * Mecanismo de troca de temas.

### Arquitetura da Aplicação* **Interface Gráfica:** Desenvolvida utilizando a biblioteca CustomTkinter, que oferece uma interface moderna e personalizável.
* **Lógica de Negócio:** Responsável por tratar as interações do usuário e as operações com o banco de dados.
* **Banco de Dados:** Armazena as informações dos clientes. Atualmente, o sistema utiliza um banco de dados SQLite.

### Banco de Dados

A tabela de clientes possui os seguintes campos:

* **id:** Chave primária, autoincremental.
* **nome:** Nome completo do cliente.
* **telefone:** Número de telefone.
* **email:** Endereço de email.
* **endereco:** Endereço completo.

O módulo `bd_gestao` é responsável por:

* **Criar a tabela de clientes:** Caso a tabela não exista, ela é criada com os campos definidos.
* **Inserir novos registros:** Os dados coletados na interface são inseridos na tabela de clientes.
* **Consultar registros:** Permite realizar consultas personalizadas na tabela, como buscar clientes por nome ou por data de cadastro.
* **Atualizar registros:** Permite modificar as informações de um cliente já cadastrado.

### Tecnologias Utilizadas

* **Python:** Linguagem de programação utilizada para desenvolver o sistema.
* **CustomTkinter:** Biblioteca Python para criar interfaces gráficas modernas e personalizáveis.
* **SQLite:** Sistema de gerenciamento de banco de dados leve e integrado ao Python.
* **Openpyxl:** Biblioteca Python para manipular planilhas Excel.
* **Pandas:** Gestão em planilhas.
Este documento apresenta uma visão geral do sistema de gestão de pessoas. Para um aprofundamento maior, recomenda-se a análise do código fonte e da documentação das bibliotecas utilizadas.

**Próximas etapas:**

* **Implementação da função de exclusão de clientes.**
* **Inclusão de relatórios mais detalhados.**
* **Integração com outros sistemas.**

**Observações:**

* A imagem da arquitetura do sistema pode ser substituída por um diagrama mais detalhado, utilizando ferramentas como UML.
* A imagem da estrutura da tabela pode ser gerada a partir do banco de dados utilizando ferramentas como SQLite Studio.
* As imagens dos logos das tecnologias podem ser encontradas facilmente na internet.

**Possíveis seções adicionais:**

* **Fluxograma:** Um diagrama que mostra o fluxo de dados e as interações entre os diferentes componentes do sistema.
* **Testes:** Descrição dos testes realizados para garantir a qualidade do software.
* **Guia do usuário:** Um manual para auxiliar os usuários a utilizar o sistema.
