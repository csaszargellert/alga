# Feladat megoldás:

1) **Rekurzív ellenőrzés alapja**:

Az `is_bst` függvény rekurzívan ellenőrzi, hogy egy adott csomópont értéke a megadott minimum és maximum érték közé esik-e:

`min_val < node.data < max_val`

A fa bal részfájának értékei nem lehetnek nagyobbak a jelenlegi csomópont adatánál, míg a jobb részfának értékei nem lehetnek kisebbek. Ezért a `min_val` és `max_val` dinamikusan frissül a bal és jobb részfák ellenőrzésénél.

2) **Üres fa kezelése**:

Ha a `csomópont/node` None, azaz a fa vége, akkor igaz értékkel tér vissza, mert egy üres fa mindig érvényes BST.

3) **A fa érvényessége**:

Ha az összes csomópont megfelel a BST tulajdonságoknak, az algoritmus `True` értéket ad vissza, ellenkező esetben `False`-t.

Ez garantálja a fa helyességének ellenőrzését a BST definíciója alapján.

4) **A feladat kiindulópontja**:

A `check_binary_search_tree_` függvény, ami a feladat által megadott függvény neve, az `is_bst` függvényt hívja meg a fa gyökércsomópontjával, és alapértelmezett értékkel indítja az ellenőrzést `-inf` és `inf` határok között.