import os

class Config:
    DEBUG = os.getenv('DEBUG', False)
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    # Add more configuration settings as needed
