# Megoldás menete:

1) Bemeneti paraméter:

- `root`: a gyökérre mutató referencia
- `s`: a dekódolni kívánt string

2) Változók inicializálása

- `decoded_string`: ebben a változóban fogjuk eltárolni a dekódolt üzenetet.
- `current`: ez egy fa node-ja, ami mindig az adott iterációban egy gyereknode-ra mutat.

3) For ciklus:

```python
for char in s:
	if char == '0':
		current = current.left
	else:
		current = current.right

	if current.left is None and current.right is None:
		decoded_string += current.data
		current = root
```

Végigmegyünk a dekódolni kívánt stringen, és attól függően, hogy milyen értéket tartalmaz, döntjük el, hogy jobbra vagy balra indulunk el bejárni a fát.

Abban az esetben ha `0` az érték, balra megyünk, ha más (jelen esetben a másik érték csak `1` lehet), akkor meg jobbra indulunk el bejárni a fát.

Ahhoz hogy számon tudjuk tartani, melyik `node`-on vagyunk, az adott iterációban lévő karakter értékétől függően adjuk meg a `current` változónak a jobb vagy a baloldali `node` referenciáját.

Miután megtörtént a referenciaátadás, megnézzük, hogy ez a `current` node egy levél-e. Ezt úgy tudjuk leellenőrizni, hogy megvizsgáljuk van-e jobb, illetva baloldali gyereke.

Abban az esetben ha a `current` node egy levél, akkor a `node`-nak az értékét hozzáadjuk a dekódolni kívánt stringhez, és újrainicializáljuk a `current` változó refernciáját a root node-ra.

Ezt az eljárást addig folytatjuk, amíg végig nem értünk a dekódolni kívént stringen.