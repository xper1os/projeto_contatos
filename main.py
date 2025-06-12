import banco
from menu import exibir_menu

if __name__ == "__main__":
    # Inicializa o banco de dados
    banco.conectar()

    # Exibe o menu para o usuário
    exibir_menu()
