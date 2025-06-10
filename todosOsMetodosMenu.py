from operacoesbd import *


def listarManifestacoes(conexao):
    # Consulta todas as manifestações
    sql = "SELECT * FROM Manifestacoes"
    manifestacoes = listarBancoDados(conexao, sql)

    # Verifica se não há nenhuma manifestação
    if len(manifestacoes) == 0: 
        print("Nenhuma manifestação cadastrada!")

    # Exibe as informações de cada linha retornada
    else:
        print("\n--- MANIFESTAÇÕES ---")
        for item in manifestacoes:
            print("\n-------------------------",
                "\nCódigo:", item[0],         # CÓDIGO
                "\n", item[4], ",", item[3],  # TIPO E AUTOR
                "\n-", item[1],               # TÍTULO
                "\n-", item[2])               # DESCRIÇÃO            



def listarManifestacoesPorTipo(conexao):
    # Exibe opções de tipo e recebe a escolha do usuário
    tipoManifestacao = int(input("\n1. Elogio \n2. Sugestão \n3. Reclamaçao \nEscolha um tipo de manifestação acima para listar: "))

    # Mapeia o número digitado para o texto do tipo correspondente
    if tipoManifestacao == 1:
        tipo = "Elogio"

    elif tipoManifestacao == 2:
        tipo = "Sugestão"

    elif tipoManifestacao == 3:
        tipo = "Reclamação"

    # Caso o número digitado for diferente de 1, 2 ou 3
    else:
        print("Opção inválida! Escolha uma das opções de 1 a 3.")


    # Se a opção for válida, realiza a consulta filtrada
    if tipoManifestacao in (1, 2, 3):
        sql = "SELECT * FROM Manifestacoes WHERE Tipo = %s"
        params = (tipo,)
        manifestacoes = listarBancoDados(conexao, sql, params)


        if len(manifestacoes) == 0:
            print("Nenhuma manifestação cadastrada!")

        else:
            print("\n--- MANIFESTAÇÕES ---")
            for item in manifestacoes:
                print("\n-------------------------",
                    "\n", item[4], ",", item[3],  # TIPO E AUTOR
                    "\n-", item[1],               # TÍTULO
                    "\n-", item[2])               # DESCRIÇÃO



def criarNovaManifestacao(conexao):
    # Pergunta ao usuário o tipo da manifestação que deseja criar
    tipoManifestacao = int(input("\n1. Elogio \n2. Sugestão \n3. Reclamaçao \nEscolha um tipo de manifestação acima para adicionar: "))

    #A variável "tipo" será alimentada de acordo com base na opção escolhida acima
    if tipoManifestacao == 1:
        tipo = "Elogio"

    elif tipoManifestacao == 2:
        tipo = "Sugestão"

    elif tipoManifestacao == 3:
        tipo = "Reclamação"

    #Caso a opção seja diferente ded 1, 2 ou 3
    else:
        print("Opção inválida! Escolha uma das opções de 1 a 3.")

    # Só continua se o tipo escolhido for válido (estiver dentro do conjunto 1, 2 ou 3)
    if tipoManifestacao in (1, 2, 3):
        autor = input("Digite seu nome: ")
        titulo = input("Digite o título da sua manifestação: ")
        descricao = input("Digite sua manifestação: ")

    # Insere os dados no banco
        sql = "INSERT INTO Manifestacoes (Titulo, Descricao, Autor, Tipo) VALUES (%s, %s, %s, %s)"
        dados = (titulo, descricao, autor, tipo)
        manifestacoes = insertNoBancoDados(conexao, sql, dados)

        print("\nSua manifestação foi adicionada com sucesso!")



def exibirQuantidade(conexao):
    # Conta o total de registros na tabela
    sql = "SELECT COUNT(*) FROM Manifestacoes"
    manifestacoes = listarBancoDados(conexao, sql, params=None)

    # Exibe o total de manifestações cadastradas
    if len(manifestacoes) == 0:
        print("\nNenhuma manifestação cadastrada!")

    else:
        print("\nTotal de manifestações cadastradas:", manifestacoes[0][0])



def pesquisarPorCodigo(conexao):
    # Verifica se há manifestações cadastradas
    sql = "SELECT * FROM Manifestacoes"    
    manifestacoes = listarBancoDados(conexao, sql, params=None)

    if len(manifestacoes) == 0:
        print("Nenhuma manifestação cadastrada!")


    # Solicita o código a ser pesquisado
    else:
        codigo = int(input("\nDigite o código da manifestação que deseja pesquisar: "))
        sql = "SELECT * FROM Manifestacoes WHERE Codigo = %s"
        params = (codigo,)
        manifestacoes = listarBancoDados(conexao, sql, params)

    # Se não encontrar, avisa o usuário:
        if not manifestacoes:
            print("Não existe manifestação para esse código!")

    # Se encontrar, exibe:
        else:
            print("\nA manifestação pesquisada foi:")
            for item in manifestacoes:
                print("\n", item[4], ",", item[3],   # TIPO E AUTOR
                    "\n-", item[1],                  # TÍTULO
                    "\n-", item[2])                  # DESCRIÇÃO



def excluirPeloCodigo(conexao):
    # Solicita o código a ser deletado
    codigoDeletar = int(input("\nDigite o código da manifestação que deseja deletar: "))

    # Executa a exclusão
    sql = "DELETE FROM Manifestacoes WHERE Codigo = %s"
    dados = (codigoDeletar,)
    linhasAfetadas = excluirBancoDados(conexao, sql, dados) # Nome da váriavel "linhasAlteradas" apenas para facilitar a leitura

    # Informa o resultado ao usuário
    if linhasAfetadas > 0:
        print("\nManifestação deletada com sucesso!")
    else:
        print("\nNenhuma manifestação encontrada com esse código.")
