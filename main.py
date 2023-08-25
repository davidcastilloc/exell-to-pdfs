import pyfiglet
import pandas as pd
from tqdm import tqdm
import time
from colorama import init, Fore
from dto.obra import ObraArteDTO
from helper.pdf_generator import PDFGenerator

class PDFGeneratorInterface:
    def __init__(self):
        self.pdf_generator = None

    def run(self):
        init()
        self.show_banner()
        print(Fore.GREEN,"Bienvenido al generador de PDF")
        self._generate_pdfs()

    def show_banner(self):
        banner_text = pyfiglet.figlet_format("PDF Obras", font="slant")
        print(banner_text)

    def _get_input_paths(self):
        self.template_path = input("Ingrese la ruta del archivo de plantilla PDF: ")
        self.output_path = input("Ingrese la ruta de salida para el archivo PDF generado: ")
        #self.pdf_generator = PDFGenerator(self.template_path, self.output_path)

    def _generate_pdfs(self):
        # Leer el archivo Excel
        excel_file = "test.xlsx"  # Definimos la ruta del excell
        sheet_name = "Hoja1"  # Definimos el nombre de la hoja.
        df = pd.read_excel(excel_file, sheet_name, engine="openpyxl")
        #Leemos los datos necesarios del excell
        for index, row in tqdm(df.iterrows(), desc="GenerandoPDF Obras",ascii='█', unit=' Obra'):
            time.sleep(1)
            obra_dto = ObraArteDTO(
                fecha=row['FECHA de inspeccion'],
                codigo=row['codigo'],
                ubicacion_obra=row["Ubicación"],
                distrito=row['Distrito'],
                departamento=row['Departamento'],
                autor=row['Autor'],
                titulo_obra=row['titulo'],
                medio=row['medio'],
                tiraje=row['tiraje'],
                nacionalidad="Nacionalidad",
                ano_creacion=row["Año de creación"],
                tecnica=row["técnica"],
                observaciones_obra=row["OBSERVACION"],
                medidas=row["Medida sin marco"],
                estado=row["estado"],
                registro_fotografico=row["REGISTRO FOTO"],
                artista=row["artista"],
                valor_comercial=row["VALOR COMERCIAL"]
            )
            gpdf = PDFGenerator("template.pdf", "output\\Obra COD - " + str(obra_dto.codigo)+ ".pdf", obra_dto )
            gpdf.generate_pdf()


    

if __name__ == "__main__":
    interface = PDFGeneratorInterface()
    interface.run()
