import os


class BaseConfig(object):
    """Default configuration options."""
    SITE_NAME = os.environ.get('APP_NAME', 'Fitly')

    SECRET_KEY = 'secret'

    JWT_SECRET_KEY = 'secret'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'fitly')
    POSTGRES_PASS = os.environ.get('POSTGRES_PASS', 'fitly')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'postgres')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'fitly')

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASS,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    """Development configuration options."""
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False
