# 🦠 Blocco 04: Minacce, Network Security e Blockchain
## Lezioni 20 - 26

In quest'ultima parte analizziamo come i concetti di crittografia vengono applicati (o aggirati) nel mondo reale.

---

### 👾 1. Malware e Minacce (Lezioni 20-21)
Non tutti gli attacchi sono crittografici; molti sfruttano il codice malevolo.
* **Virus:** Richiede l'intervento umano per diffondersi (es. aprire un file).
* **Worm:** Si diffonde autonomamente sfruttando le vulnerabilità di rete.
* **Trojan:** Si maschera da software utile per ingannare l'utente.
* **Ransomware:** Cifra i dati dell'utente e chiede un riscatto (usa la crittografia contro la vittima).

---

### 🛡️ 2. Sicurezza nei Protocolli di Rete (Lezioni 22-23)
Come proteggiamo i dati mentre viaggiano?
* **IPSec:** Protegge le comunicazioni a livello di rete (Layer 3). Fondamentale per le VPN.
* **SSL/TLS:** Protegge il traffico web (HTTPS). Usa crittografia asimmetrica per scambiare una chiave simmetrica temporanea.
* **Firewall:** Barriera che filtra il traffico in entrata e uscita in base a regole di sicurezza.



---

### 🔍 3. Computer Forensics (Lezione 24)
La scienza di raccogliere prove digitali che abbiano valore legale.
* **Regola d'oro:** Non lavorare mai sul supporto originale. Si crea una **copia bit-a-bit** (immagine forense).
* **Integrità:** Si calcola l'Hash della copia per dimostrare in tribunale che i dati non sono stati alterati.

---

### ⛓️ 4. Blockchain e Bitcoin (Lezioni 25-26)
La Blockchain è un registro distribuito e immutabile che usa tutto ciò che abbiamo studiato:

1. **Hash:** Ogni blocco contiene l'hash del blocco precedente, creando una catena. Se modifichi un dato, rompi tutta la catena.
2. **Firma Digitale:** Le transazioni sono firmate asimmetricamente (solo il proprietario della chiave privata può spendere i propri Bitcoin).
3. **P2P:** Non esiste un server centrale; la sicurezza è garantita dalla rete.

---

### 🧭 Navigazione
[🏠 Home Indice](../../README.md) |



---
