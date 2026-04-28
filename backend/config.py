import yaml
import os 

file =  __file__
BASE_DIR = os.path.dirname(os.path.abspath(file))

CONFIG_PATH = os.path.join(BASE_DIR, '..', 'config.yaml')

def load_config():
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)
    return config