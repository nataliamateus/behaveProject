import configparser
import io


def create_allure_environment(path, values):
    buf = io.StringIO()
    config = configparser.ConfigParser()

    for (key, value) in values.items():
        config.set("", option=key, value=value)

    config.write(buf)
    buf.seek(0)
    next(buf)

    with open(f'reports/{path}/environment.properties', 'w+') as file:
        file.write(buf.read())
