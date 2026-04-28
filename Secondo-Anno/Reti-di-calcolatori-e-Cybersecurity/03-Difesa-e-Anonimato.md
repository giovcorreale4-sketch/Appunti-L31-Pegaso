# 🕶️ Reti Blocco 03: Firewall e Comunicazioni Anonime
## Lezioni 17 - 19

In quest'ultima sezione vediamo come proteggere i confini di una rete e come navigare senza lasciare tracce.

---

### 🛡️ 1. Il Firewall (Lezione 17)
Il firewall è un dispositivo (hardware o software) che filtra il traffico tra una rete interna protetta e Internet.

#### **Tipologie di Firewall per l'esame:**
* **Packet Filter (Filtro di pacchetti):** Lavora a livello di Rete/Trasporto. Controlla Indirizzi IP e porte. È veloce ma "stupido" (non vede il contenuto dei dati).
* **Application Gateway (Proxy):** Lavora a livello Applicazione. Analizza il contenuto specifico (es. blocca siti web specifici o comandi FTP). È molto sicuro ma più lento.



---

### 🕵️ 2. Anonimato in Rete (Lezione 18)
Navigare "in incognito" sul browser non basta. Per il vero anonimato servono protocolli che nascondano il tuo indirizzo IP ai server e ai nodi intermedi.

* **Protocollo Crowds:** Gli utenti formano un "gruppo" (folla). Quando invii un messaggio, questo viene passato casualmente tra i membri del gruppo prima di uscire. Il destinatario vede il messaggio provenire dalla "folla", non da te.
* **Mix Networks:** Server che rimescolano i messaggi in arrivo e li rispediscono in ordine diverso per impedire l'analisi del traffico.

---

### 🧅 3. Tor e il Deep Web (Lezione 19)
Tor (*The Onion Router*) è l'evoluzione più famosa dei sistemi di anonimato.

* **Onion Routing (Cifratura a cipolla):** Il tuo messaggio è avvolto in vari strati di cifratura. Ogni nodo della rete Tor rimuove uno strato per scoprire l'indirizzo del nodo successivo, ma nessuno conosce mai contemporaneamente sia l'origine che la destinazione finale.
* **Deep Web:** Quella parte di Internet (circa il 90%) non indicizzata dai motori di ricerca (database privati, pagine protette).
* **Dark Web:** Una piccola sottosezione del Deep Web accessibile solo tramite software specifici come Tor, usata sia per scopi nobili (attivismo in regimi totalitari) che per attività illegali.



---

### 📊 Tabella Riassuntiva: Tipi di Web

| Nome | Accesso | Contenuto |
| :--- | :--- | :--- |
| **Surface Web** | Google, Bing, ecc. | Siti pubblici, Social, News |
| **Deep Web** | Credenziali o Link diretti | Email, Cloud, Database bancari |
| **Dark Web** | Software Tor / I2P | Forum anonimi, Market neri |

---
[🏠 Torna alla Home](../README.md)
