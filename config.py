import os
import sys
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-duper-difficult-password-666'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'vtmchars.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
