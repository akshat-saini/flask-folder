import os
from configparser import ConfigParser


basedir = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(basedir, 'config.cfg')

config = ConfigParser()
config.read(config_file)
class Config:
    ENV = config.get('development','ENV')
    print
    if ENV in ['dev', 'DEV', 'development']:
        PORT = config.get('development','PORT')
        DEBUG = config.get('development','DEBUG')
        DATABASE_URI = config.get('development','DATABASE_URI')