from configparser import ConfigParser

config = ConfigParser()

config['DEFAULT'] = {
    'DB_NAME': 'db_name_default',
    'DB_USER': 'db_user_default',
    'DB_PASSWORD': 'db_password_default'
}

config['QA'] = {
    'ENVIRONMENT_NAME ': 'ix.qa',
    'BASE_URL': '.firestonecompleteautocare.com',
    'BROWSER ': 'chrome'
}

config['PRODUCTION'] = {
    'ENVIRONMENT_NAME ': 'ix.qa',
    'BASE_URL': '.firestonecompleteautocare.com',
    'BROWSER ': 'chrome'
}

with open('./config.ini', 'w') as f:
    config.write(f)
