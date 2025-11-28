from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename, encoding='utf-8')

    if not parser.has_section(section):
        raise Exception(f'Section {section} not found in {filename}')

    config = {}
    for key, value in parser.items(section):
        config[key] = value
    return config

if __name__ == '__main__':
    cfg = load_config()
    print(cfg)
