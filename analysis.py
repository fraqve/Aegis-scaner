import json



def load_config(config_file:str):
    with open(config_file) as file:
        config = json.load(file)
    return config





