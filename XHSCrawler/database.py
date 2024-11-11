# database.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import MEDIUMTEXT, LONGTEXT

from XHSCrawler.config import DB_CONFIG
import logging

db = SQLAlchemy()

def init_db(app):
    """Initialize the database connection."""
    app.config.update(DB_CONFIG)
    db.init_app(app)

class ScrapedData(db.Model):
    """the database ORM."""
    __tablename__ = 'xhs_content'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    description = db.Column(LONGTEXT)
    images = db.Column(LONGTEXT)

    def __init__(self, title, description, images):
        self.title = title
        self.description = description
        self.images = images

# 获取当前模块的日志记录器
logger = logging.getLogger(__name__)

def save_data(detail_title, detail_desc, image_urls):
    """Save scraped data to the database."""
    images = ','.join(image_urls)
    data = ScrapedData(title=detail_title, description=detail_desc, images=images)
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        # 捕获并记录异常
        db.session.rollback()  # 回滚数据库会话，以确保后续操作不受影响
        logger.error(f"Failed to save data to the database: {e}")
