""" index file for REST APIs using Flask """
import os
import sys
import requests
from flask import jsonify, request, make_response, send_from_directory

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOTH_PATH' : ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))