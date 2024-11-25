
import os
import platform
import time
import json

"""
Módulo de gerenciamento de sistema acadêmico.

Este módulo implementa um menu de gerenciamento de entidades do sistema acadêmico, permitindo que
usuários possam incluir, listar, atualizar e excluir dados de entidades como estudantes, professores,
disciplinas, turmas e matrículas.

@autor: Cleber de Moraes Goncalves 😊✨
"""

# ===================== INFRAESTRUTURA ===================== #

def limpar_console() -> None:
    """
    Limpa o console para melhorar a experiência do usuário.

    Funciona tanto no Windows quanto no Linux/macOS.
    """
    sistema_operacional = platform.system()
    
    if sistema_operacional == "Windows":
        os.system('cls')  # Comando para limpar o console no Windows
    else:
        os.system('clear')  # Comando para limpar o console no Linux/macOS

def imprimir_cabecalho(titulo: str) -> None:
    """
    Imprime um cabeçalho estiloso formatado com base no título passado.

    @param {str} titulo - O título a ser exibido no cabeçalho.
    """
    print(f"####### {titulo.upper()} ######")


# ===================== GERENCIAMENTO DE DADOS ===================== #

DADOS_PATH = 'dados.json'

def carregar_dados() -> dict:
    """
    Carrega os dados do arquivo JSON.

    @return {dict} Um dicionário com os dados carregados.
    """
    if not os.path.exists(DADOS_PATH):
        return {entidade: [] for entidade in entidades.values()}
    
    with open(DADOS_PATH, 'r') as arquivo:
        return json.load(arquivo)

def salvar_dados(dados: dict) -> None:
    """
    Salva os dados no arquivo JSON.

    @param {dict} dados - Um dicionário com os dados a serem salvos.
    """
    with open(DADOS_PATH, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# ======================== DOMÍNIO ======================== #

# Dicionário para mapear opções do menu principal com suas entidades
entidades = {
    '1': 'estudantes',
    '2': 'professores',
    '3': 'disciplinas',
    '4': 'turmas',
    '5': 'matrículas'
}

# Dicionário para mapear opções do menu de operações com suas ações
acoes = {
    '1': 'Incluir',
    '2': 'Listar',
    '3': 'Atualizar',
    '4': 'Excluir'
}


# ===================== APLICAÇÃO ===================== #

def menu_principal() -> None:
    """
    Exibe o menu principal com as opções de entidades e permite que o usuário
    selecione qual entidade deseja gerenciar.

    Caso o usuário escolha uma opção válida, o menu de operações para a entidade será chamado.
    O menu é exibido em loop até que o usuário escolha a opção de sair.
    """
    while True:
        limpar_console()  # Limpa o console antes de exibir o menu principal
        imprimir_cabecalho("menu principal")  # Exibe o cabeçalho do menu principal

        # Exibe as opções disponíveis no menu principal
        for key, entidade in entidades.items():
            print(f"({key}) Gerenciar {entidade}.")
        print("(0) Sair.")
        
        # Recebe a opção escolhida pelo usuário
        opcao = input("Informe a opção desejada: ")
        
        # Verifica a opção escolhida e executa a ação correspondente
        if opcao == '0':
            limpar_console()  # Limpa o console antes de exibir o menu principal
            print("Finalizando aplicação...")
            time.sleep(1)  # Delay de 1 segundos
            break
        elif opcao in entidades:
            # Chama o menu de operações para a entidade selecionada
            menu_operacoes(entidades[opcao])
        else:
            print("Opção inválida. Tente novamente.")


def menu_operacoes(entidade: str) -> None:
    """
    Exibe o menu de operações para a entidade selecionada, permitindo que o usuário
    escolha a ação que deseja realizar (Incluir, Listar, Atualizar, Excluir).

    @param {str} entidade - Nome da entidade selecionada no menu principal.
    """
    while True:
        limpar_console()  # Limpa o console antes de exibir o menu principal
        imprimir_cabecalho(f"menu de operações - {entidade}")  # Exibe o cabeçalho do menu de operações

        # Exibe as ações disponíveis no menu de operações
        for key, acao in acoes.items():
            print(f"({key}) {acao}.")
        print("(0) Voltar ao menu principal.")
        
        # Recebe a ação escolhida pelo usuário
        opcao = input("Informe a ação desejada: ")
        
        # Verifica a ação escolhida e executa a ação correspondente
        if opcao == '0':
            limpar_console()  # Limpa o console antes de exibir o menu principal
            print("Voltando ao menu principal...")
            time.sleep(1)  # Delay de 1 segundos
            break
        elif opcao in acoes:
            executar_acao(entidade, opcao)
        else:
            print("Opção inválida. Tente novamente.")


def executar_acao(entidade: str, opcao: str) -> None:
    """
    Executa a ação escolhida pelo usuário para a entidade selecionada.

    @param {str} entidade - Nome da entidade para a qual a ação será realizada.
    @param {str} opcao - A ação selecionada (Incluir, Listar, Atualizar, Excluir).
    """
    dados = carregar_dados()
    if opcao == '1':  # Incluir
        novo_item = input(f"Informe os dados do novo {entidade[:-1]}: ")
        dados[entidade].append(novo_item)
        salvar_dados(dados)
        print(f"{entidade[:-1].capitalize()} incluído com sucesso!")
    elif opcao == '2':  # Listar
        if not dados[entidade]:
            print(f"Não há {entidade} cadastrados.")
        else:
            print(f"Lista de {entidade}:")
            for idx, item in enumerate(dados[entidade], start=1):
                print(f"{idx}. {item}")
    elif opcao == '3':  # Atualizar
        if not dados[entidade]:
            print(f"Não há {entidade} cadastrados.")
        else:
            for idx, item in enumerate(dados[entidade], start=1):
                print(f"{idx}. {item}")
            indice = int(input("Informe o número do item que deseja atualizar: ")) - 1
            if 0 <= indice < len(dados[entidade]):
                novo_valor = input(f"Informe o novo valor para {entidade[:-1]}: ")
                dados[entidade][indice] = novo_valor
                salvar_dados(dados)
                print(f"{entidade[:-1].capitalize()} atualizado com sucesso!")
            else:
                print("Índice inválido.")
    elif opcao == '4':  # Excluir
        if not dados[entidade]:
            print(f"Não há {entidade} cadastrados.")
        else:
            for idx, item in enumerate(dados[entidade], start=1):
                print(f"{idx}. {item}")
            indice = int(input("Informe o número do item que deseja excluir: ")) - 1
            if 0 <= indice < len(dados[entidade]):
                dados[entidade].pop(indice)
                salvar_dados(dados)
                print(f"{entidade[:-1].capitalize()} excluído com sucesso!")
            else:
                print("Índice inválido.")
    
    input("\nPressione enter para continuar...")

# ===================== INICIALIZAÇÃO ===================== #

if __name__ == "__main__":
    """
    Ponto de entrada da aplicação.
    
    Inicia a exibição do menu principal e aguarda a interação do usuário.
    """
    menu_principal()
