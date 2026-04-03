# Asociatividad-Precedencia

**INTRODUCCION**

Este proyecto muestra cómo diseñar gramáticas no ambiguas para procesar expresiones matemáticas y lógicas. El objetivo es controlar el orden de las operaciones mediante la estructura de las reglas (estratificación), asegurando que el código se interprete correctamente.

Utilizo Lark en Python para construir el analizador y Graphviz para generar los árboles de derivación. Estos diagramas permiten ver cómo los operadores de mayor prioridad se "hunden" en la base del árbol, mientras que la recursividad (izquierda o derecha) define cómo se agrupan los datos.

**COMO EJECUTARLO**

PASO 1-Instalacion de la libreria utilizada. Es necesario tener instalado Python 3.x y el software Graphviz en el sistema. Puedes instalar las dependencias de Python con el siguiente comando:

```bash
  pip install lark pydot
```

PASO 2-ejecutar el programa

```bash
python3 COMPARACION.py
```

**DESCRIPCION DEL CODIGO**

El proyecto usa una técnica llamada estratificación, que consiste en organizar la gramática en capas. Esto permite que el analizador sepa exactamente qué operación va primero: los operadores de mayor prioridad se colocan en las reglas más profundas, mientras que los de menor prioridad se quedan cerca del inicio.

Para el procesamiento, el script utiliza Lark con un análisis ascendente. La dirección en la que la regla se llama a sí misma (recursividad) es la que define la asociatividad: si se llama por la izquierda, los datos se agrupan en ese orden, y si lo hace por la derecha, se agrupan hacia el final, como ocurre con la potencia.

Finalmente, el código convierte estos procesos internos en imágenes PNG usando Graphviz. Estos árboles visuales son la prueba de que la gramática no es ambigua y que el compilador está interpretando la jerarquía y el agrupamiento de los operadores tal como se planeó.

**RESULTADOS Y PRUEBAS**

**Ejecucion en consola**

