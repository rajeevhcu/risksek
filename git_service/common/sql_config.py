"""mysql configuration file"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """mysql configuration to app"""
    APP_ROOT = os.path.join(os.path.dirname(__file__), '../../')
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.getenv("MYSQL_USER_ID") + ":" +\
                              os.getenv("MYSQL_PASSWORD") + "@" + os.getenv("MYSQL_HOST") + "/" + \
                              os.getenv("MYSQL_DATABASE") \
                              + "?host=" + os.getenv("MYSQL_HOST") + "?port=3306"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_MAX_OVERFLOW = 10