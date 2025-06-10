# OPERAÇÃO 5 - PESQUISAR PELO CODIGO

from operacoesbd import *

conexao = criarConexao('127.0.0.1', 'root', '1234567', 'bd_sistema_ouvidoria')

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


encerrarConexao(conexao)