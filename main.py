import tkinter as tk
from tkinter import ttk
import re
from datetime import datetime

def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def validar_curp(curp):
    curp_regex = re.compile(
        r"^[A-Z]{4}"        
        r"\d{2}"            
        r"(0[1-9]|1[0-2])" 
        r"(0[1-9]|[12]\d|3[01])" 
        r"[HM]"    #sex when?
        r"(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS)" 
        r"[A-Z]{3}"      
        r"[0-9A-Z]\d$"     
    )
    
    if not curp_regex.match(curp):
        return "Formato de CURP no válido."
    
    anio = int(curp[4:6]) + 1900 if int(curp[4:6]) >= 20 else int(curp[4:6]) + 2000
    mes = int(curp[6:8])
    dia = int(curp[8:10])

    try:
        fecha = datetime(anio, mes, dia)
    except ValueError:
        return "Fecha no válida en la CURP."

    if mes == 2 and dia == 29 and not es_bisiesto(anio):
        return "Año no bisiesto, fecha incorrecta en CURP."

    return "CURP válida."

def ejecutar_validacion():
    curp = entrada.get().upper()
    resultado = validar_curp(curp)
    
    if resultado == "CURP válida.":
        tabla_resultados.insert("", "end", values=(curp, resultado))
        mensaje_resultado.config(text="")
    else: 
        mensaje_resultado.config(text=resultado, fg="red")

root = tk.Tk()
root.title("Máquina de Turing - Validación de CURP Mexicana")

etiqueta_entrada = tk.Label(root, text="Ingrese una CURP:")
etiqueta_entrada.pack()

entrada = tk.Entry(root)
entrada.pack()

boton_ejecutar = tk.Button(root, text="Validar CURP", command=ejecutar_validacion)
boton_ejecutar.pack()

tabla_resultados = ttk.Treeview(root, columns=("CURP", "Resultado"), show="headings")
tabla_resultados.heading("CURP", text="CURP")
tabla_resultados.heading("Resultado", text="Resultado")
tabla_resultados.pack()

mensaje_resultado = tk.Label(root, text="")
mensaje_resultado.pack()

root.mainloop()
