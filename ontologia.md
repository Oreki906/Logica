Conceptos y predicados
Predicado	    Significado
animal(x)   	    x es un animal
pelo(x)	            x tiene pelo
leche(x)	        x da leche a sus crías
cuatroPatas(x)	    x tiene cuatro patas
amigable(x)	        x es amigable
domestico(x)	    x es doméstico
mamifero(x) 	    x es mamífero
pezuñas(x)  	    x tiene pezuñas
cuerpoRobusto(x)	x tiene cuerpo robusto
pasto(x)	        x se alimenta principalmente de pasto
perro(x)        	x es perro
vaca(x)	            x es vaca
plumas(x)	        x tiene plumas
vuela(x)        	x vuela
huevos(x)       	x pone huevos
carne(x)	        x come carne
ave(x)	            x es un ave
carnivoro(x)    	x es carnívoro
ungulado(x)	        x es ungulado

Reglas 

1. pelo(x) → mamifero(x)
2. leche(x) → mamifero(x)
3. plumas(x) → ave(x)
4. vuela(x) ∧ huevos(x) → ave(x)
5. mamifero(x) ∧ carne(x) → carnivoro(x)
6. mamifero(x) ∧ pezuñas(x) → ungulado(x)
7. carnivoro(x) ∧ leonado(x) ∧ manchasOscuras(x) → guepardo(x)
8. carnivoro(x) ∧ leonado(x) ∧ manchasNegras(x) → tigre(x)
9. ungulado(x) ∧ cuelloLargo(x) ∧ manchasOscuras(x) → jirafa(x)
10. ungulado(x) ∧ rayasNegras(x) → cebra(x)
11. ave(x) ∧ nada(x) ∧ blancoNegro(x) → pingüino(x)
12. ave(x) ∧ vuelaMuyBien(x) → albatros(x)
13. pelo(x) ∧ cuatroPatas(x) ∧ amigable(x) → puedeSerPerro(x)
14. amigable(x) ∧ domestico(x) ∧ pelo(x) ∧ cuatroPatas(x) → perro(x)
15. mamifero(x) ∧ pezuñas(x) ∧ cuerpoRobusto(x) → puedeSerVaca(x)
16. cuatroPatas(x) ∧ pezuñas(x) ∧ pasto(x) → puedeSerVaca(x)