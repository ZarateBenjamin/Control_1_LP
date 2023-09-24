import pygame
import sys
import time
import math
from pygame.math import Vector2
from antlr4 import *
from PointerLexer import PointerLexer
from PointerParser import PointerParser
from antlr4.tree.Trees import Trees
import tkinter as tk
from tkinter import ttk

#Lista para almacenar las celdas con los colores cambiados
colored_cells = {}

# Lista para almacenar todas las instrucciones ingresadas
all_instructions = []

# Lista para almacenar los árboles léxicos de las instrucciones ingresadas
lexical_trees = []

class POINTER:
    def __init__(self, id, color, initial_position):
        self.id = id
        self.x, self.y = initial_position
        self.pos = Vector2(self.x, self.y)
        self.color = color
        self.angle = 0
        self.drawing = False
        self.trail_color = None
        self.trail = []  # Lista para almacenar las posiciones anteriores del puntero
        self.trail_color_positions = []  # Lista para almacenar las posiciones por donde pasa el puntero
        self.colored_cells = {}  # Diccionario para rastrear celdas coloreadas (x, y) -> color

    def draw_pointer(self):
        pointer_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, self.color, pointer_rect)
        # Dibuja una línea que indica la dirección del puntero (del mismo tamaño que el cuadrado del puntero)
        center = self.pos * cell_size + Vector2(cell_size / 2, cell_size / 2)
        endpoint = center + Vector2(1, 0).rotate(-self.angle) * (cell_size / 2)
        pygame.draw.line(screen, (0, 0, 0), center, endpoint, 3)

    def rotate(self, degrees):
        # Actualiza el ángulo
        self.angle += degrees

    def update_trail(self):
        if self.drawing:
            self.trail.append(self.pos.copy())

    def draw_trail(self, screen, cell_size):
        if self.drawing and len(self.trail) > 1:
            for pos in self.trail:
                # Calcula la posición actual del trazo desde el centro del POINTER
                x, y = int(pos.x), int(pos.y)
                if 0 <= x < cell_number and 0 <= y < cell_number:
                    # Asegúrate de que la posición esté dentro del rango del tablero
                    colored_cells[(x, y)] = self.trail_color
                    screen.fill(self.trail_color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))


def draw_grid_numbers(screen, cell_size, cell_number):
    font = pygame.font.Font(None, 18)  # Reducir el tamaño de la fuente a 24 puntos
    for x in range(cell_number):
        for y in range(cell_number):
            text = font.render(f'{x},{y}', True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2)
            screen.blit(text, text_rect)


def execute_instruction(instruction):
    global pointers, selected_pointer
    repeat_count = 1  # Número de repeticiones por defecto
    if instruction[0] == "select":
        selected_pointer = int(instruction[1])
    elif instruction[0] == "avanza":
        # Verificando si la instrucción es del tipo "avanza INT"
        if len(instruction) == 3:
            distance = int(instruction[1])
            direction = Vector2(1, 0).rotate(-pointers[selected_pointer - 1].angle)
            for _ in range(distance):
                pointers[selected_pointer - 1].pos += direction
                pointers[selected_pointer - 1].update_trail()  # Registrar la posición
                # Verificando si la instrucción es del tipo "avanza INT,INT"
        elif len(instruction) == 5 and instruction[2] == ",":
            # Obtén la posición objetivo
            target_pos = Vector2(int(instruction[1]), int(instruction[3]))

            # Calcula la dirección desde la posición actual del puntero hasta la posición objetivo
            direction = target_pos - pointers[selected_pointer - 1].pos

            # Ajusta el ángulo del puntero basado en la dirección del movimiento
            angle = math.degrees(math.atan2(-direction.y, direction.x))

            # Asegúrate de que el ángulo esté en el rango [0, 360)
            angle %= 360

            # Actualiza el ángulo del puntero
            pointers[selected_pointer - 1].angle = angle
            # Redibuja la pantalla para mostrar la nueva orientación del puntero
            screen.fill((60, 60, 60))
            draw_grid_numbers(screen, cell_size, cell_number)
            for pointer in pointers:
                pointer.draw_pointer() 
                pointer.draw_trail(screen, cell_size)  
            pygame.display.update()
            # Espera 0,5 segundos
            time.sleep(0.5)
            # Mueve el puntero a la posición objetivo
            pointers[selected_pointer - 1].pos = target_pos
            pointers[selected_pointer - 1].update_trail()  # Registrar la posición
        # Si no se cumple ninguno de los dos formatos, imprimir un error.
        else:
            print("Formato de instrucción avanza incorrecto.")
    elif instruction[0] == "rota":
        if len(instruction) == 3:
            # Si la instrucción es del tipo "rota INT" (rotación por ángulo en grados)
            degrees = int(instruction[1])
            if 1 <= selected_pointer <= len(pointers):
                pointers[selected_pointer - 1].rotate(degrees)
        elif len(instruction) == 5 and instruction[2] == ",":
            # Si la instrucción es del tipo "rota INT,INT" (rotación hacia una coordenada)
            target_pos = Vector2(int(instruction[1]), int(instruction[3]))

            # Calcula la dirección desde la posición actual del puntero hasta la posición objetivo
            direction = target_pos - pointers[selected_pointer - 1].pos

            # Ajusta el ángulo del puntero basado en la dirección del movimiento
            angle = math.degrees(math.atan2(-direction.y, direction.x))

            # Asegúrate de que el ángulo esté en el rango [0, 360)
            angle %= 360

            # Actualiza el ángulo del puntero
            pointers[selected_pointer - 1].angle = angle
            # Redibuja la pantalla para mostrar la nueva orientación del puntero
            screen.fill((60, 60, 60))
            draw_grid_numbers(screen, cell_size, cell_number)
            for pointer in pointers:
                pointer.draw_pointer() 
                pointer.draw_trail(screen, cell_size)  
            pygame.display.update()
        # Verifica si la longitud de la instrucción es 11, 9 o 7 y si cumple con el formato esperado
        if (len(instruction) == 11 or len(instruction) == 9 or len(instruction) == 7) and instruction[1] == "(" and instruction[5].isdigit():
            if len(instruction) == 11:
                #avanza int,int
                #rota (avanza X,Y)Z,Z
                target_pos = Vector2(int(instruction[3]), int(instruction[5]))
                direction = target_pos - pointers[selected_pointer - 1].pos
                angle = math.degrees(math.atan2(-direction.y, direction.x))
                angle %= 360
                pointers[selected_pointer - 1].angle = angle
                screen.fill((60, 60, 60))
                draw_grid_numbers(screen, cell_size, cell_number)
                for pointer in pointers:
                    pointer.draw_pointer() 
                    pointer.draw_trail(screen, cell_size)  
                pygame.display.update()
                time.sleep(0.5)
                pointers[selected_pointer - 1].pos = target_pos
                pointers[selected_pointer - 1].update_trail()  # Registrar la posición
                #
                #rota int,int
                target_pos = Vector2(int(instruction[7]), int(instruction[9]))
                direction = target_pos - pointers[selected_pointer - 1].pos
                angle = math.degrees(math.atan2(-direction.y, direction.x))
                angle %= 360
                pointers[selected_pointer - 1].angle = angle
                screen.fill((60, 60, 60))
                draw_grid_numbers(screen, cell_size, cell_number)
                for pointer in pointers:
                    pointer.draw_pointer() 
                    pointer.draw_trail(screen, cell_size)  
                pygame.display.update()
                #
                selected_pointer = 1 
                #rota (avanza X,Y)Z,Z
            elif len(instruction) == 9 and ')' in instruction[4]:
                #rota (avanza X)Z,Z
                #avanza int
                distance = int(instruction[3])
                direction = Vector2(1, 0).rotate(-pointers[selected_pointer - 1].angle)
                for _ in range(distance):
                    pointers[selected_pointer - 1].pos += direction
                    pointers[selected_pointer - 1].update_trail()  # Registrar la posición                
                #
                #rota int,int
                target_pos = Vector2(int(instruction[5]), int(instruction[7]))
                direction = target_pos - pointers[selected_pointer - 1].pos
                angle = math.degrees(math.atan2(-direction.y, direction.x))
                angle %= 360
                pointers[selected_pointer - 1].angle = angle
                screen.fill((60, 60, 60))
                draw_grid_numbers(screen, cell_size, cell_number)
                for pointer in pointers:
                    pointer.draw_pointer() 
                    pointer.draw_trail(screen, cell_size)  
                pygame.display.update()
                #
                #rota (avanza X)Z,Z                                
            elif len(instruction) == 9 and ',' in instruction[4]:
                #avanza int,int
                #rota (avanza X,Y)Z
                target_pos = Vector2(int(instruction[3]), int(instruction[5]))
                direction = target_pos - pointers[selected_pointer - 1].pos
                angle = math.degrees(math.atan2(-direction.y, direction.x))
                angle %= 360
                pointers[selected_pointer - 1].angle = angle
                screen.fill((60, 60, 60))
                draw_grid_numbers(screen, cell_size, cell_number)
                for pointer in pointers:
                    pointer.draw_pointer() 
                    pointer.draw_trail(screen, cell_size)  
                pygame.display.update()
                time.sleep(0.5)
                pointers[selected_pointer - 1].pos = target_pos
                pointers[selected_pointer - 1].update_trail()  # Registrar la posición
                #
                #  rota int              
                degrees = int(instruction[7])
                if 1 <= selected_pointer <= len(pointers):
                    pointers[selected_pointer - 1].rotate(degrees)
                selected_pointer = 1  
                #
                #rota (avanza X,Y)Z               
            elif len(instruction) == 7:
                #rota (avanza X)Z
                #avanza int
                distance = int(instruction[3])
                direction = Vector2(1, 0).rotate(-pointers[selected_pointer - 1].angle)
                for _ in range(distance):
                    pointers[selected_pointer - 1].pos += direction
                    pointers[selected_pointer - 1].update_trail()  # Registrar la posición
                #
                #rota int
                degrees = int(instruction[5])
                if 1 <= selected_pointer <= len(pointers):
                    pointers[selected_pointer - 1].rotate(degrees)
                selected_pointer = 1  
                #
                #rota (avanza X)Z
    elif instruction[0] == "mira":
        if len(instruction) == 3 and instruction[1] == 'a':
            target_id = int(instruction[2])
            target_pointer = None
            for pointer in pointers:
                if pointer.id == target_id:
                    target_pointer = pointer
                    break
            if target_pointer is not None:
                direction = target_pointer.pos - pointers[selected_pointer - 1].pos
                pointers[selected_pointer - 1].angle = -direction.angle_to(Vector2(1, 0))
            else:
                print(f"Puntero con ID '{target_id}' no encontrado.")
    elif instruction[0] == "dibuja":
        if 1 <= selected_pointer <= len(pointers):
            pointers[selected_pointer - 1].drawing = True
            pointers[selected_pointer - 1].trail_color = pointers[selected_pointer - 1].color
    elif instruction[0] == "desplaza":
        if 1 <= selected_pointer <= len(pointers):
            pointers[selected_pointer - 1].drawing = False
            if pointers[selected_pointer - 1].trail_color is not None:
                # Conservar el color en colored_cells si trail_color no es None
                for pos in pointers[selected_pointer - 1].trail_color_positions:
                    pointers[selected_pointer - 1].colored_cells[pos] = pointers[selected_pointer - 1].trail_color
    elif instruction[0] == "repite":
        repeat_count = int(instruction[1])
        repeat_instruction = instruction[3:]  # Eliminar el contador de repeticiones
        for _ in range(repeat_count):
            pygame.display.flip()
            execute_instruction(repeat_instruction)



# Función para mostrar el árbol léxico
def print_lexical_tree(input_str, tree_view):
    input_stream = InputStream(input_str)
    lexer = PointerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PointerParser(token_stream)
    tree = parser.start()

    tree_str = Trees.toStringTree(tree, None, parser)
    tree_view.insert("", "end", text=tree_str)


# Función para mostrar la ventana con árboles léxicos
def show_lexical_trees():
    root = tk.Tk()
    root.title("Árboles Léxicos")

    tree_frame = ttk.Frame(root)
    tree_frame.pack(fill=tk.BOTH, expand=True)

    tree_label = ttk.Label(tree_frame, text="Árboles Léxicos:")
    tree_label.pack()

    tree_view = ttk.Treeview(tree_frame)
    tree_view.pack(fill=tk.BOTH, expand=True)

    for idx, instruction in enumerate(all_instructions, start=1):
        print(f"Instrucción {idx}: {instruction}")
        print_lexical_tree(instruction, tree_view)
        print("\n")

        # Agregar un botón para cerrar la ventana
    close_button = ttk.Button(root, text="Cerrar", command=root.destroy)
    close_button.pack()

    # Hacer que la ventana se cierre automáticamente después de un tiempo 10 segundos)
    root.after(100000, root.destroy)

    root.mainloop()



if __name__ == "__main__":
    pygame.init()

    cell_size = 40
    cell_number = 21
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    clock = pygame.time.Clock()

    # Crear punteros con identificadores (id) y colores
    red_pointer = POINTER(1, (255, 0, 0), (3, 3))    # Puntero rojo con id 1 en (3, 3)
    green_pointer = POINTER(2, (0, 255, 0), (8, 5))  # Puntero verde con id 2 en (8, 5)
    blue_pointer = POINTER(3, (0, 0, 255), (1, 1))  # Puntero azul con id 3 en (12, 8)
    pointers = [red_pointer, green_pointer, blue_pointer]
    selected_pointer = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Al salir del "juego", mostrar el árbol léxico de todas las instrucciones
                show_lexical_trees()
                pygame.quit()
                sys.exit()

        screen.fill((60, 60, 60))

        draw_grid_numbers(screen, cell_size, cell_number)

        for pointer in pointers:
            pointer.draw_pointer()  # dibuja el puntero
            pointer.update_trail()  # registra la posición anterior del POINTER
            pointer.draw_trail(screen, cell_size)  # dibuja el trazo

        # Colorear celdas según colored_cells
        for cell, color in colored_cells.items():
            x, y = cell
            screen.fill(color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))

        pygame.display.update()
        clock.tick(60)

        # Lectura de instrucción desde el usuario
        instruction_str = input("Ingrese una instrucción (o 'salir' para salir): ").lower()

        if instruction_str == 'salir':
            # Al salir del "juego", mostrar el árbol léxico de todas las instrucciones
            show_lexical_trees()
            pygame.quit()
            sys.exit()
        else:
            # Almacenar la instrucción ingresada en la lista de todas las instrucciones
            all_instructions.append(instruction_str)

            # Analizar la instrucción ingresada utilizando ANTLR
            input_stream = InputStream(instruction_str)
            lexer = PointerLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = PointerParser(token_stream)

            try:
                tree = parser.start()
                # Obtener la lista de tokens en la instrucción
                tokens = [token.text for token in token_stream.tokens]

                # Ejecutar la instrucción
                execute_instruction(tokens)
            except Exception as e:
                print(f"Error léxico/sintáctico: {e}")



