# 🛡️ Blocco 01: Fondamenti e Crittografia Simmetrica
## Lezioni 1 - 10

In questo blocco analizziamo come proteggere l'informazione usando algoritmi a chiave condivisa.

---

### 🏛️ 1. I Pilastri della Sicurezza (Lezione 1)
Ogni strategia di difesa deve soddisfare il **Triangolo CIA**:

* **Confidenzialità (Confidentiality):** Solo chi è autorizzato legge i dati. (Contro l'intercettazione).
* **Integrità (Integrity):** I dati non vengono modificati. (Contro la manomissione).
* **Disponibilità (Availability):** Il servizio è sempre raggiungibile. (Contro attacchi DoS).

---

### 🔑 2. Crittografia Simmetrica (Lezioni 3-7)
La crittografia simmetrica utilizza la **stessa chiave** per cifrare e decifrare.

#### **Classificazione degli Algoritmi**
1. **Cifrari a Sostituzione:** Ogni carattere è sostituito con un altro (es. Cesare).
2. **Cifrari a Trasposizione:** I caratteri vengono rimescolati.
3. **Cifrari a Blocchi:** Il testo è diviso in blocchi di bit fissi (es. 64 o 128 bit).



---

### ⚔️ 3. Confronto Tecnico: DES vs AES (Lezioni 6-8)
*Parte fondamentale per l'esame.*

| Caratteristica | DES | AES |
| :--- | :--- | :--- |
| **Anno** | 1977 | 2001 (Standard attuale) |
| **Dimensione Blocco** | 64 bit | 128 bit |
| **Lunghezza Chiave** | 56 bit (Debole) | 128, 192, 256 bit (Sicuro) |
| **Struttura** | Rete di Feistel | Sostituzione-Permutazione |

---

### ⚙️ 4. Modalità di Funzionamento (Lezione 9)
Come gestiamo i file grandi divisi in blocchi:

* **ECB (Electronic Codebook):** Ogni blocco è cifrato da solo. **Insicuro** perché pattern uguali creano cifrati uguali (es. in un'immagine si vedrebbero ancora le sagome).
* **CBC (Cipher Block Chaining):** Ogni blocco è concatenato al precedente. **Sicuro** perché nasconde i pattern ripetuti.






