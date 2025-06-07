#SISTEMA DE OUVIDORIA COM MYSQL - SEGUNDA ENTREGA (PYTHON)
from operacoesbd import *
conexao = criarConexao("127.0.0.1", "root", "1234567", "sistema_de_ouvidoria_bd")

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
        print("Listar todas as manifestações")

    elif menu == 2:
       print("Listar manifestações por tipo")

    elif menu == 3:
        print("Criar nova manifestação")
    
    elif menu == 4:
        print("Exibir quantidade de manifestações")

    elif menu == 5:
        print("Pesquisar manifestação por código")

    elif menu == 6:
        print("Excluir manifestação pelo código")

    elif menu != 6:
        print("⚠️  Opção inválida. Escolha uma das opções listadas acima!")
        

print("\nObrigado(a) por usar nosso Sistema de Ouvidoria!"
      "\nSua opinião é muito importante para nós. Até a próxima!")

encerrarConexao(conexao)
