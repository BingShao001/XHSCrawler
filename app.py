# app.py
from flask import Flask, request, jsonify
from XHSCrawler.database import init_db, save_data, db
from XHSCrawler.crawler import crawl_data
from XHSCrawler.config import APP_CONFIG
from XHSCrawler.logging_config import setup_logging

app = Flask(__name__)
init_db(app)
setup_logging(app)
# 500 错误处理程序
@app.errorhandler(500)
def internal_error(error):
    app.logger.error("An internal error occurred: %s", error)
    return jsonify(error="Internal Server Error"), 500


@app.route('/crawl', methods=['POST'])
def crawl():
    """Receive URL and scrape data."""
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    try:
        title, desc, images = crawl_data(url)
        save_data(title, desc, images)
        return jsonify({
            "title": title,
            "description": desc,
            "images": images
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
def main():
    # 启动 Flask 应用
    app.run(**APP_CONFIG)

if __name__ == '__main__':
    main()


