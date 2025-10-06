import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validator import PasswordValidator


validator = PasswordValidator()

def test_valid_password():
    assert validator.validate("Abcd@123")[0] == True

def test_short_password():
    result, message = validator.validate("Abc@1")
    assert result == False
    assert "mínimo 8" in message

def test_missing_uppercase():
    result, message = validator.validate("abcd@123")
    assert result == False
    assert "maiúscula" in message

def test_missing_lowercase():
    result, message = validator.validate("ABCD@123")
    assert result == False
    assert "minúscula" in message

def test_missing_number():
    result, message = validator.validate("Abcdef@x")
    assert result == False
    assert "número" in message

def test_missing_special_char():
    result, message = validator.validate("Abcdef12")
    assert result == False
    assert "caractere especial" in message

def test_contains_space():
    result, message = validator.validate("Abc 123@")
    assert result == False
    assert "espaços" in message