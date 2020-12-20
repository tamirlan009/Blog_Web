
class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'fsjdkeyunxkdiopz'

    ### Flask-Security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
