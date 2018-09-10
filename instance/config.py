# instance/config.py


class Config(object):
    """Configuration for parent class"""
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    """Configuration for production"""


class DevelopmentConfig(Config):
    """Configuration for development"""
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    """Conficuration for testing"""
    DEBUG = True
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestConfig
}
