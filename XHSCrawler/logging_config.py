# logging_config.py
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(app):
    # 创建日志文件目录
    if not os.path.exists('logs'):
        os.mkdir('logs')

    # 配置日志记录
    file_handler = RotatingFileHandler('logs/flask_app.log', maxBytes=10240, backupCount=10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))

    # 将日志处理器添加到 Flask 应用的日志
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

    # 在应用启动时记录日志
    app.logger.info('Flask application startup')
