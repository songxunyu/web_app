'''
启动
'''
import os
from app import app_create

#创建程序实例
app = app_create(os.getenv('FLASK_CONFIG') or 'production')


if __name__ == '__main__':
    app.run()