# Reto3_PatronesDeDesbloqueo
Reto 3 para prueba de Alto nivel Python - Patrones de Desbloqueo (Unlock Patterns)

Descripción del reto
Este reto está inspirado en la funcionalidad de desbloqueo de dispositivos Android a través
de las combinaciones disponibles en la pantalla de bloqueo conectando los puntos sin
levantar el dedo de la pantalla
Debes desarrollar una función capaz de encontrar el número de combinaciones posibles
conectando los puntos disponibles.


Objetivo:
Deberás implementar una función que devuelva la cantidad de patrones posibles a partir de
un primer punto dado, que tienen una longitud determinada.
Los puntos a conectar serían:
| A | B | C |
| D | E | F |
| G | H | I |
La función contará con un primer parámetro de tipo caracter correspondiente al punto de la
cuadrícula (A, B, C, D, E, F, G, H o I).
La función contará con un segundo parámetro de tipo numérico correspondiente al número
de puntos que debe tener cada patrón.
Por ejemplo:
Por ejemplo, pasar los parámetros “C" y 2, debería devolver el número de patrones que
comienzan en 'C' y que tienen 2 conexión de dos puntos. El valor de retorno en este caso
sería 5, porque hay 5 patrones posibles:
(C -> B), (C -> D), (C -> E), (C -> F) y (C -> H).
No debe devolver los patrones en sí, solo el número de patrones posibles.
Reglas
● En un patrón, los puntos/puntos no se pueden repetir: solo se pueden usar una vez,
como máximo.
● En un patrón, dos puntos/puntos posteriores cualesquiera solo se pueden conectar
con líneas rectas directas de cualquiera de estas formas:
○ Horizontalmente: como (A -> B).
○ Verticalmente: como (D -> G).
○ Diagonalmente: como (I -> E), así como (B -> I).
● Pasando por encima de un punto entre ellos que ya ha sido 'usado': como (G -> C)
pasando por encima de E, en la imagen del patrón de ejemplo.
○ Esta es la regla más complicada. Normalmente, no podría conectar G con C,
porque E está entre ellos, sin embargo, cuando E ya se ha utilizado como
parte del patrón que está rastreando, puede conectar G con C pasando por
E, porque E se ignora, al haber sido usado.
