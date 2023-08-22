# Información Repositorio

Encontrarás información sobre Python con conceptos que te ayudarán a dar un salto como desarrollador Python y sobretodo en pruebas de conceptos sobre este lenguaje.

Conoceremos conceptos como:

- Filosofía detrás de Python.

- Conjuntos (sets).

- Comprehensions (list y dict).

- Funciones.

- Módulos.

- Manejo de errores.

Todo esto nos permitirá mejorar nuestro código y hacerlo más eficiente, además de poder trabajar con errores de una manera más elegante.

## Zen de Python
1. Nuestro código debe ser fácil de leer y debemos priorizar la claridad sobre la complejidad.

2. El código siempre debe ser claro y explícito para evitar que el yo del futuro o nuestros compañeros no se confunda con la lectura de este.

3. La simplificad es mejor que la complejidad y esto se puede ver a la hora de mantener o depurar nuestro código.

4. Debemos manejar los errores de manera elegante y no silenciarlos.

5. Siempre elegir la solución más práctica.

6. Nuestro código siempre debe funcionar o mejor dicho, debe retornar resultados predecibles.

7. Priorizar las soluciones simples sobre las más complejas.

8. Es mejor algo que esté funcionando a algo perfecto, por eso siempre comienza implementando una solución tipo MVP para luego ir mejorando.

9. Siempre debes tomarte el tiempo de hacer las cosas correctamente y usar buenas prácticas sobre tu código.

## Conjuntos (sets)

Los conjuntos son una colección de elementos únicos, es decir, que no se repiten. Estos elementos deben ser **únicos**, es decir, que los valores nunca estarán duplciados, cabe mencionar que los conjuntos son **mutables**, puedes ser modificados y que los conjuntos no tienen orden, es decir, que no podemos acceder a sus elementos por medio de índices como lo hacemos con una lista en Python.

Si agregamos un valor duplicado a un conjunto, este no se agregará, ya que los conjuntos no permiten elementos duplicados pero esto no quiere decir que se generará un error, simplemente no se agregará. También podemos usar distintos tipos de datos en un conjunto o estructuras de datos como una lista o un dict.

### Modificando conjuntos

Al igual que las listas podemos usar distintas funciones para aplicar a nuestros sets.

- **add**: Agrega un elemento al conjunto.

- **remove**: Remueve un elemento del conjunto, si el elemento no existe, se genera un error (intentar manejar siempre este posible error).

- **discard**: Remueve un elemento del conjunto, si el elemento no existe, no se genera un error. Es más recomendado que **remove**

- **update**: Agrega varios elementos al conjunto.

- **clear**: Remueve todos los elementos del conjunto.

### Operaciones con conjuntos

- **union**: Devuelve un nuevo conjunto con todos los elementos que se encuentran en ambos conjuntos. Recuerda que si el elemento se encuentra duplicado en ambos conjuntos, solo se agregará una vez.

- **intersection**: Devuelve un nuevo conjunto con los elementos que se encuentran en ambos conjuntos.

- **difference**: Devuelve un nuevo conjunto con los elementos que **sólo** se encuentran en el primer conjunto pero que no se encuentran en el segundo, incluso segregando a los valores duplciados en ambos conjuntos.

- **symmetric_difference**: Devuelve un nuevo conjunto con los elementos que **no** se encuentran en ambos conjuntos.

### Conclusiones
Ya que sabes que existen los conjuntos y lo más importante, tenemos una nueva herramienta que nos facilitará la vida. Ahora debes estar preguntándote, cuando utilizar un set, una lista un diccionario o una tupla, bien acá tengo la respuesta:

- **Lista**: Cuando necesites almacenar elementos y estos no necesiten ser únicos.

- **Set**: Cuando necesites almacenar elementos y estos necesiten ser únicos.

- **Diccionario**: Cuando necesites almacenar elementos únicos pero asociándolos a una llave.

- **Tupla**: Cuando necesites almacenar elementos y estos no necesiten ser únicos pero no quieras que estos sean modificados.
