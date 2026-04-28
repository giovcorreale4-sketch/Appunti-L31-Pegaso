# 🔒 Reti Blocco 02: Sicurezza e Protocolli Standard
## Lezioni 9 - 16

In questo blocco analizziamo come i protocolli di rete integrano la crittografia per proteggere i dati a diversi livelli dello stack.

---

### 🪪 1. Identità Digitale: X.509 (Lezioni 9-10)
Per evitare attacchi Man-in-the-Middle, dobbiamo essere certi dell'identità del server.
* **Certificato X.509:** Un documento digitale che lega una chiave pubblica a un'identità (es. `google.com`).
* **CA (Certification Authority):** L'ente che firma il certificato, garantendone la validità.

---

### 🛡️ 2. Sicurezza ai Vari Livelli (Lezioni 11-15)

L'esame si concentra su dove viene applicata la sicurezza:

#### **A. Livello di Rete: IPSec**
Protegge tutto il traffico tra due host o due reti (VPN).
* **Protocollo ESP:** Fornisce confidenzialità (cifra il pacchetto) e autenticazione.
* **Modalità Transport:** Protegge solo il carico (payload) del pacchetto IP.
* **Modalità Tunnel:** Protegge l'intero pacchetto IP originale (usato nelle VPN).



#### **B. Livello di Trasporto: SSL/TLS**
È il cuore dell'**HTTPS**. Protegge la comunicazione tra il browser e il server.
1. **Handshake:** Il client e il server si scambiano i certificati e decidono una chiave segreta comune (usando RSA o Diffie-Hellman).
2. **Cifratura Record:** Una volta stabilita la chiave, i dati vengono cifrati con algoritmi veloci (Simmetrici come AES).



#### **C. Livello Applicazione: PGP**
* **Pretty Good Privacy (PGP):** Usato principalmente per la sicurezza delle e-mail. Permette di firmare e cifrare messaggi in modo che solo il destinatario possa leggerli.

---

### 💳 3. Transazioni Sicure: SET (Lezione 16)
Il protocollo **SET (Secure Electronic Transaction)** è stato progettato per i pagamenti con carta di credito.
* **Punto chiave:** Il mercante non vede mai il numero di carta di credito del cliente; solo la banca può decifrare quelle informazioni. Usa la "doppia firma" per garantire privacy e autenticità.

---

### 💻 Valore Aggiunto GitHub: Check-list di Sicurezza

| Protocollo | Livello Stack | Cosa protegge |
| :--- | :--- | :--- |
| **PGP / S/MIME** | Applicazione | E-mail e File |
| **SSL / TLS** | Trasporto | Sessioni Web (HTTPS) |
| **IPSec** | Rete | Intere connessioni (VPN) |

---
