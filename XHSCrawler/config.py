# config.py
DB_CONFIG = {
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:123456@127.0.0.1:3306/xhs_data',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}

# Flask service configuration
APP_CONFIG = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': True
}
