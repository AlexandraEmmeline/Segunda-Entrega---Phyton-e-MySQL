from operacoesbd import *

conexao = criarConexao('127.0.0.1', 'root', '1234567', 'bd_sistema_ouvidoria')

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

encerrarConexao(conexao)