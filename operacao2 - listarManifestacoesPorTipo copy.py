# OPERAÇÃO 2 - LISTAR MANIFESTAÇÕES POR TIPO

from operacoesbd import *

conexao = criarConexao('127.0.0.1', 'root', '1234567', 'bd_sistema_ouvidoria')

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
         

encerrarConexao(conexao)