# SISTEMA DE OUVIDORIA COM MYSQL - SEGUNDA ENTREGA (PYTHON)
from operacoesbd import *
from todosOsMetodosMenu import *


conexao = criarConexao("127.0.0.1", "root", "1234567", "bd_sistema_ouvidoria")

menu = 0

print("\n=== Bem-vindo(a) ao Sistema de Ouvidoria ===")
print("Aqui você pode registrar, consultar e gerenciar manifestações.")

while menu != 7:
    print("\n--- MENU PRINCIPAL ---"
          "\n1️⃣) Listar todas as manifestações"
          "\n2️⃣) Listar manifestações por tipo"
          "\n3️⃣) Criar nova manifestação"
          "\n4️⃣) Exibir quantidade de manifestações"
          "\n5️⃣) Pesquisar manifestação por código"
          "\n6️⃣) Excluir manifestação pelo código"
          "\n7️⃣) Sair")

    try:
        menu = int(input("Escolha uma das opções acima: "))
    except ValueError:
        print("Opção inválida! Escolha uma opção de 1 a 7.")
        continue

    if menu == 1:
        listarManifestacoes(conexao)

    elif menu == 2:
        listarManifestacoesPorTipo(conexao)

    elif menu == 3:
        criarNovaManifestacao(conexao)

    elif menu == 4:
        exibirQuantidade(conexao)

    elif menu == 5:
        pesquisarPorCodigo(conexao)

    elif menu == 6:
        excluirPeloCodigo(conexao)

    elif menu != 7:
        print("⚠️  Opção inválida. Escolha uma das opções listadas acima!")


print("\nObrigado(a) por usar nosso Sistema de Ouvidoria!"
      "\nSua opinião é muito importante para nós. Até a próxima!")

encerrarConexao(conexao)
