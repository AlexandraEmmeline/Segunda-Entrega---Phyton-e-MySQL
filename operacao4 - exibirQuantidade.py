# OPERAÇÃO 4 - EXIBIR QUANTIDADE DE MANIFESTAÇÕES

from operacoesbd import *

conexao = criarConexao('127.0.0.1', 'root', '1234567', 'bd_sistema_ouvidoria')

# Conta o total de registros na tabela
sql = "SELECT COUNT(*) FROM Manifestacoes"
manifestacoes = listarBancoDados(conexao, sql, params=None)

# Exibe o total de manifestações cadastradas
if len(manifestacoes) == 0:
    print("\nNenhuma manifestação cadastrada!")

else:
    print("\nTotal de manifestações cadastradas:", manifestacoes[0][0])

encerrarConexao(conexao)
