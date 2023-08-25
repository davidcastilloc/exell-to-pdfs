import pyfiglet
import pandas as pd

# Leer el archivo Excel
excel_file = "test.xlsx"  # Definimos la ruta del excell
sheet_name = "Hoja1"  # Definimos el nombre de la hoja.
df = pd.read_excel(excel_file, sheet_name, engine="openpyxl")


class PDFGeneratorInterface:
    def __init__(self):
        self.pdf_generator = None

    def run(self):
        self.show_banner()
        print("Bienvenido al generador de PDF")
        self._get_input_paths()
        self.pdf_generator.generate_pdf()

    def show_banner(self):
        banner_text = pyfiglet.figlet_format("PDF Generator", font="slant")
        print(banner_text)

    def _get_input_paths(self):
        self.template_path = input("Ingrese la ruta del archivo de plantilla PDF: ")
        self.output_path = input("Ingrese la ruta de salida para el archivo PDF generado: ")
        #self.pdf_generator = PDFGenerator(self.template_path, self.output_path)
    
    def _generatePdfFromExellData():
        df = pd.read_excel(excel_file, sheet_name, engine="openpyxl")
    

if __name__ == "__main__":
    interface = PDFGeneratorInterface()
    interface.run()
