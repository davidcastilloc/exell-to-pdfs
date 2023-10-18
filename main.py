import pyfiglet
import pandas as pd
from tqdm import tqdm
from colorama import init, Fore
from dto.obra import ObraArteDTO
from helper.pdf_generator import PDFGenerator
from helper.config_module import Config
from helper.tools import clear
import os
__version__ = "1.0.0"

class PDFGeneratorInterface:
    def __init__(self):
        self.pdf_generator = None

    def run(self):
        init()
        clear()
        self.show_banner()
        if not Config().is_valid():
            #TODO: validar todas las rutas de la configuracion
            print(Fore.RED, "Error: ")
            input("La configuracion no se pudo cargar.\n")
            input("Presiona [ENTER] para salir...\n")
            return False
        Config().print_config()
        input("Presiona [ENTER] para continuar...\n")
        self._generate_pdfs()

    def show_banner(self):
        banner_text = pyfiglet.figlet_format("PDF Obras", font="slant")+ \
        '# pdf-obras @version: {}'.format(__version__)
        print(Fore.CYAN, banner_text)

    def _generate_pdfs(self):
        excel_file = Config().excell_route
        sheet_name = Config().sheet_name
        df = pd.read_excel(excel_file, sheet_name, engine="openpyxl")
        df.fillna('', inplace=True)
        #for df in df.values():
        #    df.fillna('N/A', inplace=True)
            
        for index, row in tqdm(df.iterrows(), desc="GenerandoPDF Obras", ascii='█', unit=' Obras'):
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
                valor_comercial=row["valor-comercial"],
                valor_realizacion=row["valor-realizacion"],
                metodologia=row["metodologia-y-funtes"]
            )
            pdf_output_path = Config().pdf_output_path
            template_path = Config().template_path

            # Use os.makedirs() with exist_ok=True to create the pdf_output_path directory if it doesn't exist.
            os.makedirs(pdf_output_path, exist_ok=True)

            output_file = os.path.join(pdf_output_path, f"Obra COD - {str(obra_dto.codigo)}.pdf")
            gpdf = PDFGenerator(template_path, output_file, obra_dto)
            gpdf.generate_pdf()


if __name__ == "__main__":
    interface = PDFGeneratorInterface()
    interface.run()
