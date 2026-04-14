# 🔑 Blocco 02: Crittografia Asimmetrica
## Lezioni 11 - 13

Mentre la crittografia simmetrica usa una sola chiave, qui ne usiamo due: una **Pubblica** (che tutti possono vedere) e una **Privata** (che solo il proprietario conosce).

---

### 🔓 1. Il Problema dello Scambio delle Chiavi (Lezione 11)
Il limite della crittografia simmetrica è: *come faccio a mandare la chiave al destinatario senza che un hacker la intercetti?*
La crittografia asimmetrica risolve questo problema.

* **Chiave Pubblica:** Serve per **CIFRARE**. Può essere distribuita a chiunque.
* **Chiave Privata:** Serve per **DECIFRARE**. Deve restare segreta e protetta.

> **Regola d'oro:** Quello che viene cifrato con la chiave pubblica può essere decifrato **solo** con la corrispondente chiave privata.



---

### 🧮 2. L'Algoritmo RSA (Lezione 12)
È l'algoritmo asimmetrico più usato. Si basa sulla difficoltà di fattorizzare numeri primi molto grandi.

**I 3 passaggi chiave per l'esame:**
1. Si scelgono due numeri primi enormi ($p$ e $q$).
2. Si calcola il loro prodotto $n = p \cdot q$ (che farà parte della chiave pubblica).
3. È facile calcolare $n$ da $p$ e $q$, ma è quasi impossibile fare il contrario per un computer.

---

### 🤝 3. Scambio di Chiavi Diffie-Hellman (Lezione 13)
Non serve per mandare messaggi, ma per **generare una chiave segreta comune** tra due persone che parlano su un canale pubblico.

* **La logica:** Alice e Bob mescolano una base comune con i propri segreti privati. Si scambiano il risultato e, rimescolando ancora, ottengono la stessa chiave finale senza averla mai spedita "in chiaro".



---

### ⚖️ Confronto: Simmetrica vs Asimmetrica

| Tipo | Velocità | Sicurezza Scambio Chiavi | Uso Principale |
| :--- | :--- | :--- | :--- |
| **Simmetrica** | Molto Veloce | Difficile | Cifratura di grandi file |
| **Asimmetrica** | Lenta | Molto Facile | Firma digitale e Login |

### 🧭 Navigazione
[🏠 Home Indice](../../README.md) |
