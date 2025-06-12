from contato import Contato
import banco


def exibir_menu():
    while True:
        print("Menu de Contatos")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Atualizar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            email = input("Digite o email do contato: ")
            telefone = input("Digite o telefone do contato: ")
            contato = Contato(nome, email, telefone)
            banco.adicionar_contato(
                contato.nome, contato.email, contato.telefone)
        elif opcao == '2':
            contatos = banco.listar_contatos()
            if contatos:
                print("Lista de Contatos:")
                for contato in contatos:
                    print(
                        f"ID: {contato[0]}, Nome: {contato[1]}, Email: {contato[2]}, Telefone: {contato[3]}")
            else:
                print("Nenhum contato encontrado.")
        elif opcao == '3':
            try:
                id_contato = int(
                    input("Digite o ID do contato a ser atualizado: "))
                nome = input("Digite o novo nome do contato: ")
                email = input("Digite o novo email do contato: ")
                telefone = input("Digite o novo telefone do contato: ")
                contato = Contato(nome, telefone, email)
                banco.atualizar_contato(
                    id_contato, contato.nome, contato.email, contato.telefone)
                print("Contato atualizado com sucesso.")
            except ValueError:
                print("ID inválido. Por favor, insira um número inteiro.")
        elif opcao == '4':
            try:
                id_contato = int(
                    input("Digite o ID do contato a ser removido: "))
                banco.remover_contato(id_contato)
                print("Contato removido com sucesso.")
            except ValueError:
                print("ID inválido. Por favor, insira um número inteiro.")
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
