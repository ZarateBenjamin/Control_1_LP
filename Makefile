# Variables
PYTHON = python3
PIP = pip3
REQUIREMENTS = requirements.txt

# Regla para instalar las dependencias
install:
    @echo "Instalando dependencias Python..."
    $(PIP) install -r $(REQUIREMENTS)
    
    @echo "Verificando si tkinter está instalado..."
    if ! dpkg -l | grep -q 'python3-tk'; then \
        echo "Se requiere python3-tk para ejecutar este programa."; \
        echo "Por favor, proporcione permisos de superusuario para continuar."; \
        sudo apt install python3-tk; \
    else \
        echo "python3-tk ya está instalado."; \
    fi

# Regla para ejecutar el programa
run:
	antlr -Dlanguage=Python3 Pointer.g4
    $(PYTHON) pointer.py

.PHONY: install run
