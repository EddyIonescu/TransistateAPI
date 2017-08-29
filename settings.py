import configparser

MONGO_HOST = '54.183.239.250'
MONGO_PORT = 27017


MONGO_DBNAME = 'transistate'

def getUsername():
    config = configparser.ConfigParser()
    config.read("keys")
    return config["mongo"]["username"]

def getPassword():
    config = configparser.ConfigParser()
    config.read("keys")
    return config["mongo"]["password"]

MONGO_USERNAME = getUsername()
MONGO_PASSWORD = getPassword()

DOMAIN = {'agencies': {}, 'vehicles': {}, '1503213592': {}}
ALLOW_UNKNOWN = True
