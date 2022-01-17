import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URL') or "mysql+pymysql://root:root@127.0.0.1:3306/test_2?charset=utf8"
