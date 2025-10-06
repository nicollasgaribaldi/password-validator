import re

class PasswordValidator:
    def validate(self, password: str) -> tuple[bool, str]:
        if len(password) < 8:
            return False, "A senha deve ter no mínimo 8 caracteres."
        if not re.search(r"[A-Z]", password):
            return False, "A senha deve conter pelo menos uma letra maiúscula."
        if not re.search(r"[a-z]", password):
            return False, "A senha deve conter pelo menos uma letra minúscula."
        if not re.search(r"\d", password):
            return False, "A senha deve conter pelo menos um número."
        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
            return False, "A senha deve conter pelo menos um caractere especial."
        if re.search(r"\s", password):
            return False, "A senha não pode conter espaços."
        return True, "Senha válida."
