import os

from app import create_app
from app.config import Config

app = create_app()

# Set maximum upload size
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1024 MB

def init_data():
    """You may put your init programs here"""
    pass 

if __name__ == '__main__':
    init_data()
    app.run(host=Config.HOST, port=Config.PORT, debug=True)
