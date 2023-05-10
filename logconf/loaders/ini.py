import configparser
import io
from logconf import PARAMS

def load(conf_file):
    """Get configuration values from JSON file.
    """
    conf = {}
    with open(conf_file, 'r') as stream:
        conf_string = io.StringIO(stream.read())
        conf_ini = configparser.ConfigParser()
        conf_ini.read_file(conf_string)
        for param in PARAMS:
            if param in conf_ini['logconf']:
                conf[param] = conf_ini['logconf'][param]
    return conf
