import configparser as cp


class PropertyReader:

    def __init__(self, property_file):
        self.property_file = property_file
        self.config_parser = cp.ConfigParser()
        self.config_parser.optionxform = str
        prop_file_promo = open(self.property_file)
        prop_file_promo.close()
        self.config_parser.read(self.property_file)

    def get_property(self, sec_name, prop_name) -> str:
        return self.config_parser.get(sec_name, prop_name)
