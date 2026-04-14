Proyecto = input("Escriba el nombre del proyecto: ")

Horas_estimadas = input("Escriba cuanto tiempo estima para este proyecto: ")

Valor_de_hora = input("Escriba cuanto valdra la hora trabajada: ")

Plazo_estimado = input("Escriba cuanto tiempo estima que tomara el proyecto: ")


print(Proyecto)
print(Horas_estimadas)
print(Valor_de_hora)
print(Plazo_estimado)

Valor_total = int(Horas_estimadas) * int(Valor_de_hora)
print(Valor_total)

#generador de PDF's
#1- Crear un PDF
#2- Definir un tipo de letra
#3- Llenar los datos
#4- Guardar entrgables

from fpdf import FPDF
pdf = FPDF()

pdf.add_page()
#Tipo de letra que queremos, en este caso (Arial)
pdf.set_font("Arial")

pdf.text(115, 145, Proyecto)
pdf.text(115, 160, Horas_estimadas)
pdf.text(115, 175, Valor_de_hora)
pdf.text(115, 190, Plazo_estimado)
pdf.text(115, 205, str(Valor_total))

from datetime import datetime
hoy = datetime.now().strftime("%d/%m/%Y")
pdf.text(115, 220, f"fecha: {hoy}")

pdf.output("Presupuesto.pdf")

print("Presupuesto generado con exito")