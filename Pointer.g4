grammar Pointer;

// Reglas de gramática
start: instruction*;

instruction: selectPointer
           | advance
           | toggleDraw
           | rotate
           | lookAt
           | repeat;

selectPointer: 'select' INT;
advance: 'avanza' intVal (',' intVal)? ;
toggleDraw: 'dibuja' | 'desplaza';
rotate: 'rota' ('(' advance ')')? intVal (',' intVal)? ;
lookAt: 'mirar' 'a' INT;
repeat: 'repite' INT ':' instruction+;

// Tokens
intVal : '-'? INT ;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: ('-'? [0-9]+) | [0-9]+;
WS: [ \t\r\n]+ -> skip;
