# Feladat címe: The full counting sort

## A feladat linkje: [The full counting sort](https://www.hackerrank.com/challenges/countingsort4/problem)

#### Leírás

> A feladat megoldásához a számláló rendezést kell használni az egész számokhoz társított karakterláncok listájának rendezéséhez.
> 
> Ha két karakterlánc ugyanahhoz az egész számhoz van társítva, akkor azokat az eredeti sorrendben kell kinyomtatni, azaz a rendezési algoritmusnak stabilnak kell lennie. 
>
> **Csavar**: a tömb első felében lévő karakterláncokat a `-` karakterrel kell helyettesíteni.

#### Konkrét példa

> Bemenet:
> 
> ```
> 20
> 0 ab
> 6 cd
> 0 ef
> 6 gh
> 4 ij
> 0 ab
> 6 cd
> 0 ef
> 6 gh
> 0 ij
> 4 that
> 3 be
> 0 to
> 1 be
> 5 question
> 1 or
> 2 not
> 4 is
> 2 to
> 4 the
> ```
> 
> Kimenet:
> 
> `- - - - - to be or not to be - that is the question - - - -`
> 
> Magyarázat:
> 
> ```
> 0 ab
> 0 ef
> 0 ab
> 0 ef
> 0 ij
> 0 to
> 1 be
> 1 or
> 2 not
> 2 to
> 3 be
> 4 ij
> 4 that
> 4 is
> 4 the
> 5 question
> 6 cd
> 6 gh
> 6 cd
> 6 gh
> ```
> 
> `sorted = [['-', '-', '-', '-', '-', 'to'], ['be', 'or'], ['not', 'to'], ['be'], ['-', 'that', 'is', 'the'], ['question'], ['-', '-', '-', '-'], [], [], [], []]`

#### Függvény
>
> A `countSort` függvénynek vissza kell adnia a rendezett stringet.
>
> A függvény a következő paraméterekkel rendelkezik:
>
> - Egy tömb, amely kéttagú tömbök épül fel. A beágyazott tömbnek az első fele egy szám és a második fele pedig egy string.
> - A következő sorok pedig a párokat tartalmazzák.
>
> ##### Input
>
> - A bemenet első sora egy egész szám, ami meghatározza a szám/string párok számát a tömbben.
>
> ##### Korlátok
>
> - 1 <= n <= 1000000, ahol n a darabszámot jelöli és páros szám
> - 1 <= |s| <= 10
> - 0 <= x < 100