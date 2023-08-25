# para compilar a ejecutable
pyinstaller --add-data "C:/Users/pc911/github-repos/python/venv/Lib/site-packages/pyfiglet;./pyfiglet" --onefile main.py

# solo click al ejecutable y el proceso iniciara automaticamente

# Requisitos para funcionar..

En el directorio del ejecutable deben estar 2 archivos
el archivo de plantilla para el pdf
y el fichero de excell de donde se leeran los registros
