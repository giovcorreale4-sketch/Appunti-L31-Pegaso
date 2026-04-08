# 📐 Blocco 02: Spazi Vettoriali e Basi
## Lezioni 5 - 10

In questo blocco passiamo dal calcolo meccanico alla struttura geometrica dei dati.

---

## 🌌 1. Cos'è uno Spazio Vettoriale? (Lezioni 5-6)
Non è solo "frecce". È un insieme $V$ dove puoi sommare elementi e moltiplicarli per un numero (scalare) senza mai uscire dall'insieme.

### Sottospazi Vettoriali
Un sottoinsieme $W$ è un sottospazio se:
1. Contiene lo **zero** ($\vec{0}$).
2. È chiuso rispetto alla somma ($u + v \in W$).
3. È chiuso rispetto al prodotto ($k \cdot u \in W$).

---

## 🔗 2. Combinazioni e Indipendenza (Lezioni 7-8)
Questo è il concetto più importante per l'esame.

* **Combinazione Lineare:** Sommare vettori moltiplicati per dei coefficienti ($a\vec{v_1} + b\vec{v_2} + \dots$).
* **Linearmente INDIPENDENTI:** Nessun vettore può essere scritto come combinazione degli altri. 
    > **Test pratico:** Metti i vettori in una matrice. Se il determinante è $\neq 0$, sono indipendenti.



---

## 🏗️ 3. Base e Dimensione (Lezioni 9-10)
Una **Base** è il "kit minimo" di vettori per costruire tutto lo spazio.

* **Base:** Un insieme di vettori che sono sia *Indipendenti* che *Generatori*.
* **Dimensione:** Il numero di vettori presenti nella base.
    * Es: Lo spazio $\mathbb{R}^3$ ha dimensione 3 (servono 3 coordinate: $x, y, z$).



---

## 🛠 Procedure d'Esame
1. **Verificare se un insieme è una Base:** - Conta i vettori (devono essere pari alla dimensione dello spazio).
   - Verifica l'indipendenza lineare (calcola il determinante).
2. **Trovare la Dimensione:** - È uguale al **rango** della matrice formata dai vettori.

---
[🏠 Home Indice](../../README.md)
