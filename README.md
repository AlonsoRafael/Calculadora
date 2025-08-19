# 🧮 Calculadora Python

Uma calculadora moderna e elegante construída com Python e PySide6, apresentando uma interface gráfica intuitiva com tema escuro.

## ✨ Características

- **Interface moderna** com tema escuro elegante
- **Operações matemáticas básicas**: adição, subtração, multiplicação e divisão
- **Operações avançadas**: potenciação (^) e inversão de sinal (N)
- **Suporte completo ao teclado** para entrada rápida
- **Display responsivo** com alinhamento à direita
- **Histórico de cálculos** exibido na área de informações
- **Tratamento de erros** com mensagens informativas
- **Interface redimensionável** que se ajusta automaticamente

## 🖥️ Interface

A calculadora possui uma interface limpa e organizada:

- **Display principal**: Área de entrada e visualização dos números
- **Área de informações**: Mostra o histórico e resultado das operações
- **Grid de botões**: Layout 5x4 com todos os controles necessários

### Layout dos Botões

```
[ C ] [ D ] [ ^ ] [ / ]
[ 7 ] [ 8 ] [ 9 ] [ * ]
[ 4 ] [ 5 ] [ 6 ] [ - ]
[ 1 ] [ 2 ] [ 3 ] [ + ]
[ N ] [ 0 ] [ . ] [ = ]
```

## 🎮 Como Usar

### Mouse

- Clique nos botões numerados para inserir números
- Use os botões de operação (+, -, \*, /, ^) para operações matemáticas
- Pressione "=" para calcular o resultado
- "C" limpa tudo
- "D" apaga o último caractere
- "N" inverte o sinal do número atual

### Teclado

- **Números 0-9**: Inserir dígitos
- **+ - \* /**: Operações matemáticas básicas
- **P**: Potenciação (^)
- **Enter ou =**: Calcular resultado
- **Backspace ou D**: Apagar último caractere
- **Escape ou C**: Limpar tudo
- **.**: Inserir ponto decimal

## 🛠️ Requisitos

- Python 3.9 a 3.12 (recomendado: 3.12)
- PySide6
- qdarktheme

> **⚠️ Importante**: `qdarktheme` atualmente suporta Python 3.9 até 3.12. Se você estiver usando Python 3.13+, veja as [opções alternativas](#-solucionando-problemas-de-instalação) abaixo.

## 📦 Instalação

### Instalação Padrão (Python 3.9-3.12)

1. Clone ou baixe este repositório
2. Instale as dependências:

```bash
pip install PySide6 qdarktheme
```

3. Execute o programa:

```bash
python main.py
```

### 🔧 Solucionando Problemas de Instalação

#### Problema: Python 3.13+ (qdarktheme incompatível)

Se você estiver usando Python 3.13 ou superior, você tem algumas opções:

**Opção 1: Usar sem tema escuro (mais simples)**

```bash
# Instale apenas o PySide6
pip install PySide6

# Modifique o arquivo style.py para desabilitar o qdarktheme
```

**Opção 2: Usar Python 3.12 com pyenv (recomendado)**

```bash
# Instale pyenv (Windows)
git clone https://github.com/pyenv-win/pyenv-win.git %USERPROFILE%\.pyenv

# Instale Python 3.12
pyenv install 3.12.0
pyenv local 3.12.0

# Instale as dependências
pip install PySide6 qdarktheme
```

**Opção 3: Usar ambiente virtual com Python 3.12**

```bash
# Se você tiver Python 3.12 instalado
py -3.12 -m venv venv_calc
venv_calc\Scripts\activate
pip install PySide6 qdarktheme
```

#### Para usar sem qdarktheme:

Edite o arquivo `style.py` e comente ou remova as linhas relacionadas ao qdarktheme:

```python
# import qdarktheme  # Comente esta linha

def setupTheme():
    # qdarktheme.setup_theme(...)  # Comente todo este bloco
    pass  # Adicione apenas isto
```

## 📁 Estrutura do Projeto

```
calculadora/
├── main.py              # Arquivo principal da aplicação
├── main_window.py       # Janela principal da calculadora
├── display.py           # Display de entrada/saída
├── buttons.py           # Grid de botões e lógica de operações
├── info.py              # Área de informações/histórico
├── utils.py             # Funções utilitárias
├── variables.py         # Constantes e configurações
├── style.py             # Configuração do tema e estilos
└── files/
    └── icon.png         # Ícone da aplicação
```

## 🏗️ Arquitetura

O projeto segue uma arquitetura modular com separação clara de responsabilidades:

- **`MainWindow`**: Gerencia a janela principal e layout geral
- **`Display`**: Controla a entrada de dados e eventos de teclado
- **`ButtonsGrid`**: Gerencia o grid de botões e lógica de cálculo
- **`Info`**: Exibe informações e histórico das operações
- **`Utils`**: Funções auxiliares para validação e conversão
- **`Variables`**: Configurações centralizadas (cores, fontes, tamanhos)
- **`Style`**: Configuração de temas e estilos visuais

## ⚡ Funcionalidades Técnicas

- **Validação de entrada**: Previne entrada de dados inválidos
- **Tratamento de erros**: Divisão por zero e overflow são tratados adequadamente
- **Sinais Qt**: Comunicação eficiente entre componentes
- **Tema responsivo**: Interface que se adapta automaticamente
- **Foco automático**: O display mantém foco para entrada contínua

## 🐛 Tratamento de Erros

A calculadora trata os seguintes tipos de erro:

- **Divisão por zero**: Exibe mensagem de erro específica
- **Overflow matemático**: Para cálculos que excedem limites
- **Entrada inválida**: Previne caracteres não numéricos indevidos
- **Operações incompletas**: Verifica se todos os operandos foram fornecidos

## 🎨 Personalização

As cores e tamanhos podem ser facilmente modificados no arquivo `variables.py`:

```python
PRIMARY_COLOR = '#1e81b0'           # Cor principal dos botões especiais
DARKER_PRIMARY_COLOR = '#16658a'    # Cor hover
DARKEST_PRIMARY_COLOR = '#115270'   # Cor pressed

BIG_FONT_SIZE = 40      # Tamanho da fonte do display
MEDIUM_FONT_SIZE = 24   # Tamanho da fonte dos botões
SMALL_FONT_SIZE = 18    # Tamanho da fonte das informações
```

## 🚀 Execução

Para executar a calculadora:

```bash
python main.py
```

A aplicação abrirá uma janela com a calculadora pronta para uso.

## 📝 Licença

Este projeto é de código aberto e está disponível para uso educacional.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:

- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests
- Melhorar a documentação

---

## 📋 Notas de Versão

### Compatibilidade com Python 3.13+

- ✅ **Versão atual**: Funciona com Python 3.13+ usando tema escuro customizado
- 📁 **Backup disponível**: `style_with_qdarktheme.py` contém a versão original com qdarktheme
- 🎨 **Tema**: Sistema de tema escuro personalizado implementado em CSS/QSS nativo

_Desenvolvido com ❤️ usando Python e PySide6_
