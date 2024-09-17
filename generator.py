# generator.py

import secrets
import string

def generate_password(length=12, use_special_chars=True, exclude_ambiguous=True):
    """Gera uma senha segura e aleatória.
    
    Args:
        length (int): Comprimento da senha.
        use_special_chars (bool): Incluir caracteres especiais.
        exclude_ambiguous (bool): Excluir caracteres ambíguos (ex.: l, O, 0, I).

    Returns:
        str: Senha gerada.
    """
    alphabet = string.ascii_letters + string.digits
    if use_special_chars:
        alphabet += string.punctuation

    if exclude_ambiguous:
        alphabet = alphabet.replace('l', '').replace('O', '').replace('0', '').replace('I', '')

    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    length = int(input("Comprimento da senha: "))
    use_special_chars = input("Incluir caracteres especiais? (s/n): ").lower() == 's'
    exclude_ambiguous = input("Excluir caracteres ambíguos? (s/n): ").lower() == 's'

    password = generate_password(length, use_special_chars, exclude_ambiguous)
    print(f"Senha gerada: {password}")

if __name__ == "__main__":
    main()
