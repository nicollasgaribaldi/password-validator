# 🔐 Password Validator

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/nicollasgaribaldi/password-validator)
[![Coverage](https://img.shields.io/badge/coverage-100%25-success.svg)](https://github.com/nicollasgaribaldi/password-validator)

> Primeira avaliação da disciplina **Qualidade de Software**  
> Sistema de validação de senhas com testes unitários automatizados

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Regras de Negócio Testadas](#-regras-de-negócio-testadas)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Executar a Aplicação](#-como-executar-a-aplicação)
- [Como Executar os Testes](#-como-executar-os-testes)
- [Relatório de Cobertura](#-relatório-de-cobertura)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Autor](#-autor)

## 🎯 Sobre o Projeto

O **Password Validator** é uma aplicação Python desenvolvida para validar senhas de acordo com regras de segurança predefinidas pela empresa. O sistema foi criado com foco em **qualidade de software**, implementando testes unitários automatizados com alta cobertura de código.

### Objetivo

Garantir que as senhas dos usuários atendam aos critérios mínimos de segurança, reduzindo vulnerabilidades e protegendo informações sensíveis contra acessos não autorizados.

### Contexto de Uso

- Sistemas de cadastro de usuários
- APIs de autenticação
- Validação client-side e server-side
- Políticas corporativas de segurança

## 🧪 Regras de Negócio Testadas

Esta seção mapeia cada regra de negócio implementada com seus respectivos testes unitários:

### 1. **Tamanho Mínimo da Senha**
- **Regra**: A senha deve ter no mínimo 8 caracteres
- **Justificativa**: Senhas curtas são mais vulneráveis a ataques de força bruta
- **Testes Implementados**:
  - `test_password_minimum_length_valid()` - Valida senha com exatamente 8 caracteres
  - `test_password_minimum_length_invalid()` - Rejeita senhas com menos de 8 caracteres
  - `test_password_empty()` - Rejeita senha vazia
- **Cenários Cobertos**:
  - ✅ Senha com 8 caracteres: `"Abc123@#"`
  - ❌ Senha com 7 caracteres: `"Abc12@#"`
  - ❌ Senha vazia: `""`

### 2. **Presença de Letra Maiúscula**
- **Regra**: Deve conter pelo menos uma letra maiúscula (A-Z)
- **Justificativa**: Aumenta a complexidade da senha contra ataques de dicionário
- **Testes Implementados**:
  - `test_password_uppercase_present()` - Valida senha com maiúscula
  - `test_password_uppercase_missing()` - Rejeita senha sem maiúscula
- **Cenários Cobertos**:
  - ✅ Com maiúscula: `"Password123@"`
  - ❌ Sem maiúscula: `"password123@"`

### 3. **Presença de Letra Minúscula**
- **Regra**: Deve conter pelo menos uma letra minúscula (a-z)
- **Justificativa**: Adiciona diversidade de caracteres à senha
- **Testes Implementados**:
  - `test_password_lowercase_present()` - Valida senha com minúscula
  - `test_password_lowercase_missing()` - Rejeita senha sem minúscula
- **Cenários Cobertos**:
  - ✅ Com minúscula: `"Password123@"`
  - ❌ Sem minúscula: `"PASSWORD123@"`

### 4. **Presença de Número**
- **Regra**: Deve conter pelo menos um dígito numérico (0-9)
- **Justificativa**: Mesclar letras e números dificulta ataques automatizados
- **Testes Implementados**:
  - `test_password_digit_present()` - Valida senha com número
  - `test_password_digit_missing()` - Rejeita senha sem número
- **Cenários Cobertos**:
  - ✅ Com número: `"Password123@"`
  - ❌ Sem número: `"Password@#$"`

### 5. **Presença de Caractere Especial**
- **Regra**: Deve conter pelo menos um caractere especial (!@#$%^&*()_+-=[]{}|;:,.<>?)
- **Justificativa**: Máxima complexidade e resistência a ataques
- **Testes Implementados**:
  - `test_password_special_char_present()` - Valida senha com caractere especial
  - `test_password_special_char_missing()` - Rejeita senha sem caractere especial
- **Cenários Cobertos**:
  - ✅ Com especial: `"Password123@"`
  - ❌ Sem especial: `"Password1234"`

### 6. **Ausência de Espaços em Branco**
- **Regra**: Não pode conter espaços em branco
- **Justificativa**: Evita erros de digitação e problemas de parsing
- **Testes Implementados**:
  - `test_password_no_whitespace_valid()` - Valida senha sem espaços
  - `test_password_whitespace_invalid()` - Rejeita senha com espaços
- **Cenários Cobertos**:
  - ✅ Sem espaços: `"Password123@"`
  - ❌ Com espaços: `"Pass word123@"`
  - ❌ Com espaço inicial: `" Password123@"`
  - ❌ Com espaço final: `"Password123@ "`

### 7. **Validação Completa (Integração)**
- **Regra**: A senha deve atender a TODAS as regras simultaneamente
- **Testes Implementados**:
  - `test_password_fully_valid()` - Valida senha que atende todos os critérios
  - `test_password_multiple_violations()` - Rejeita senha com múltiplas violações
- **Cenários Cobertos**:
  - ✅ Senha válida: `"SecurePass123@"`
  - ❌ Múltiplas falhas: `"abc"`

### 8. **Casos Extremos (Edge Cases)**
- **Testes Implementados**:
  - `test_password_null()` - Rejeita entrada None
  - `test_password_only_special_chars()` - Valida comportamento com apenas caracteres especiais
  - `test_password_very_long()` - Valida senhas muito longas
  - `test_password_unicode_characters()` - Comportamento com caracteres Unicode
- **Cenários Cobertos**:
  - Entrada nula
  - Senhas extremamente longas (>100 caracteres)
  - Caracteres especiais de diferentes idiomas

## 🛠 Tecnologias Utilizadas

- **Python 3.11** - Linguagem de programação
- **Pytest** - Framework de testes unitários
- **Pytest-cov** - Plugin para análise de cobertura de código
- **Pytest-html** - Geração de relatórios HTML dos testes

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)

Verificar instalação:
```bash
python --version  # Deve retornar Python 3.11.x
pip --version     # Deve retornar pip 23.x ou superior
```

## ⚙️ Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/nicollasgaribaldi/password-validator.git
cd password-validator
```

### 2. Criar ambiente virtual (recomendado)
```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém:
```
pytest==7.4.3
pytest-cov==4.1.0
pytest-html==4.1.1
```

## 🚀 Como Executar a Aplicação

### Modo Interativo (CLI)
```bash
python src/main.py
```

Você será solicitado a digitar uma senha para validação:
```
=== Password Validator ===
Digite uma senha para validar: SecurePass123@

✅ Senha válida!
A senha atende a todos os critérios de segurança.
```

### Uso Programático
```python
from src.password_validator import PasswordValidator

validator = PasswordValidator()
resultado = validator.validate("SecurePass123@")

if resultado.is_valid:
    print("Senha válida!")
else:
    print(f"Erros encontrados: {resultado.errors}")
```

### Validação em Lote
```bash
python src/batch_validator.py passwords.txt
```

## 🧪 Como Executar os Testes

### Executar todos os testes
```bash
pytest
```

### Executar com output detalhado
```bash
pytest -v
```

### Executar testes específicos
```bash
# Testar apenas validação de maiúsculas
pytest tests/test_password_validator.py::test_password_uppercase_present

# Testar um arquivo específico
pytest tests/test_password_validator.py
```

### Executar com cobertura de código
```bash
pytest --cov=src --cov-report=term-missing
```

### Gerar relatório HTML completo
```bash
pytest --cov=src --cov-report=term-missing --cov-report=html --html=report.html --self-contained-html
```

Após executar, abra o arquivo `report.html` no navegador para visualizar o relatório detalhado.

## 📊 Relatório de Cobertura

### Cobertura Atual: 100%

O projeto mantém cobertura completa de código, garantindo que todas as funcionalidades críticas estão testadas.

#### Exemplo de Saída do Pytest-cov:
```
---------- coverage: platform linux, python 3.11.0 -----------
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
src/__init__.py                       0      0   100%
src/password_validator.py            45      0   100%
src/validation_rules.py              32      0   100%
src/exceptions.py                     8      0   100%
---------------------------------------------------------------
TOTAL                                85      0   100%
```

#### Visualização dos Relatórios

**Relatório em Terminal:**

<img width="1915" height="483" alt="image" src="https://github.com/user-attachments/assets/18822133-ab7a-423e-ab46-1642b3537b7e" />

**Relatório HTML Detalhado:**

<img width="541" height="242" alt="image" src="https://github.com/user-attachments/assets/806b9b09-096b-4f40-98af-de7dd0a01941" />
<img width="793" height="272" alt="image" src="https://github.com/user-attachments/assets/083be693-7b15-4303-8773-d12caeef477e" />
<img width="793" height="261" alt="image" src="https://github.com/user-attachments/assets/f1c8c507-8bf1-4cd8-aa4b-c5e545302529" />

### Métricas de Qualidade

- ✅ **100% de cobertura** em código de produção
- ✅ **42 testes** passando
- ✅ **0 testes falhando**
- ✅ **0 advertências** ou warnings
- ✅ Tempo médio de execução: **< 0.5s**

## 📁 Estrutura do Projeto

```
password-validator/
│
├── src/
│   ├── __init__.py
│   ├── password_validator.py      # Classe principal de validação
│   ├── validation_rules.py        # Regras individuais de validação
│   ├── exceptions.py              # Exceções customizadas
│   └── main.py                    # Interface CLI
│
├── tests/
│   ├── __init__.py
│   ├── test_password_validator.py # Testes da classe principal
│   ├── test_validation_rules.py   # Testes das regras individuais
│   └── test_integration.py        # Testes de integração
│
├── docs/
│   └── coverage_report/           # Relatórios HTML gerados
│
├── .gitignore
├── requirements.txt               # Dependências do projeto
├── pytest.ini                     # Configurações do Pytest
└── README.md                      # Este arquivo
```

## 💡 Exemplos de Uso

### Senhas Válidas ✅
```python
senhas_validas = [
    "SecurePass123@",
    "MyP@ssw0rd!",
    "Tr0ng#Pass",
    "C0mpl3x&Secure",
    "Valid@Pass123"
]
```

### Senhas Inválidas ❌
```python
senhas_invalidas = [
    "abc",              # Muito curta
    "password123",      # Sem maiúscula e caractere especial
    "PASSWORD123@",     # Sem minúscula
    "Password@",        # Sem número
    "Password123",      # Sem caractere especial
    "Pass word123@"     # Com espaço
]
```

### Exemplo Completo
```python
from src.password_validator import PasswordValidator

validator = PasswordValidator()

# Validar múltiplas senhas
senhas = ["SecurePass123@", "fraca", "Média123"]

for senha in senhas:
    resultado = validator.validate(senha)
    
    if resultado.is_valid:
        print(f"✅ '{senha}' é válida")
    else:
        print(f"❌ '{senha}' é inválida:")
        for erro in resultado.errors:
            print(f"   - {erro}")
```

### Saída Esperada
```
✅ 'SecurePass123@' é válida
❌ 'fraca' é inválida:
   - A senha deve ter no mínimo 8 caracteres
   - Deve conter pelo menos uma letra maiúscula
   - Deve conter pelo menos um número
   - Deve conter pelo menos um caractere especial
❌ 'Média123' é inválida:
   - Deve conter pelo menos um caractere especial
```

## 🔍 Detalhes de Implementação

### Arquitetura

O projeto utiliza o padrão **Strategy** para validação de regras:

```python
class ValidationRule(ABC):
    @abstractmethod
    def validate(self, password: str) -> ValidationResult:
        pass

class MinimumLengthRule(ValidationRule):
    def validate(self, password: str) -> ValidationResult:
        # Implementação específica
        pass
```

### Fluxo de Validação

1. **Entrada**: Usuário fornece senha
2. **Sanitização**: Remoção de caracteres invisíveis (opcional)
3. **Validação**: Cada regra é aplicada sequencialmente
4. **Agregação**: Resultados são combinados
5. **Resposta**: Retorna status + lista de erros

### Extensibilidade

Adicionar novas regras é simples:

```python
class NoRepeatedCharsRule(ValidationRule):
    def validate(self, password: str) -> ValidationResult:
        if any(password.count(char) > 3 for char in set(password)):
            return ValidationResult(
                is_valid=False,
                errors=["Não pode ter mais de 3 caracteres repetidos"]
            )
        return ValidationResult(is_valid=True)
```

## 🎓 Aprendizados e Boas Práticas

Este projeto demonstra:

- ✅ **Test-Driven Development (TDD)**: Testes escritos antes da implementação
- ✅ **Clean Code**: Código legível e manutenível
- ✅ **SOLID Principles**: Especialmente Single Responsibility e Open/Closed
- ✅ **Cobertura de Testes**: 100% do código crítico testado
- ✅ **Documentação**: README completo e código autodocumentado
- ✅ **Versionamento**: Uso adequado de Git e GitHub
- ✅ **CI/CD Ready**: Preparado para integração contínua

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaRegra`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova regra de validação'`)
4. Push para a branch (`git push origin feature/NovaRegra`)
5. Abra um Pull Request

### Checklist para PRs

- [ ] Código segue o estilo do projeto
- [ ] Testes adicionados/atualizados
- [ ] Cobertura mantida em 100%
- [ ] Documentação atualizada
- [ ] Todos os testes passando

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais como parte da disciplina de Qualidade de Software.

## 👨‍💻 Autor

**Nicollas Garibaldi**

- GitHub: [@nicollasgaribaldi](https://github.com/nicollasgaribaldi)
- Projeto: [password-validator](https://github.com/nicollasgaribaldi/password-validator)

---

## 📚 Referências

- [OWASP Password Guidelines](https://owasp.org/www-community/password-special-characters)
- [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)

---

**Desenvolvido com ❤️ e ☕ para a disciplina de Qualidade de Software**

*Última atualização: Outubro 2025*
