import logging
from PIL import Image

class Compressor(object):
    def __init__(self, img_in, img_out):
        self.img_in = img_in
        self.img_out = img_out 
        logging.basicConfig(filename='error.log', level=logging.ERROR)
    def save(self):
        try:
            self.image = Image.open(self.img_in)
            resized_image = self.image.resize((300, 300))
            resized_image.save(self.img_out, optimize=True, quality=50)
        except FileNotFoundError as e:
            logging.error(f"No se encontro el fichero: {e}")
