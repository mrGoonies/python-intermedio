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


## Comprehension
Es una forma práctica y simple de crear estructuras de datos como listas o diccionarios.

Es altamente recomendado utilizar este tipo de característica que nos entrega Python, ya que nos permite escribir menos código y hacerlo de una manera más legible, además cumplimos con el **zen** principios de Python.

## Funciones
Las funciones permiten modularizar nuestro código o en palabras más simples, reutilizar funcionalidades específicas en distintas partes de nuestro código. Es recomendable entender que las funciones deben ser pequeñas y realizar una sola tarea, esto nos permitirá tener un código más limpio y fácil de mantener. En Python podemos asignar valores por defecto a los argumentos de una función, esto nos permite evitar errores, aunque siempre será mejor manejar los errores de manera elegante por medio de un **try/except**. Siempre que queramos varios valores de una funcion, estos valores sera retornados en una tupla, por lo que debemos asignarlos a una variable para poder acceder a ellos.

### Scope
El scope o ámbito de una variable es el alcance que tiene esta dentro de nuestro código, es decir, en que partes de nuestro código podemos acceder a esta variable. En Python existen dos tipos de scope:

1. **Global**: Las variables globales son aquellas que se pueden acceder desde cualquier parte de nuestro código, es decir, que su alcance es global.

2. **Local**: Las variables locales son aquellas que se pueden acceder sólo desde una parte específica de nuestro código, es decir, que su alcance es local.


### lambda functions
Las funciones lambda son funciones anónimas, es decir, que no tienen un nombre y se utilizan para realizar una tarea muy específica. Estas funciones son muy útiles cuando necesitamos pasar una función como argumento a otra función, por ejemplo, cuando queremos ordenar una lista por medio de un criterio específico.

### High order functions (HOF)
Las funciones de orden superior son aquellas que reciben como argumento a otra función o que retornan una función como resultado. Esto permite que nuestro código sea más declarativo y expresivo, además de permitirnos reutilizar código. Los principales beneficios son:

1. **Facilitan la lectura del código**.
2. **Utilizamos un paradigma declarativo** en vez de un paradigma imperativo. Nos centramos en decirle a la computadora que hacer en vez de centrarnos en como hacerlo.
3. **Reducción de código repetido**. Creamos una función de orden superior que recibe como argumento una función y esta función se encarga de ejecutar la función que recibe como argumento. Podemos ver a una función de orden superior como un validador de funciones.

Es importante (como todo en la programación) no abusar de las funciones de orden superior, ya que esto puede generar un código difícil de leer y mantener.

**¿Cuáles son los mejores casos para implementar este tipo de funciones?**
1. Filtrado de datos.
2. Transformaación de datos.
3. Operaciones de reducción.
4. Callbacks y eventos.
5. Implementación de patrones de diseño como *Observe* o *Strategy*
6. Operaciones en listas.
## Tips

1. Si quieres almacenar un valor que fué generado dentro de una función, debes retornarlo y asignarlo a una variable.

2. Agregar valores a los argumentos de una función es una mala práctica, ya que puede generar efectos secundarios.

3. Es buena practica que las variables globales sean constantes, es decir, que no cambien su valor. Y si queremos modificar variables globales, debemos hacerlo por medio de una función.


