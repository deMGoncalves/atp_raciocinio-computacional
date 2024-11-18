# Projeto ATP - Sistema de Gerenciamento Acadêmico

Este repositório contém o projeto desenvolvido para a avaliação da disciplina de Raciocínio Computacional. O sistema foi implementado em Python e utiliza conceitos como estruturas condicionais, repetição, listas e organização modular de funções.

## 📋 Descrição do Projeto

O sistema tem como objetivo gerenciar entidades acadêmicas, oferecendo funcionalidades básicas como inclusão e listagem de estudantes, além de apresentar mensagens de retorno para opções ainda em desenvolvimento. Ele foi projetado com foco na clareza e organização do código, visando facilitar futuras extensões.

## 🚀 Funcionalidades Implementadas

1. **Menu Principal:**
   - Oferece opções para gerenciar diferentes entidades: estudantes, professores, disciplinas, turmas e matrículas.
   - O menu permite navegação clara e retorna ao início em caso de entrada inválida.

2. **Gerenciamento de Estudantes:**
   - **Inclusão:** Permite cadastrar nomes de estudantes, que são armazenados em uma lista.
   - **Listagem:** Exibe os nomes cadastrados. Caso a lista esteja vazia, mostra a mensagem: "Não há estudantes cadastrados".
   - **Mensagens para funcionalidades futuras:** As opções de "Atualizar" e "Excluir" exibem a mensagem "EM DESENVOLVIMENTO".

3. **Outras Entidades:**
   - Para professores, disciplinas, turmas e matrículas, o sistema exibe a mensagem "EM DESENVOLVIMENTO".

## 🛠 Estrutura do Código

- **`main.py`:** Arquivo principal do sistema, contendo todas as funções e a lógica de execução.
  - **Organização em funções:** O código é dividido em funções para o menu principal, menu de operações, e ações específicas para cada entidade.
  - **Estrutura limpa e comentada:** Cada função tem comentários explicativos para facilitar o entendimento.

### Principais Funções:

- `menu_principal()`: Exibe o menu inicial e permite navegar entre as entidades.
- `menu_operacoes(entidade: str)`: Gera o menu de ações para a entidade selecionada.
- `executar_acao(entidade: str, opcao: str)`: Executa a ação escolhida para a entidade, verificando se a funcionalidade está implementada.
- `limpar_console()`: Limpa o console para melhor experiência do usuário.

## 📂 Como Executar

1. Certifique-se de ter o Python 3.x instalado.
2. Baixe ou clone este repositório.
3. Execute o arquivo `main.py` no terminal ou em um ambiente Python:
   ```bash
   python main.py
   ```

## 🌟 Observações

- Este projeto foi publicado no GitHub no dia da entrega para evitar possíveis cópias antes do prazo.
- A estrutura foi projetada para ser facilmente expansível, permitindo a implementação de funcionalidades futuras.
