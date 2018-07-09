'''
程序实例配置
'''

#设置模块引入路径为上级
import sys
sys.path.append('..')

from flask import Flask
from config import config


def app_create(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #配置各功能模块路由
    from .api_learn import api_learn
    app.register_blueprint(api_learn)
    return app
