import pytest 
from helper.config_module import Config 
class TestConfig: 
    # Crear objeto Config con ruta de archivo de configuración predeterminada 
    def test_create_default_config_object(self): 
        config = Config() 
        assert config.config_route == 'config.ini' 
        assert config._config is not None 
    # Crear objeto Config con ruta de archivo de configuración personalizada 
    def test_create_custom_config_object(self): 
        config = Config('custom_config.ini') 
        assert config.config_route == 'custom_config.ini' 
        assert config._config is not None 
    # Llamar al método print_config para imprimir todos los valores de configuración 
    def test_print_config(self, capsys): 
        config = Config() 
        config.print_config() 
        captured = capsys.readouterr() 
        assert captured.out == '[section1]\nkey1 = value1\n\n[section2]\nkey2 = value2\n\n' 
    # El archivo de configuración no existe 
    def test_invalid_config_file_not_exist(self): 
        config = Config('nonexistent_config.ini') 
        assert not config.is_valid() 
    # El archivo de configuración no es legible 
    def test_invalid_config_file_not_readable(self): 
        config = Config('unreadable_config.ini') 
        assert not config.is_valid() 
    # El archivo de configuración no es escribible 
    def test_invalid_config_file_not_writable(self): 
        config = Config('unwritable_config.ini') 
        assert not config.is_valid() 
    # Llamar al método get_value para obtener un valor de configuración específico 
    def test_get_value(self): 
        config = Config() 
        value = config.get_value('section', 'key') 
        assert value == expected_value