# ⚡ Blocco 03: Sistemi Lineari e Algoritmi
## Lezioni 11 - 15

In questo blocco impariamo a risolvere sistemi di $m$ equazioni in $n$ incognite utilizzando matrici e algoritmi deterministici.

---

## 🔢 1. Il Rango di una Matrice (Lezione 11)
Il **rango** ($rk(A)$) è il numero massimo di righe (o colonne) linearmente indipendenti.
* È fondamentale per capire quante soluzioni ha un sistema.
* Si calcola solitamente con l'algoritmo di Gauss (contando i pivot).

---

## 📐 2. Il Determinante (Lezioni 12-13)
Il determinante è un numero associato a una matrice **quadrata** che ne riassume le proprietà geometriche.

### Metodi di calcolo:
* **Matrici 2x2:** $ad - bc$.
* **Matrici 3x3 (Regola di Sarrus):** Si ricopiano le prime due colonne a destra e si sommano i prodotti delle diagonali principali meno quelle secondarie.
* **Matrici n x n (Teorema di Laplace):** Si sviluppa lungo una riga o colonna (preferibilmente quella con più zeri).

> **Proprietà d'oro:** Se $det(A) \neq 0$, la matrice è invertibile e il sistema ha una soluzione unica.



---

## 🚜 3. Algoritmo di Gauss (Lezioni 14-15)
È il metodo più potente per risolvere i sistemi. Trasforma la matrice in una forma **a scalini** (Upper Triangular).

**Operazioni consentite:**
1. Scambiare due righe.
2. Moltiplicare una riga per un numero $\neq 0$.
3. Sommare a una riga il multiplo di un'altra.



---

## 🏛️ 4. Teorema di Rouché-Capelli
Questo teorema ti dice SE il sistema ha soluzioni prima ancora di calcolarle.
Dato un sistema $Ax = b$:

1. Se $rk(A) \neq rk(A|b)$ ➡️ **Incompatibile** (0 soluzioni).
2. Se $rk(A) = rk(A|b) = n$ (numero incognite) ➡️ **Determinato** (1 soluzione).
3. Se $rk(A) = rk(A|b) < n$ ➡️ **Indeterminato** ($\infty$ soluzioni).

---


---
[🏠 Home Indice](../../README.md)

## 💻 Valore Aggiunto: Script di Verifica (Python)

```python
import numpy as np

# Inserisci qui la tua matrice dell'esercizio
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

# Calcolo del Rango
rango = np.linalg.matrix_rank(A)

# Calcolo del Determinante
det = np.linalg.det(A)

print(f"Rango: {rango}")
print(f"Determinante: {round(det, 2)}")
