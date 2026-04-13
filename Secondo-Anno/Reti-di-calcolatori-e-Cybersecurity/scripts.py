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
