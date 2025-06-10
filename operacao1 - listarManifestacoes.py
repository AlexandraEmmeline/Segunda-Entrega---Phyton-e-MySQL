# OPERAÇÃO 2 - LISTAR MANIFESTAÇÕES
from operacoesbd import *

conexao = criarConexao("127.0.0.1", "root", "1234567", "bd_sistema_ouvidoria")

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

encerrarConexao(conexao)
