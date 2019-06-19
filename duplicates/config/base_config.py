
class BaseConfig(object):
    DOCKER_INTERNAL_URI = 'host.docker.internal'

    DEBUG = True
    VERBOSE = True

    SECRET_KEY = 'my_precious'
    SECURITY_PASSWORD_SALT = 'my_precious_two'
