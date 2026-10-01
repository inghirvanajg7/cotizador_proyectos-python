from fpdf import FPDF #import of the FPDF class from the fpdf module

#give the user a prompt to input the project name, estimated hours, hourly rate, and estimated time of the project
proyecto = input("Ingrese el nombre del proyecto: ")
horas_estimadas = input("Ingrese las horas estimadas: ")
valor_hora = input("Ingrese el valor por hora trabajada: ")
termino = input("Ingrese el tiempo estimado del proyecto: ")

valor_total = int(horas_estimadas) * float(valor_hora) #valor of the project

# Create a PDF instance
pdf = FPDF()
pdf.add_page()
# Set font and size
pdf.set_font("helvetica", size=12)  
pdf.image("Template.png", 0, 0) # Add a template image

pdf.text(115, 145, f"{proyecto}") # Add the project name to the PDF")
pdf.text(115, 160, f"{horas_estimadas}")
pdf.text(115, 175, f"{valor_hora}")
pdf.text(115, 190, f"{termino}")
pdf.text(115, 205, f"{str(valor_total)}")

#leave the file name as "cotizacion.pdf"
pdf.output("Cotizacion.pdf")
print("PDF generado exitosamente con el nombre 'Cotizacion.pdf'")
