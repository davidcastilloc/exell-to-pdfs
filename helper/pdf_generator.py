# clase propuesta para la solucion del problema
import locale
import logging
import os
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from helper.image_compressor import Compressor
from helper.config_module import Config
import textwrap
import datetime
import numbers

class PDFGenerator:
    def __init__(self, template_path, output_path, obra):
        self.template_path = template_path
        self.output_path = output_path
        self.obra = obra
        locale.setlocale(locale.LC_ALL, 'es_PE')

    def generate_pdf(self):
        template = PdfReader(self.template_path, decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(self.output_path)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        canvas.setFont("Helvetica", 7)

        self._draw_fields(canvas, self.obra)
        self._draw_images(canvas, self.obra)
        canvas.save()

    def _draw_fields(self, canvas, obra):
        obra = self.obra
        fields = [
            (91, 689,  obra.fecha ),
            (152, 620, obra.codigo ),
            (208, 602, obra.ubicacion_obra),
            (153,585, obra.distrito),
            (453,585, obra.departamento),
            (152,541, obra.autor),
            (152,525, obra.titulo_obra),
            (152,508, obra.medio),
            (153,490, obra.edicion),
            (253,490, obra.firma),
            (404,541, obra.nacionalidad),
            (404,525, obra.ano_creacion),
            (338,508, obra.tecnica),
            (91, 459, obra.observaciones_obra),
            (338,490, obra.medidas),
            (452,490, obra.estado),
            (91, 214-23, obra.valor_comercial),
            (335, 214-23, obra.valor_realizacion),
        ]
        
        textbox = [
            (91, 290, obra.artista),
            (335, 290, obra.metodologia)
        ]

        for x, y, text in textbox:
            max_chars_per_line = 60
            lines = textwrap.wrap(text, max_chars_per_line)
            for line in lines:
                canvas.drawString(x, y, line)
                y -= 12


        for x, y, text in fields:
            try:
                if isinstance(text, datetime.datetime):
                    canvas.drawString(x, y+1, text.strftime("%d %B, %Y"))
                elif isinstance(text, numbers.Number):
                    canvas.drawString(x, y+1, str(text))
                elif isinstance(text, str):
                    canvas.drawString(x, y+1, str(text))
            except Exception as e:
                logging.error(f"An exception occurred: {e}")
            

    def _draw_images(self, canvas, obra):
        # Coordenadas de la posicion de la imagen
        SCALE = 90
        coord_img = [
            (91+50, 328),
            (335+50, 328),
        ]

        if obra.codigo == 'nan':
            print(f"Image code invalid : {obra.codigo}")
            return
        
        IMG_A_IN_ROUTE = os.path.join(os.getcwd(), Config().img_route, f"{obra.registro_fotografico_a:08}.jpg")
        IMG_A_OUT_ROUTE =  os.path.join(os.getcwd(), Config().img_route,f"{obra.registro_fotografico_a:08}-opt.jpg")
        
        IMG_B_IN_ROUTE = os.path.join(os.getcwd(), Config().img_route, f"{obra.registro_fotografico_b:08}.jpg")
        IMG_B_OUT_ROUTE =  os.path.join(os.getcwd(), Config().img_route, f"{obra.registro_fotografico_b:08}-opt.jpg")
        
        #PINTAMOS LA CARA A DE LA OBRA
        if os.path.exists(IMG_A_IN_ROUTE):
            try:
                x , y = coord_img[0]
                Compressor(IMG_A_IN_ROUTE, IMG_A_OUT_ROUTE).save()
                canvas.drawImage(IMG_A_OUT_ROUTE, x, y, SCALE, SCALE)
            except Exception as e:
                print(e)

        #PINTAMOS LA CARA B DE LA OBRA
        if os.path.exists(IMG_B_IN_ROUTE):
            try:
                x , y = coord_img[1]
                Compressor(IMG_B_IN_ROUTE, IMG_B_OUT_ROUTE).save()
                canvas.drawImage(IMG_B_OUT_ROUTE, x, y, SCALE, SCALE)
            except Exception as e:
                print(e)
