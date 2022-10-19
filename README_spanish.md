# EuroCob
Calculador de las combinaciones del Euromillones, usando lo que conozco de probabilidades intento te reducir el número de combinaciones.

------------
## Características 🚀

### Combinaciónes
Usando [itertools](https://docs.python.org/3/library/itertools.html "itertools") calculo todas las combinaciones.

### Probabilidad
1. Elimino las combinaciones consecutivas
2. Elimino las combinaciones que todos los números sean pares e impares
3. Elimino las combinaciones que tengan una diferencia muy pequeña entre los números.

```
(k[3]+k[4])-(k[0]+k[1])=c
c/k[2]= x
x>*diferencia*
```

### Acciones
1. Combinaciones aleatorias

## Más a delante
- [x] Extraer de una web los números ganadores
   - [ ] Clasificar los números según veces que han salido
- [ ] Cribar combinaciones según la tabla de números obtenida anteriormente.

## ¿Cómo puedo apoyar esto?
Lo más fácil que puede hacer es darme una estrella.
Si tiene una sugerencia, bifurque la rama `master` y abra una Pull Request.
## ¡Gracias por leer!