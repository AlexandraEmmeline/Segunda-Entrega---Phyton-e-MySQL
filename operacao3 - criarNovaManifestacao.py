# OPERAÇÃO 3 - CRIAR NOVA MANIFESTAÇÃO

from operacoesbd import *

conexao = criarConexao('127.0.0.1', 'root', '1234567', 'bd_sistema_ouvidoria')

# Pergunta ao usuário o tipo da manifestação que deseja criar
tipoManifestacao = int(input("\n1. Elogio \n2. Sugestão \n3. Reclamaçao \nEscolha um tipo de manifestação acima para adicionar: "))

#A variável "tipo" será alimentada com base na opção escolhida acima
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

encerrarConexao(conexao)