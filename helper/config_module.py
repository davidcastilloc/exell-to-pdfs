import configparser
import os


class Config:
    def __init__(self, config_route='config.ini'):
        self.config_route = config_route
        self._config = None
        self._load_config()

    def _load_config(self):
        self._config = configparser.ConfigParser()
        self._config.read(self.config_route)

    @property
    def template_route(self):
        return self._get_config_value('Config', 'template_route')

    @property
    def debug(self):
        return self._get_config_boolean('Config', 'debug')

    @property
    def excell_route(self):
        return self._get_config_value('Data', 'excell_route')

    @property
    def img_route(self):
        return self._get_config_value('Data', 'img_route')

    @property
    def sheet_name(self):
        return self._get_config_value('Data', 'sheet_name')
    
    @property
    def template_path(self):
        return self._get_config_value('Config', 'template_route')

    @property
    def pdf_output_path(self):
        return self._get_config_value('Config', 'pdf_output_path')

    def print_config(self):
        for section in self._config.sections():
            print(f"[{section}]")
            for key, value in self._config.items(section):
                print(f"{key} = {value}")
            print()

    def _get_config_value(self, section, key):
        try:
            return self._config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None

    def _get_config_boolean(self, section, key):
        try:
            return self._config.getboolean(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return False

    def is_valid(self):
        # if config file is valid
        if not os.path.isfile('config.ini') or not os.access('config', os.R_OK | os.W_OK):
            return True
