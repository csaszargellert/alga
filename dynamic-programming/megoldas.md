# Megoldás menete

A tömben található maximális részhalmaz összegét és a pozitív elemekből képzett legnagyobb részösszeget számolja ki. 

Az algoritmus két értéket ad vissza: a legnagyobb résztömb összegét és a legnagyobb pozitív részszekvenciát. 

1) A `maxSubarray` függvény bemenete egy `arr` nevű lista, amely egész számokat tartalmaz.
2) A `cur_sum` változó a jelenlegi részösszeget követi, míg a `max_sum` a legnagyobb összefüggő részlista összegét tárolja. 
3) Egy ciklus során, ha a `cur_sum` negatívvá válik, lenullázódik, hogy új potenciális `subarray` kezdődjön. 
4) A ciklus során folyamatosan frissül a `max_sum` a legnagyobb talált részösszegre.
5) A pozitív számokat hozzáadja a `max_subsequence` értékéhez, hogy a lehető legnagyobb, nem feltétlenül összefüggő szekvenciát számítsa ki. A ciklus végén a tömb legnagyobb értékét levonja, ha a teljes szekvencia nem negatív.
