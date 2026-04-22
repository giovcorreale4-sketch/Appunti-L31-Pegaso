# 🌐 Reti Blocco 01: Fondamenti e Architettura
## Lezioni 1 - 8

In questo blocco analizziamo come è costruita la rete Internet e quali sono le metriche per misurarne le prestazioni.

---

### 🏛️ 1. Cos'è Internet? (Lezioni 1-2)
Internet è una "Rete di reti" basata sulla commutazione di pacchetto.
* **Edge (Bordo):** Host, client e server che eseguono applicazioni.
* **Core (Nucleo):** I router che collegano le reti tra loro.
* **Mezzi Trasmissivi:** - Guidati: Doppino (Ethernet), Fibra Ottica, Cavo Coassiale.
    - Non guidati: Onde radio (Wi-Fi, Bluetooth), Satelliti.

---

### ⏱️ 2. Prestazioni: Ritardi e Perdite (Lezioni 3-5)
I dati non viaggiano istantaneamente. Il ritardo totale è la somma di 4 componenti:

1. **Ritardo di Elaborazione (Nodal Processing):** Tempo per controllare gli errori nell'header.
2. **Ritardo di Accodamento (Queuing):** Tempo di attesa nel buffer del router (causa di congestione).
3. **Ritardo di Trasmissione:** Tempo per "spingere" i bit sul canale $d_{trans} = \frac{L}{R}$ dove $L$ è la lunghezza del pacchetto e $R$ la velocità del link).
4. **Ritardo di Propagazione:** Tempo fisico del segnale nel mezzo ($d_{prop} = \frac{d}{s}$, distanza/velocità).



---

### 🧱 3. Architettura a Livelli (Lezioni 7-8)
L'informatica usa i livelli per gestire la complessità. Ogni livello offre un servizio a quello superiore.

| Livello (Stack TCP/IP) | Funzione Principale | Unità di Dati (PDU) |
| :--- | :--- | :--- |
| **Applicazione** | HTTP, DNS, SMTP | Messaggio |
| **Trasporto** | TCP (Affidabile), UDP | Segmento |
| **Rete** | Instradamento (IP) | Pacchetto / Datagramma |
| **Link** | Trasferimento tra nodi vicini | Frame |
| **Fisico** | Trasmissione bit su cavo | Bit |

---

### 📦 4. Incapsulamento
Quando invii un dato, esso scende lo stack e ogni livello aggiunge un **Header** (intestazione) con le informazioni di controllo. Quando arriva a destinazione, lo stack viene risalito e gli header rimossi.

---

### 💻 Laboratorio nel Terminale:

1. **Test della Latenza:** Digita `ping google.com.` Il valore che leggerai come RTT (Round Trip Time) indica quanti millisecondi impiega un pacchetto di dati a fare il "giro completo": dalla tua tastiera ai server di Google e ritorno.
2. **Tracciamento del Percorso:** `Digita tracert google.com.` Qui vedrai i "salti" (hop) che fa il tuo pacchetto: ogni riga è un router diverso che i tuoi dati attraversano prima di raggiungere la destinazione finale.
---

### 🧭 Navigazione
[🏠 Home Indice](../../README.md) |

