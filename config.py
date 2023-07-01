import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def get_db_name():
    return config['database']['db_name']


def get_app_title():
    return config['title']['app_title']
