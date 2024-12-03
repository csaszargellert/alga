# Megoldás menete

1) **Segédtömb létrehozása**:

A `createHelperArray` függvény egy olyan listát készít, amely adott számú üres listát tartalmaz. 
Ez a segédtömb a rendezés során a különböző indexekhez tartozó elemek tárolására szolgál.

2) **Maximális index meghatározása**:
 
A `getMaxIndex` függvény megkeresi az arr első oszlopában található maximális értéket.
Ez azért szükséges, hogy a segédtömb méretét megfelelően lehessen meghatározni.

3) **A megoldás tárolása**:

Végigiterálunk a 2D-s bemeneti tömbön, és a feladatleírás értelmében ha az eredeti sorrendet figyelembe vesszük, és az iterált elem az első felében található, akkor a "-" karakter kerül az a segédtömbbe. Ha az elem a második felében van, akkor az eredeti string második oszlopa kerül a segédtömbbe.

4) **Sík lista létrehozása**:

Mivel a segédtömb 2D-s, ezért ki kell nyújtani, hogy 1D-s legyen. Ezt a következő kódrészlet mutatja:

```python
flatten_array = []
    for item in helper_array:
        flatten_array.extend(item)
```