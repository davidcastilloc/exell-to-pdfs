import pyfiglet
import pandas as pd
from tqdm import tqdm
import time
from colorama import init, Fore
from dto.obra import ObraArteDTO
from helper.pdf_generator import PDFGenerator
from helper.config_module import Config

class PDFGeneratorInterface:
    def __init__(self):
        self.pdf_generator = None

    def run(self):
        init()
        self.show_banner()
        print(Fore.GREEN,"Bienvenido al generador de PDF.")
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
        conf = Config()
        df = pd.read_excel(conf.excell_route, sheet_name, engine="openpyxl")
        df.fillna('N/A', inplace=True)
        
        #Leemos los datos necesarios del excell
        for index, row in tqdm(df.iterrows(), desc="GenerandoPDF Obras",ascii='█', unit=' Obra'):
            obra_dto = ObraArteDTO(
                fecha=row['fecha-de-inspeccion'],
                firma=row['firma'],
                codigo=row['codigo'],
                ubicacion_obra=row["ubicacion"],
                distrito=row['distrito'],
                departamento=row['departamento'],
                autor=row['autor'],
                titulo_obra=row['titulo'],
                medio=row['medio'],
                edicion=row['edicion'],
                nacionalidad=row['nacionalidad'],
                ano_creacion=row["anho-de-creacion"],
                tecnica=row["tecnica"],
                observaciones_obra=row["observacion"],
                medidas=row["medida-sin-marco"],
                estado=row["estado"],
                registro_fotografico_a=row["registro-foto-a"],
                registro_fotografico_b=row["registro-foto-b"],
                artista=row["artista"],
                valor_comercial=row["valor-comercial"]
            )
            gpdf = PDFGenerator("template.pdf", "output/Obra-COD-" + str(obra_dto.codigo) + ".pdf", obra_dto )
            gpdf.generate_pdf()

if __name__ == "__main__":
    interface = PDFGeneratorInterface()
    conf_loader = Config()
    conf_loader.render_config()
    interface.run()
