# clase propuesta para la solucion del problema
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from dto import ObraArteDTO


class PDFGenerator:
    def __init__(self, template_path, output_path):
        self.template_path = template_path
        self.output_path = output_path

    def generate_pdf(self):
        template = PdfReader(self.template_path, decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(self.output_path)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        canvas.setFont("Helvetica", 9)

        self._draw_fields(canvas)

        canvas.save()

    def _draw_fields(self, canvas, obra):
        fields = [
            (91, 689,  obra.fecha ),
            (152, 620, obra.codigo ),
            (208, 602, obra.ubicacion_obra),
            (153,585, obra.distrito),
            (453,585, obra.departamento),
            (152,541, obra.autor),
            (152,525, obra.titulo_obra),
            (152,508, obra.medio),
            (153,490, obra.tiraje),
            (404,541, obra.nacionalidad),
            (404,525, obra.ano_creacion),
            (404,507, obra.tecnica),
            (91, 459, obra.observaciones_obra),
            (338,490, obra.medidas),
            (452,490, obra.estado),
            (91, 412, obra.registro_fotografico),
            (91, 290, obra.artista),
            (91, 214, obra.valor_comercial),
        ]

        for x, y, text in fields:
            canvas.drawString(x, y, text)

if __name__ == "__main__":
    template_path = "template.pdf"
    output_path = "output.pdf"
    
    pdf_generator = PDFGenerator(template_path, output_path)
    pdf_generator.generate_pdf()
