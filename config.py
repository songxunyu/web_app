'''
全局配置文件
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    #开发环境
    DEBUG = True

class ProductionConfig(Config):
    # 生产环境
    pass
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
