# Control I: Lenguajes de Programación II – ICI425/INC415

Profesor: Alonso Inostrosa Psijas
Fecha de entrega: 26 de septiembre de 2023

-------------------------

Descripción del Desafío:

Se crea un programa capaz de generar un dibujo en un plano mediante una secuencia de instrucciones. Posteriormente, se representan estas instrucciones como un árbol de sintaxis abstracta al final del proceso.

Consideraciones:

Para este programa, se utiliza la versión 4.12.0 de Antlr4. Si bien esto no constituye un límite para su ejecución, si se emplea una versión diferente, pueden aparecer advertencias relacionadas con el uso de una versión distinta. Además, las librerías necesarias para ejecutar el programa de manera correcta se encuentran especificadas en el archivo 'requeriments.txt'

En este programa, se han definido puntos clave que se presentarán a continuación, incluyendo su ubicación y los nombres de los archivos correspondientes dentro del proyecto:
- Tokens: Archivos correspondientes "Pointer.tokens" y "PointerLexer.tokens".
- Expresiones Regulares y Gramática de Libre Contexto: Archivos correspondientes "PointerLexer.py" y "Pointer.g4".
- Interpretadores del lenguaje: Archivos correspondientes "Pointer.interp" y "PointerLexer.interp".
- Recopilador de instrucciones: Archivos correspondientes "PointerListener.py" y "PointerParser.py.

Dentro del proyecto, se encuentra un archivo que contiene los comandos que se pueden utilizar para llevar a cabo pruebas del mismo, dicho archivo se encuentra en la carpeta "Informacion" con el nombre "comandos.txt". Estos comandos deben ser escritos UNO A UNO, si no LAS INSTRUCCIONES NO SERÁN RECONOCIDAS.

Propuesta de solución:

Como solución, se presenta un programa que utiliza una cuadrícula de dimensiones 21x21. En esta cuadrícula, inicialmente se ubican tres colores diferentes: Rojo, Verde y Azul, representados como cuadrados o punteros con relleno del color correspondiente en el plano.

Cada color tiene tres características distintas:
- Rotación: La dirección hacia la cual se mueve el cuadrado pintado depende de la dirección hacia la cual apunta inicialmente, comenzando por apuntar hacia el este. Se puede cambiar la dirección de mira utilizando el comando "rota INT". El valor "INT" puede ser cualquier ángulo entre 1° y 360° en sentido antihorario.
- Desplazamiento: La dirección de movimiento del cuadrado pintado también depende de su dirección de mira, que se define mediante la rotación. Para avanzar, se utiliza el comando "avanza INT". El valor "INT" representa la cantidad de pasos a avanzar, también se puede utilizar "avanza INT,INT" para avanzar a un cuadro en especifico del plano.
- Dibujar: Para activar esta característica, se usa el comando "dibuja". Cuando está activada, el cuadrado pinta su propio color en las casillas que atraviesa mientras se desplaza. Por diseño, cuando el puntero está apuntando en diagonal, también pinta la casilla que se encuentra en la ruta hacia esa diagonal. Se puede desactivar esta característica utilizando el comando "desplaza". Así mismo, los trazos del dibujo tienen jerarquías; es decir, el puntero que se selecciona primero es el que se muestra por encima de los otros colores, en caso de que se decida pintar con otros colores sobre un mismo cuadro.

Para poder seleccionar un puntero, se utiliza la instrucción "select" la cual debe ir acompañada del ID del puntero que se quiera utilizar.

ID de los punteros:
- 1 Rojo
- 2 Verde
- 3 Azul
Esta solución proporciona una forma intuitiva de crear dibujos en el plano, permitiendo el control de la dirección, el desplazamiento y la capacidad de pintar utilizando colores definidos en la cuadrícula.

Gramática Generada:

La gramática generada abarca las palabras y expresiones permitidas en el programa, que a su vez comprenden varios símbolos autorizados para ejecutar las instrucciones a través de la consola y así crear nuestro dibujo.

Tokens:
- intVal: '-'? INT
- ID: [a-zA-Z_][a-zA-Z0-9_]*
- INT: ('-'? [0-9]+) | [0-9]+
- WS: [ \t\r\n]+ -> skip

Instrucciones permitidas:
- select 
- avanza 
- dibuja
- desplaza
- rota 
- mirar 
- repite 

Reglas de la gramática:
- select INT (puntero identificador de cuadro de color)
- avanza intVal(',' intVal)?
- dibuja
- desplaza
- rota ('(' advance ')')? intVal (',' intVal)?
- mirar a INT
- repite INT: instrucciones+

---------------------------------------------------------------------

Colaboradores:
- [Kevin Alejandro Diaz Cantillano](https://github.com/ixyz022)
- [Ashly Yamilet Mazuela Ávalos](https://github.com/ashlyMazuela)
- [Benjamín Alexander Zárate Chacana](https://github.com/ZarateBenjamin)
