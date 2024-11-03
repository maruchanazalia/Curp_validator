import tkinter as tk
from tkinter import ttk

# Lista de estados de México
estados_mexico = (
    "AGUASCALIENTES", "BAJA CALIFORNIA", "BAJA CALIFORNIA SUR", "CAMPECHE", "CHIAPAS", 
    "CHIHUAHUA", "CIUDAD DE MÉXICO", "COAHUILA", "COLIMA", "DURANGO", 
    "GUANAJUATO", "GUERRERO", "HIDALGO", "JALISCO", "MÉXICO", 
    "MICHOACÁN", "MORELOS", "NAYARIT", "NUEVO LEÓN", "OAXACA", 
    "PUEBLA", "QUERÉTARO", "QUINTANA ROO", "SAN LUIS POTOSÍ", "SINALOA", 
    "SONORA", "TABASCO", "TAMAULIPAS", "TLAXCALA", "VERACRUZ", 
    "YUCATÁN", "ZACATECAS"
)

def generar_curp(nombre, apellido_paterno, apellido_materno, dia, mes, año, sexo, estado):
    nombre = nombre.strip().upper()
    apellido_paterno = apellido_paterno.strip().upper()
    apellido_materno = apellido_materno.strip().upper()
    sexo = sexo.strip().upper()
    estado = estado.strip().upper()

    # Obtener primera letra y primera vocal interna del apellido paterno
    primera_letra_paterno = apellido_paterno[0]
    primera_vocal_paterno = next((c for c in apellido_paterno[1:] if c in 'AEIOU'), 'X')

    # Obtener primera letra del apellido materno y del nombre
    primera_letra_materno = apellido_materno[0] if apellido_materno else 'X'
    primera_letra_nombre = nombre[0]

    # Formar CURP básica
    curp = (primera_letra_paterno + primera_vocal_paterno + primera_letra_materno + primera_letra_nombre +
            año[2:] + mes + dia + sexo + estado[:2])

    # Añadir homoclave (ejemplo simple, en la realidad se genera más compleja)
    homoclave = "01"
    curp += homoclave

    return curp

def run_turing_machine(input_nombre, input_apellido_paterno, input_apellido_materno, 
                       input_dia, input_mes, input_año, input_sexo, input_estado):
    nombre = input_nombre.get()
    apellido_paterno = input_apellido_paterno.get()
    apellido_materno = input_apellido_materno.get()
    dia = input_dia.get()
    mes = input_mes.get()
    año = input_año.get()
    sexo = input_sexo.get()
    estado = input_estado.get()

    # Validar que los campos de fecha no estén vacíos
    if not (dia and mes and año):
        result_label.config(text="Error: Debe ingresar día, mes y año.")
        return
    
    curp = generar_curp(nombre, apellido_paterno, apellido_materno, dia.zfill(2), mes.zfill(2), año, sexo, estado)

    results_table.insert("", tk.END, values=(nombre, apellido_paterno + ' ' + apellido_materno, 
                                             f"{dia}/{mes}/{año}", estado, sexo, curp))
    return True

root = tk.Tk()
root.geometry("1280x720")
root.title("Generador de CURP")

# Etiquetas y campos de entrada para cada dato
input_label = tk.Label(root, text="Nombre")
input_label.pack()
input_field_nombre = tk.Entry(root)
input_field_nombre.pack()

input_label_apellido_paterno = tk.Label(root, text="Apellido Paterno")
input_label_apellido_paterno.pack()
input_field_apellido_paterno = tk.Entry(root)
input_field_apellido_paterno.pack()

input_label_apellido_materno = tk.Label(root, text="Apellido Materno")
input_label_apellido_materno.pack()
input_field_apellido_materno = tk.Entry(root)
input_field_apellido_materno.pack()

# Campos separados para día, mes y año
input_label_fecha_nacimiento = tk.Label(root, text="Fecha de Nacimiento")
input_label_fecha_nacimiento.pack()

input_label_dia = tk.Label(root, text="Día")
input_label_dia.pack()
input_field_dia = tk.Entry(root)
input_field_dia.pack()

input_label_mes = tk.Label(root, text="Mes")
input_label_mes.pack()
input_field_mes = tk.Entry(root)
input_field_mes.pack()

input_label_año = tk.Label(root, text="Año")
input_label_año.pack()
input_field_año = tk.Entry(root)
input_field_año.pack()

# Campo para el sexo (usando Combobox)
input_label_sexo = tk.Label(root, text="Sexo")
input_label_sexo.pack()
input_field_sexo = ttk.Combobox(root, values=["H", "M"])
input_field_sexo.pack()

# Campo para el estado (usando Combobox)
input_label_estado = tk.Label(root, text="Estado de Nacimiento")
input_label_estado.pack()
input_field_estado = ttk.Combobox(root, values=estados_mexico)
input_field_estado.pack()

# Botón de validación y tabla de resultados
run_button = tk.Button(root, text="Generar CURP", command=lambda: run_turing_machine(
    input_field_nombre, input_field_apellido_paterno, input_field_apellido_materno, 
    input_field_dia, input_field_mes, input_field_año, 
    input_field_sexo, input_field_estado
))
run_button.pack()

results_table = ttk.Treeview(root, columns=("Nombre", "Apellidos", "Fecha de nacimiento", "Entidad Federativa", "Sexo", "CURP"), show="headings")
results_table.heading("Nombre", text="Nombre")
results_table.heading("Apellidos", text="Apellidos")
results_table.heading("Fecha de nacimiento", text="Fecha de nacimiento")
results_table.heading("Entidad Federativa", text="Entidad Federativa")
results_table.heading("Sexo", text="Sexo")
results_table.heading("CURP", text="CURP")
results_table.pack()

result_label = tk.Label(root, text="", fg="red")
result_label.pack()

root.mainloop()
