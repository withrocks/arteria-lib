import jsonpickle

class ConfigurationService:

    def __init__(self, path):
        self._config_loaded = False
        self._path = path

    def _load_config_file(self, from_cache=True):
        if not self._config_loaded or not from_cache:
            self._config_file = ConfigurationFile.read(self._path)
            print "Read config file from {0}".format(self._path)
        self._config_loaded = True

    def port(self):
        self._load_config_file()
        return self._config_file.port

    def monitored_directories(self, host):
        self._load_config_file()
        return self._config_file.monitored_directories


class ConfigurationFile:
    """Represents a json serialized configuration file"""
    def __init__(self, monitored_directories, port):
        self.monitored_directories = monitored_directories
        self.port = port

    @staticmethod
    def read(path):
        with open(path, 'r') as f:
            json = f.read()
            return jsonpickle.decode(json)

    @staticmethod
    def write(path, obj):
        jsonpickle.set_encoder_options(
            'simplejson', sort_keys=True, indent=4)
        with open(path, 'w') as f:
            json = jsonpickle.encode(obj)
            f.write(json)
