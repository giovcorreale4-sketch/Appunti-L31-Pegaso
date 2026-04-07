# 🟦 Blocco 01: Insiemi e Algebra delle Matrici
## Lezioni 1 - 4

Questo blocco introduce gli strumenti base per gestire i dati in forma tabellare (matrici), fondamentali per la programmazione e la computer grafica.

---

## 📚 Lezione 1: Richiami di Teoria degli Insiemi
Gli insiemi sono la base logica di tutto. Per l'esame, focalizzati sul **Prodotto Cartesiano**, perché è quello che genera le coordinate dei vettori.

* **Insiemi Numerici:** $\mathbb{N}$ (Naturali), $\mathbb{Z}$ (Interi), $\mathbb{Q}$ (Razionali), $\mathbb{R}$ (Reali).
* **Prodotto Cartesiano ($A \times B$):** L'insieme delle coppie $(a, b)$. 
    > Esempio: $\mathbb{R}^2$ è il piano cartesiano (tutte le coppie di numeri reali).

---

## 🔲 Lezione 2: Definizione di Matrice
Una matrice $A \in \mathbb{R}^{m \times n}$ è un rettangolo di numeri con $m$ righe e $n$ colonne.

### Tipologie Speciali (Da sapere a memoria)
1. **Matrice Quadrata:** Righe = Colonne ($n \times n$).
2. **Matrice Identità ($I_n$):** Quadrata, con tutti $1$ sulla diagonale e $0$ altrove. È l'elemento neutro del prodotto (come l'1 nei numeri).
3. **Matrice Trasposta ($A^T$):** Si ottiene scambiando le righe con le colonne. 
    * *Proprietà:* $(A+B)^T = A^T + B^T$ e $(AB)^T = B^T A^T$ (attenzione all'ordine!).

---

## ➗ Lezioni 3-4: Operazioni tra Matrici
Qui iniziano i calcoli d'esame.

### 1. Somma ($A + B$)
* **Vincolo:** Le matrici devono avere le STESSE dimensioni.
* **Operazione:** Somma elemento per elemento ($a_{ij} + b_{ij}$).

### 2. Prodotto per uno Scalare ($k \cdot A$)
* Ogni numero della matrice viene moltiplicato per il numero reale $k$.

### 3. Prodotto Riga per Colonna ($A \cdot B$) ⭐️ FONDAMENTALE
* **Vincolo:** Il numero di colonne di $A$ deve essere uguale al numero di righe di $B$.
* **Dimensione Risultato:** Se $A$ è $(m \times p)$ e $B$ è $(p \times n)$, il risultato è $(m \times n)$.
* **Procedura:** L'elemento in posizione $(i, j)$ è la somma dei prodotti degli elementi della riga $i$ di $A$ per la colonna $j$ di $B$.



> **⚠️ ATTENZIONE:** Il prodotto tra matrici **NON è commutativo**. In generale, $A \cdot B \neq B \cdot A$. Se cambi l'ordine, cambi il risultato (o l'operazione diventa impossibile).



---

### 🧭 Navigazione
[🏠 Home Indice](../../README.md) | [➡️ Prossimo: Spazi Vettoriali (Lezioni 5-10)](02-Spazi-Vettoriali.md)
