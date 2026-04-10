def cifrario_cesare(testo, shift):
    risultato = ""
    for i in range(len(testo)):
        char = testo[i]
        if char.isupper():
            risultato += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            risultato += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            risultato += char
    return risultato

print(cifrario_cesare("Attacco alle ore dieci", 3)) 
# Output: Dwwdffr dood ruh glhfl
