# Feladat címe: The Maximum Subarray

## A feladat linkje: [The Maximum Subarray](https://www.hackerrank.com/challenges/maxsubarray/problem)

#### Leírás

> Adott egy tömb, a feladat megkereseni a lehetséges maximális összeget a következők közül:
> 
> - minden nem üres altömb.
> - minden nem üres részsorozat.
>
> A továbbiakban egy részsorozatot a következőképpen definiálunk, egy részsorozat egy tömb bármely részhalmaza.
> 
> A továbbiakban egy altömböt a következőképpen definiálunk, egy altömb egy tömb összefüggő részsorozata.
>
> A feladat célja az, hogy írassunk ki két értéket szóközzel elválasztott egész számként egy sorba.
>
> Figyelmbe kell venni, hogy az üres altömbök, alszekvenciák nem érvényesek.

#### Konkrét példa

> Addot egy tömb:
> ```arr = [-1, 2, 3, -4, 5, 10]```
>
> A maximum altömb összeg az 1-től 5-ig terjedő indexen lévő elemekből épül fel. Az összegük 2 + 3 + (-4) + 5 + 10 = 16
>
> A maximum részsorozat összeg az 1., 2., 4., 5. indexen lévő elemekből tevődik össze, és az összegük 2 + 3 + 5 + 10 = 20

#### Függvény
>
> A `maxSubarray` függvénynek vissza kell adnia egy tömböt két egész számmal úgy, hogy az első szám az altömb összegét, míg a második szám a részsorozat összegét kell reprezentálja.
>
> A függvény a következő paraméterekkel rendelkezik:
>
> - arr[N]: egy egész számokból álló tömb
>
> ##### Input
>
> - A bemenet első sora egyetlen egész számot tartalmaz, a tesztesetek száma.
> - Minden teszteset első sora egyetlen egész számot tartalmaz, ami a tömben lévő elemek számát reprezentálja.
> - A második sor szóközzel elválasztott egész számokat tartalmaz, ami a tömben lévő elemek lesznek.
>
> ##### Korlátok
>
> - 1 <= tesztesetek száma <= 10
> - 1 <= tömbben lévő elemek száma <= 10^5
> - -10^4 <= a tömbben lévő számok értéke <= 10^4
> - Az altömbnek és a részsorozatoknak legalább egy elemet kell tartalmazniuk.