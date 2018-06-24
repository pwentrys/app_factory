from os.path import join
from sys import path


NAME = 'App'
IP = '0.0.0.0'
PORT = 9001
PROJECT = path[0]
RESOURCES = join(PROJECT, 'resources')
STATIC = join(RESOURCES, 'static')
TEMPLATES = join(RESOURCES, 'templates')
DEBUG = True
SESSION_LIFETIME = 1
THREADED = True
