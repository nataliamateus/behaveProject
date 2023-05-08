import configparser


def config_file_read():
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    print(parser.sections())

    for section in parser.sections():
        print(f'{section}')
        print(parser.get('[QA]', 'environment_name'))
        print(parser.get('[QA]', 'base_url'))
        print(parser.get('[QA]', 'browser'))


