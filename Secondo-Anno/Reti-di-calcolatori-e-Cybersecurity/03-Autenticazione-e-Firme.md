# ✍️ Blocco 03: Hash, MAC e Firme Digitali
## Lezioni 14 - 19

In questo blocco studiamo come garantire che un dato sia autentico e integro.

---

### 🌪️ 1. Funzioni Hash (Lezioni 14-15)
Una funzione Hash prende un testo di lunghezza qualsiasi e lo trasforma in un'impronta digitale fissa (es. 256 bit).

**Proprietà fondamentali per l'esame:**
* **Resistenza alla pre-immagine:** Dato un hash, è impossibile risalire al testo originale.
* **Resistenza alle collisioni:** È quasi impossibile trovare due testi diversi che producano lo stesso hash.

> **Esempi:** MD5 (insicuro), SHA-256 (standard attuale), SHA-512.

---

### 🔐 2. MAC e HMAC (Lezione 16)
Il **MAC (Message Authentication Code)** è un hash che richiede una **chiave segreta condivisa**.
* A cosa serve? Garantisce sia l'integrità che l'autenticità. Se l'hacker non ha la chiave, non può ricalcolare il MAC corretto dopo aver modificato il file.



---

### 🖋️ 3. La Firma Digitale (Lezioni 17-18)
La firma digitale usa la **crittografia asimmetrica** al contrario.

1. **Creazione:** Il mittente crea l'hash del messaggio e lo cifra con la propria **Chiave Privata**.
2. **Verifica:** Il destinatario decifra la firma con la **Chiave Pubblica** del mittente e confronta l'hash ottenuto con quello calcolato da lui.

> **Differenza Cruciale:**
> - Cifratura: Uso chiave pubblica del destinatario (per segretezza).
> - Firma: Uso mia chiave privata (per autenticità).



---

### 📜 4. Certificati Digitali e CA (Lezione 19)
Come faccio a sapere che la chiave pubblica di "Alice" appartiene davvero ad lei?
Interviene un terzo fidato: la **Certification Authority (CA)**, che emette un certificato (Standard X.509) che lega l'identità di una persona alla sua chiave pubblica.

### 🧭 Navigazione
[🏠 Home Indice](../../README.md) |  [➡️ Prossimo:Minacce, Network Security e Blockchain](04-Minacce-Forensics-Blockchain.md)


