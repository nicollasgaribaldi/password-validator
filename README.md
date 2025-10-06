# Password Validator

Pequena aplicação em Python para validar senhas conforme regras de segurança definidas.

## 🧩 Tecnologias
- Python 3.11
- Pytest
- Pytest-cov
- Pytest-html

## ⚙️ Como executar

```bash
pip install -r requirements.txt
pytest --cov=src --cov-report=term-missing
pytest --cov=src --cov-report=term-missing --cov-report=html --html=report.html --self-contained-html
```

## 🔒 Regras de Negócio Testadas

1. A senha deve ter no mínimo 8 caracteres.
2. Deve conter pelo menos uma letra maiúscula.
3. Deve conter pelo menos uma letra minúscula.
4. Deve conter pelo menos um número.
5. Deve conter pelo menos um caractere especial.
6. Não pode conter espaços em branco.

## 📊 Cobertura
<img width="1897" height="372" alt="image" src="https://github.com/user-attachments/assets/6f790e8a-70ca-4423-b97c-7ac96c9c2f41" />
<img width="546" height="237" alt="image" src="https://github.com/user-attachments/assets/ff838da2-b50b-4abe-93b6-b783a1b1b1e8" />
<img width="794" height="275" alt="image" src="https://github.com/user-attachments/assets/d1a11105-efa6-4ad5-828c-fe3e468dafd2" />
<img width="794" height="265" alt="image" src="https://github.com/user-attachments/assets/6621a9d0-1d65-4788-a387-0287b7c02a5a" />
