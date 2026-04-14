#cifrario di cesare
def cifrario_cesare(testo, shift):
    risultato = ""
    for char in testo:
        if char.isupper():
            risultato += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            risultato += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            risultato += char
    return risultato

# Simulazione  RSA
import math

def is_prime(num):
    """Controlla se un numero è primo (implementazione semplice)."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def genera_modulo_rsa(p: int, q: int) -> dict:
    """
    Genera il modulo RSA e la funzione di Eulero.
    
    Args:
        p (int): Numero primo.
        q (int): Numero primo diverso da p.
    
    Returns:
        dict: {'n': modulo pubblico, 'phi': funzione di Eulero}
    
    Raises:
        ValueError: Se p o q non sono primi o non validi.
    """
    if not isinstance(p, int) or not isinstance(q, int):
        raise ValueError("p e q devono essere interi.")
    if p == q:
        raise ValueError("p e q devono essere diversi.")
    if not is_prime(p) or not is_prime(q):
        raise ValueError("p e q devono essere numeri primi.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    print(f"Numeri Primi scelti: p={p}, q={q}")
    print(f"Modulo n (Pubblico): {n}")
    print(f"Funzione Toziente phi (Segreta): {phi}")
    
    return {'n': n, 'phi': phi}

# Simulazione Diffie-Hellman
def diffie_hellman():
    # Parametri pubblici condivisi (Base e Modulo)
    g = 9  # Base
    p = 23 # Numero primo (Modulo)
    
    # Segreti privati
    a_secret = 6  # Segreto di Alice
    b_secret = 15 # Segreto di Bob
    
    # Calcolo dei valori da scambiarsi
    A_send = (g**a_secret) % p
    B_send = (g**b_secret) % p
    
    # Calcolo della chiave segreta comune
    key_alice = (B_send**a_secret) % p
    key_bob = (A_send**b_secret) % p
    
    print(f"Chiave calcolata da Alice: {key_alice}")
    print(f"Chiave calcolata da Bob: {key_bob}")
    return key_alice == key_bob

diffie_hellman()


