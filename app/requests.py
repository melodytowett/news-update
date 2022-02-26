from concurrent.futures import process
from unicodedata import category
import urllib.request,json

from models import Article,Source

api_key = None
category_url = None
source_url = None
headline_url = None

def configure_request(app):
    '''
    Fuctiona to configure request
    '''
    global api_key,category_url,source_url,headline_url
    api_key = app.config['NEWS_API_KEY']
    category_url = app.config['CATEGORY_URL']
    source_url = app.config['SOURCE_URL']
    headline_url = app.confg['HEADLINE_URL']


def get_category(category):
    '''
    Fuction that gets the json respone to the url request
    '''
    get_category_url = category_url.format(category,api_key)
    with urllib.request.urlopen(get_category_url)as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        category_results = None

        if get_category_response['results']:
            category_results_list = get_category_response['results']
            category_results = process_results(category_results_list)

    return category_results

def process_results(category_list):
    '''
    Function to process the news category 
    '''