📖 Dicionário Interativo em Python

Um programa de terminal simples e interativo que permite ao usuário criar seu próprio dicionário personalizado, adicionando termos com seus respectivos significados e consultando-os posteriormente.

🎯 Sobre o Projeto

Este projeto implementa um dicionário dinâmico em Python, onde o usuário pode cadastrar novas palavras com seus significados e, depois, consultar o significado de qualquer termo já cadastrado. Os dados são armazenados em memória durante a execução, utilizando uma lista de dicionários.

✨ Funcionalidades
➕ Adicionar novos termos ao dicionário
🔍 Consultar o significado de um termo já cadastrado
🚫 Verificação de termos duplicados (evita cadastro repetido)
📭 Aviso quando o dicionário está vazio
⚠️ Tratamento de valores inválidos
🚪 Opção de encerrar o programa a qualquer momento
🛠️ Tecnologias Utilizadas
Python 3

Este projeto não possui dependências externas — utiliza apenas recursos nativos da linguagem.

📋 Pré-requisitos
Python 3.8 ou superior
📦 Instalação
Clone este repositório:
bash
git clone https://github.com/seu-usuario/dicionario-interativo.git
cd dicionario-interativo
Não há dependências para instalar — o script já está pronto para uso.
▶️ Como Usar

Execute o script principal:

bash
python dicionario.py

O programa exibirá um menu de opções:

PÔR (ou POR) — cadastra um novo termo, pedindo o nome do termo e seu significado
TERMO — consulta o significado de um termo já cadastrado
SAIR — encerra o programa
Exemplo de uso
Olá, tudo bem?
Deseja pôr um termo novo ou saber um termo('Pôr' - Para pôr novo termo / 'Termo' - para ver termo / 'Sair' - para encerrar)? PÔR
Qual termo deseja pôr no dicionário? Python
Qual siginificado do termo? Linguagem de programação de alto nível
Como o vocabulário não consta no dicionário, será adicionado.
O termo adicionado foi Python

Deseja pôr um termo novo ou saber um termo(...)? TERMO
Qual termo gostaria de descobrir o significado? Python
O significado de Python é: Linguagem de programação de alto nível
📁 Estrutura do Projeto
dicionario-interativo/
├── dicionario.py   # Script principal
└── README.md       # Documentação do projeto

⚠️ Os dados cadastrados são armazenados apenas em memória (na lista dicionario) e são perdidos ao encerrar o programa.

🚧 Possíveis Melhorias Futuras
 Persistência de dados em arquivo (JSON, CSV ou banco de dados)
 Opção de editar ou remover termos já cadastrados
 Listagem de todos os termos cadastrados
 Busca por termos parciais (não apenas exatos)
 Interface gráfica (GUI) ou versão web
📄 Licença

Este projeto está disponível sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

👤 Autor

Desenvolvido como projeto de estudo em Python, praticando estruturas de dados, laços de repetição e tratamento de exceções.
