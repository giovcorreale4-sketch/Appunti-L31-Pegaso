# 🔄 Blocco 04: Applicazioni Lineari e Matrici Associate
## Lezioni 16 - 19

Le applicazioni lineari sono funzioni tra spazi vettoriali che conservano le operazioni di somma e prodotto per uno scalare.

---

## 🎭 1. Cos'è un'Applicazione Lineare? (Lezione 16)
Una funzione $f: V \to W$ è lineare se:
1. $f(u + v) = f(u) + f(v)$ (Additività)
2. $f(k \cdot v) = k \cdot f(v)$ (Omogeneità)

In pratica, un'applicazione lineare può sempre essere rappresentata da una **matrice**. Moltiplicare un vettore per una matrice significa applicare quella funzione.

---

## 🕳️ 2. Nucleo (Ker) e Immagine (Im) (Lezione 17)
Questi due concetti sono fondamentali per capire come "lavora" la funzione.

* **Nucleo (Kernel - $Ker(f)$):** È l'insieme dei vettori di $V$ che vengono "schiacciati" nello zero di $W$.
    * *Cosa indica:* Se il Nucleo contiene solo lo zero, la funzione è **iniettiva**.
* **Immagine ($Im(f)$):** È l'insieme di tutti i possibili risultati della funzione in $W$.
    * *Cosa indica:* Se la dimensione dell'Immagine è pari alla dimensione di $W$, la funzione è **suriettiva**.



---

## 📐 3. Teorema della Dimensione (Lezione 18)
Conosciuto anche come Teorema del Rango e della Nullità. Lega le dimensioni degli spazi:

$$dim(V) = dim(Ker(f)) + dim(Im(f))$$

> **💡 Utilità d'esame:** Se conosci la dimensione dello spazio di partenza e trovi il rango della matrice (dimensione dell'immagine), ricavi subito la dimensione del nucleo per sottrazione.

---

## 📋 4. Matrice Associata (Lezione 19)
Ogni applicazione lineare dipende dalle basi scelte per $V$ e $W$. Cambiando le basi, cambia la matrice, anche se la funzione resta la stessa.

* **Matrice di Passaggio:** Serve per trasformare le coordinate di un vettore da una base $B$ a una base $B'$.



---

## 💻 Valore Aggiunto: Calcolo di Ker e Im (Python)
> In un esame, trovare una base per il Nucleo significa risolvere il sistema omogeneo $Ax = 0$. Ecco come farlo velocemente per verifica:

---
[🏠 Home Indice](../../README.md)

```python
import numpy as np
from scipy.linalg import null_space

# Matrice associata all'applicazione
A = np.array([[1, 2], 
              [2, 4]])

# Trova il Nucleo (Kernel)
ker = null_space(A)

# Trova la dimensione dell'Immagine (Rango)
im_dim = np.linalg.matrix_rank(A)

print(f"Base del Nucleo:\n{ker}")
print(f"Dimensione Immagine (Rango): {im_dim}")
