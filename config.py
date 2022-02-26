from distutils.command.config import config
from distutils.debug import DEBUG
from sre_constants import CATEGORY

from pkg_resources import SOURCE_DIST


import os
class Config:
    '''
    General cnfiguration
    '''
    CATEGORY_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'
    SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    HEADLINE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    production configuration cild class
    '''
    pass

class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}